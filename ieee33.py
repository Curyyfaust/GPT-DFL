import pandapower.networks as pn
import pandapower as pp
import numpy as np
import matplotlib.pyplot as plt

# def DFLieee33(wind_power, sunny_power, voltage_tolerance=0.05):
#     pi_G = 10
#     pi_T = 20
#     pi_P = 100
#     pi_curtail = 50

#     net = pn.case33bw()  # IEEE33

#     # 放大所有负荷 2.5 倍
#     net.load['p_mw'] *= 2.5
#     net.load['q_mvar'] *= 2.5

#     # 记录原始可再生能源容量
#     original_wind_total = wind_power * 3  # 3个风电节点
#     original_solar_total = sunny_power * 3  # 3个太阳能节点
    
#     # 每个节点功率相同
#     # 风电 - 设置为可控制的静态发电机
#     wind_buses = [18, 25, 30]
#     for bus in wind_buses:
#         pp.create_sgen(net, bus=bus-1, p_mw=wind_power, q_mvar=0.0, 
#                       controllable=True, max_p_mw=wind_power, min_p_mw=0.0,
#                       name=f"Wind_{bus}")

#     # 太阳能 - 设置为可控制的静态发电机
#     solar_buses = [6, 15, 22]
#     for i, bus in enumerate(solar_buses):
#         pp.create_sgen(net, bus=bus-1, p_mw=sunny_power, q_mvar=0.0,
#                       controllable=True, max_p_mw=sunny_power, min_p_mw=0.0,
#                       name=f"Solar_{bus}")

#     # DG 发电机
#     dg_buses = [7, 13, 17]
#     dg_bus_indices = [bus - 1 for bus in dg_buses]
#     for i in dg_bus_indices:
#         pp.create_sgen(net, bus=i, p_mw=1.0, q_mvar=0.0, name=f"DG at Bus {i+1}")

#     # 储能
#     storage_buses = [12, 21, 29]
#     for bus in storage_buses:
#         pp.create_storage(net, bus=bus-1, p_mw=0.0, max_e_mwh=1.0, soc_percent=50,
#                           q_mvar=0.0, min_e_mwh=0.0, name=f"Storage_{bus}")

#     # 松弛后的电压限制 - 增加容忍度
#     min_voltage = 0.9 - voltage_tolerance  # 默认 0.85
#     max_voltage = 1.1 + voltage_tolerance  # 默认 1.15
    
#     net.bus["min_vm_pu"] = min_voltage
#     net.bus["max_vm_pu"] = max_voltage

#     # 运行潮流计算
#     try:
#         pp.runpp(net)
        
#         # 使用松弛后的电压约束检查
#         vm_pu = net.res_bus['vm_pu']
#         voltage_violations = ((vm_pu < min_voltage) | (vm_pu > max_voltage)).any()
        
#         if voltage_violations or not net.converged:
#             # 逐步削减可再生能源直到电压满足松弛后的约束
#             curtailment_factor = 1.0
#             while (voltage_violations or not net.converged) and curtailment_factor > 0.1:
#                 curtailment_factor -= 0.05
                
#                 # 重新创建网络
#                 net = pn.case33bw()
#                 net.load['p_mw'] *=  2.5
#                 net.load['q_mvar'] *= 2.5
                
#                 # 应用削减后的风电
#                 for bus in wind_buses:
#                     pp.create_sgen(net, bus=bus-1, p_mw=wind_power*curtailment_factor, 
#                                   q_mvar=0.0, name=f"Wind_{bus}")
                
#                 # 应用削减后的太阳能
#                 for i, bus in enumerate(solar_buses):
#                     pp.create_sgen(net, bus=bus-1, p_mw=sunny_power*curtailment_factor, 
#                                   q_mvar=0.0, name=f"Solar_{bus}")
                
#                 # DG 发电机
#                 for i in dg_bus_indices:
#                     pp.create_sgen(net, bus=i, p_mw=1.0, q_mvar=0.0, name=f"DG at Bus {i+1}")
                
#                 # 储能
#                 for bus in storage_buses:
#                     pp.create_storage(net, bus=bus-1, p_mw=0.0, max_e_mwh=1.0, soc_percent=50,
#                                       q_mvar=0.0, min_e_mwh=0.0, name=f"Storage_{bus}")
                
#                 # 松弛后的电压限制
#                 net.bus["min_vm_pu"] = min_voltage
#                 net.bus["max_vm_pu"] = max_voltage
                
#                 try:
#                     pp.runpp(net)
#                     vm_pu = net.res_bus['vm_pu']
#                     voltage_violations = ((vm_pu < min_voltage) | (vm_pu > max_voltage)).any()
#                 except:
#                     voltage_violations = True
#                     net.converged = False
                    
#     except:
#         pass

#     # 计算实际发出的可再生能源功率
#     wind_sgen_indices = [i for i, name in enumerate(net.sgen['name']) if 'Wind' in str(name)]
#     solar_sgen_indices = [i for i, name in enumerate(net.sgen['name']) if 'Solar' in str(name)]
    
#     actual_wind_total = net.res_sgen.iloc[wind_sgen_indices]['p_mw'].sum()
#     actual_solar_total = net.res_sgen.iloc[solar_sgen_indices]['p_mw'].sum()

#     # 计算弃风弃光量
#     wind_curtailment = max(0, original_wind_total - actual_wind_total)
#     solar_curtailment = max(0, original_solar_total - actual_solar_total)
#     total_curtailment = wind_curtailment + solar_curtailment

