import pandapower.networks as pn
import pandapower as pp
import numpy as np
import matplotlib.pyplot as plt

def DFLieee33(wind_power,sunny_power):
    pi_G=10
    pi_T=20
    pi_P=100
    pi_curtail=50

    net = pn.case33bw()#IEEE33

    # 放大所有负荷 1.05 倍
    net.load['p_mw'] *= 1.05
    net.load['q_mvar'] *= 1.05

    # 记录原始可再生能源容量
    original_wind_total = wind_power * 3  # 3个风电节点
    original_solar_total = sunny_power * 3  # 3个太阳能节点
    
    
    
    #每个节点功率相同
    #风电
    wind_buses = [18, 25, 30]
    for bus in wind_buses:
        pp.create_sgen(net, bus=bus-1, p_mw=wind_power, q_mvar=0.0, name=f"Wind_{bus}")


    #太阳能
    solar_buses = [6, 15, 22]
    for i, bus in enumerate(solar_buses):
        pp.create_sgen(net, bus=bus-1, p_mw=sunny_power, q_mvar=0.0, name=f"Solar_{bus}")


    #DG 发电机
    dg_buses = [7, 13, 17]
    dg_bus_indices = [bus - 1 for bus in dg_buses]
    for i in dg_bus_indices:
        pp.create_sgen(net, bus=i, p_mw=1.0, q_mvar=0.0, name=f"DG at Bus {i+1}")

    #储能
    storage_buses = [12, 21, 29]
    for bus in storage_buses:
        pp.create_storage(net, bus=bus-1, p_mw=0.0, max_e_mwh=1.0, soc_percent=50,
                          q_mvar=0.0, min_e_mwh=0.0, name=f"Storage_{bus}")


    #电压限制
    net.bus["min_vm_pu"] = 0.9
    net.bus["max_vm_pu"] = 1.05


    pp.runpp(net)

    ## 新增：计算弃风弃光惩罚项
    # 获取实际发出的可再生能源功率
    wind_sgen_indices = [i for i, name in enumerate(net.sgen['name']) if 'Wind' in str(name)]
    solar_sgen_indices = [i for i, name in enumerate(net.sgen['name']) if 'Solar' in str(name)]
    
    actual_wind_total = net.res_sgen.iloc[wind_sgen_indices]['p_mw'].sum()
    actual_solar_total = net.res_sgen.iloc[solar_sgen_indices]['p_mw'].sum()

    # print(original_wind_total)
    # print(original_solar_total)
    # print(actual_solar_total)
    # print(actual_wind_total)

    # 计算弃风弃光量
    wind_curtailment = max(0, original_wind_total - actual_wind_total)
    solar_curtailment = max(0, original_solar_total - actual_solar_total)
    total_curtailment = wind_curtailment + solar_curtailment

    #Cost
    total_dg_mw = net.res_sgen['p_mw'].sum()
    total_grid_mw = net.res_ext_grid['p_mw'].sum()
    vm_pu = net.res_bus['vm_pu']
    # voltage_violations = np.maximum(0, vm_pu - net.bus["max_vm_pu"]) + np.maximum(0, net.bus["min_vm_pu"] - vm_pu)
    # cp = pi_P * voltage_violations.sum()

    # 弃风弃光惩罚成本
    curtailment_penalty = pi_curtail * total_curtailment
    #print("惩罚项",curtailment_penalty)
    
    # 总成本 = DG成本 + 主网成本 + 弃风弃光惩罚成本
    total_cost = total_dg_mw * pi_G + total_grid_mw * pi_T + curtailment_penalty
    


    #决策
    #print("voltage cost",cp)
    # print("voltage cost",cp)
    # print(total_dg_mw)
    # print(total_grid_mw)
    #total_cost = total_dg_mw * pi_G + total_grid_mw * pi_T+cp
    
    return total_cost,vm_pu 

if __name__ == "__main__":
    predicted_p_mw = [0.12, 0.15, 0.10, 0.14, 0.16, 0.11, 0.09, 0.10, 0.13, 0.12, 0.10, 0.11] #12stations
    cost,vm_pu=DFLieee33(predicted_p_mw)
    print(cost) 

    plt.plot(vm_pu)
    plt.show()