#     # 成本计算
#     dg_sgen_indices = [i for i, name in enumerate(net.sgen['name']) if 'DG' in str(name)]
#     total_dg_mw = net.res_sgen.iloc[dg_sgen_indices]['p_mw'].sum()
#     total_grid_mw = net.res_ext_grid['p_mw'].sum()
#     vm_pu = net.res_bus['vm_pu']

#     # 弃风弃光惩罚成本
#     curtailment_penalty = pi_curtail * total_curtailment
    
#     # 总成本 = DG成本 + 主网成本 + 弃风弃光惩罚成本
#     total_cost = total_dg_mw * pi_G + total_grid_mw * pi_T + curtailment_penalty

#     # 计算新能源消纳率
#     total_renewable_capacity = original_wind_total + original_solar_total
#     total_renewable_output = actual_wind_total + actual_solar_total
#     renewable_utilization_rate = (total_renewable_output / total_renewable_capacity * 100) if total_renewable_capacity > 0 else 0

#     return total_cost, vm_pu

def DFLieee33(wind_power, sunny_power):
    pi_G = 10
    pi_T = 20
    pi_S = 5  # 储能成本（通常比DG便宜）
    
    net = pn.case33bw()  # IEEE33
    
    # 放大所有负荷
    net.load['p_mw'] *= 1.2
    net.load['q_mvar'] *= 1.2
    
    # 将线路阻抗除以2
    net.line['r_ohm_per_km'] /= 2
    net.line['x_ohm_per_km'] /= 2
    
    # 记录原始可再生能源容量
    original_wind_total = wind_power * 2  # 2个风电节点
    original_solar_total = sunny_power * 2  # 2个太阳能节点
    
    # 风电 - 设置为可控制的静态发电机
    wind_buses = [18, 25]
    for bus in wind_buses:
        pp.create_sgen(net, bus=bus-1, p_mw=wind_power, q_mvar=0.0,
                      controllable=True, max_p_mw=wind_power, min_p_mw=0.0,
                      name=f"Wind_{bus}")
    
    # 太阳能 - 设置为可控制的静态发电机
    solar_buses = [6, 15]
    for i, bus in enumerate(solar_buses):
        pp.create_sgen(net, bus=bus-1, p_mw=sunny_power, q_mvar=0.0,
                      controllable=True, max_p_mw=sunny_power, min_p_mw=0.0,
                      name=f"Solar_{bus}")
    
    # DG 发电机
    dg_buses = [7, 13, 17]
    dg_bus_indices = [bus - 1 for bus in dg_buses]
    for i in dg_bus_indices:
        pp.create_sgen(net, bus=i, p_mw=1.0, q_mvar=0.0, name=f"DG at Bus {i+1}",
                       controllable=True, min_p_mw=0.0, max_p_mw=2.0, min_q_mvar=-0.5, max_q_mvar=0.5)
    
    # 储能
    storage_buses = [12, 21, 29]
    for bus in storage_buses:
        pp.create_storage(net, bus=bus-1, p_mw=0.0, max_e_mwh=1.0, soc_percent=50,
                          q_mvar=0.0, min_e_mwh=0.0, name=f"Storage_{bus}",
                          max_p_mw=1.0, min_p_mw=-1.0)  # 允许充放电
    
    # 删除现有的成本函数
    if len(net.poly_cost) > 0:
        net.poly_cost.drop(net.poly_cost.index, inplace=True)
    
    # 为外部电网设置购电成本函数
    for idx in net.ext_grid.index:
        pp.create_poly_cost(net, element=idx, et="ext_grid", cp1_eur_per_mw=pi_T)
    
    # 为所有可控的分布式电源设置成本函数
    
    for idx in net.sgen[net.sgen['controllable'] == True].index:
        sgen_name = net.sgen.loc[idx, 'name']
        if 'DG' in str(sgen_name):
            pp.create_poly_cost(net, element=idx, et="sgen", cp1_eur_per_mw=pi_G)
    # 运行最优潮流
    try:
        pp.runopp(net)
        #print("最优潮流求解成功")
    except:
        print("最优潮流求解失败")
        return None, None, None
    
    # 计算总成本
    ext_grid_cost = sum(net.res_ext_grid['p_mw'] * pi_T)
    sgen_cost = sum(net.res_sgen['p_mw'] * pi_G)
    storage_cost = sum(abs(net.res_storage['p_mw']) * pi_S)  # 储能成本按绝对值计算
    total_cost = ext_grid_cost + sgen_cost + storage_cost

    # 提取电压
    vm_pu = net.res_bus['vm_pu'].values
    
    # 提取决策变量
    # 外部电网功率
    ext_grid_p = net.res_ext_grid['p_mw'].values
                                                                                                                          
    # 可控分布式电源功率
    sgen_p = net.res_sgen['p_mw'].values
    
    # 储能功率
    storage_p = net.res_storage['p_mw'].values
    
    # 合成决策变量数组：[外部电网功率, 分布式电源功率, 储能功率]
    decision_vars = np.concatenate([ext_grid_p, sgen_p, storage_p])
    
    # 合成电压和决策变量
    combined_array = np.concatenate([vm_pu, decision_vars])
    
    return total_cost, decision_vars

if __name__ == "__main__":
    predicted_p_mw = [0.12, 0.15, 0.10, 0.14, 0.16, 0.11, 0.09, 0.10, 0.13, 0.12, 0.10, 0.11] #12stations
    cost,vm_pu=DFLieee33(predicted_p_mw)
    print(cost) 

    plt.plot(vm_pu)
    plt.show()

