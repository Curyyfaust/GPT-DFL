import pandapower.networks as pn
import pandapower as pp
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def ieee141():
    net = pp.create_empty_network()

    #pp.create_ext_grid(net, bus=bus_map[0], vm_pu=1.0, name="Slack Bus")
    bus_map = {}
    for bus_id in range(1, 142):
        bus_map[bus_id] = pp.create_bus(net, vn_kv=12.66, name=f"Bus {bus_id}")

    pp.create_ext_grid(net, bus=bus_map[1], vm_pu=1.0, name="Slack", 
                   max_p_mw=10.0, min_p_mw=0.0, 
                   max_q_mvar=10.0, min_q_mvar=-10.0)

    line_data = [(1, 2, 0.0289, 0.0205),
        (2, 3, 0.0863, 0.0612),
        (3, 4, 0.0005, 0.0003),
        (4, 5, 0.0046, 0.0033),
        (5, 6, 0.0034, 0.0025),
        (6, 7, 0.0235, 0.0313),
        (7, 8, 0.0368, 0.0491),
        (8, 9, 0.0325, 0.023),
        (9, 10, 0.0254, 0.018),
        (10, 11, 0.0058, 0.0041),
        (11, 12, 0.0646, 0.0457),
        (12, 13, 0.0614, 0.0433),
        (13, 14, 0.0244, 0.0173),
        (14, 15, 0.0479, 0.0339),
        (15, 16, 0.043, 0.0305),
        (16, 17, 0.0199, 0.0141),
        (17, 18, 0.0414, 0.0283),
        (18, 19, 0.0093, 0.0066),
        (19, 20, 0.028, 0.0198),
        (20, 21, 0.0183, 0.0123),
        (21, 22, 0.0287, 0.0154),
        (22, 23, 0.0132, 0.0096),
        (23, 24, 0.0342, 0.0249),
        (24, 25, 0.0199, 0.0141),
        (25, 26, 0.0365, 0.0265),
        (26, 27, 0.0168, 0.0122),
        (27, 28, 0.0292, 0.0207),
        (28, 29, 0.0328, 0.0232),
        (61, 62, 0.0206, 0.0146),
        (60, 63, 0.0177, 0.0125),
        (63, 64, 0.0524, 0.0371),
        (64, 65, 0.0337, 0.0239),
        (65, 66, 0.0151, 0.0107),
        (66, 67, 0.0228, 0.0162),
        (67, 68, 0.0109, 0.0077),
        (70, 72, 0.035, 0.0248),
        (42, 73, 0.0116, 0.0082),
        (73, 74, 0.0015, 0.0032),
        (43, 75, 0.019, 0.0134),
        (44, 76, 0.0276, 0.0196),
        (46, 77, 0.0258, 0.0218),
        (76, 78, 0.0084, 0.0055),
        (78, 79, 0.0208, 0.0051),
        (79, 80, 0.0502, 0.0122),
        (79, 81, 0.0757, 0.0185),
        (81, 82, 0.0017, 0.0004),
        (47, 83, 0.0043, 0.0031),
        (49, 84, 0.0259, 0.0225),
        (50, 85, 0.0074, 0.0018),
        (85, 86, 0.0019, 0.0008),
        (86, 87, 0.001, 0.001), #
        (7, 88, 0.0087, 0.0116),
        (88, 89, 0.0235, 0.0313),
        (89, 90, 0.015, 0.0199),
        (90, 91, 0.0106, 0.0142),
        (91, 92, 0.0158, 0.021),
        (92, 93, 0.014, 0.0187),
        (93, 94, 0.0103, 0.0137),
        (94, 95, 0.0103, 0.0137),
        (89, 96, 0.0344, 0.0243),
        (96, 97, 0.0485, 0.0343),
        (97, 98, 0.0451, 0.0098),
        (97, 99, 0.0017, 0.0004),
        (131, 132, 0.0174, 0.0123),
        (131, 133, 0.046, 0.0335),
        (121, 134, 0.0421, 0.0306),
        (16, 135, 0.0264, 0.0187),
        (16, 136, 0.0151, 0.0107),
        (18, 137, 0.0292, 0.0207),
        (23, 138, 0.0385, 0.028),
        (29, 30, 0.0171, 0.0124),
        (30, 31, 0.0064, 0.0046),
        (31, 32, 0.0174, 0.0123),
        (2, 33, 0.0222, 0.0157),
        (33, 34, 0.001, 0.0005),
        (5, 35, 0.1137, 0.0277),
        (5, 36, 0.0633, 0.0783),
        (6, 37, 0.0028, 0.0037),
        (37, 38, 0.1018, 0.072),
        (38, 39, 0.0469, 0.0332),
        (39, 40, 0.0174, 0.0123),
        (40, 41, 0.0459, 0.0325),
        (41, 42, 0.1159, 0.082),
        (42, 43, 0.0604, 0.0427),
        (43, 44, 0.0222, 0.0157),
        (44, 45, 0.0203, 0.0144),
        (45, 46, 0.008, 0.0064),
        (46, 47, 0.0318, 0.0225),
        (47, 48, 0.0209, 0.0148),
        (48, 49, 0.0366, 0.0255),
        (49, 50, 0.0414, 0.0278),
        (50, 51, 0.0199, 0.0141),
        (51, 52, 0.0113, 0.008),
        (38, 53, 0.0421, 0.0298),
        (42, 54, 0.0081, 0.0057),
        (54, 55, 0.0264, 0.0187),
        (55, 56, 0.0447, 0.0316),
        (56, 57, 0.0434, 0.0307),
        (57, 58, 0.0337, 0.0239),
        (58, 59, 0.0235, 0.0166),
        (55, 60, 0.0167, 0.0118),
        (60, 61, 0.0164, 0.0116),
        (63, 69, 0.0183, 0.013),
        (55, 70, 0.0116, 0.0082),
        (70, 71, 0.006, 0.0015),
        (99, 100, 0.0017, 0.0004),
        (91, 101, 0.0116, 0.0082),
        (101, 102, 0.0289, 0.0205),
        (102, 103, 0.0445, 0.0109),
        (103, 104, 0.0315, 0.0077),
        (104, 105, 0.0585, 0.0143),
        (104, 106, 0.0057, 0.0013),
        (92, 107, 0.0425, 0.0104),
        (94, 108, 0.0306, 0.013),
        (108, 109, 0.0226, 0.0096),
        (94, 110, 0.0017, 0.0004),
        (7, 111, 0.036, 0.0255),
        (10, 112, 0.0535, 0.0131),
        (11, 113, 0.0174, 0.0123),
        (13, 114, 0.0312, 0.0221),
        (114, 115, 0.0334, 0.0237),
        (115, 116, 0.002, 0.0005),
        (14, 117, 0.0253, 0.0183),
        (15, 118, 0.0081, 0.0057),
        (118, 119, 0.0231, 0.0164),
        (119, 120, 0.0212, 0.015),
        (120, 121, 0.0254, 0.018),
        (121, 122, 0.0366, 0.0259),
        (122, 123, 0.0292, 0.0207),
        (123, 124, 0.0305, 0.0216),
        (124, 125, 0.0392, 0.0277),
        (125, 126, 0.0417, 0.0304),
        (126, 127, 0.0174, 0.0123),
        (127, 128, 0.0285, 0.021),
        (128, 129, 0.0293, 0.0213),
        (129, 130, 0.0052, 0.0037),
        (119, 131, 0.0178, 0.0127),
        (25, 139, 0.0475, 0.0337),
        (30, 140, 0.026, 0.0189),
        (31, 141, 0.0292, 0.0207)]
    
    for from_bus, to_bus, r_pu, x_pu in line_data:
        pp.create_line_from_parameters(
            net,
            from_bus=from_bus - 1,  # Subtracting 1 if bus index is 0-based
            to_bus=to_bus - 1,
            length_km=1.0,
            r_ohm_per_km=r_pu*10 ,
            x_ohm_per_km=x_pu*10 ,
            c_nf_per_km=0,
            max_i_ka=1,
            name=f"Line {from_bus}-{to_bus}"
        )
    
    # Create loads
    # 放大所有负荷 1.05 倍
    net.load['p_mw'] *= 1.05
    net.load['q_mvar'] *= 1.05

    pp.create_load(net, bus=bus_map[3], p_mw=0.0014, q_mvar=0.0014, name="Load at Bus 3")
    pp.create_load(net, bus=bus_map[4], p_mw=0.0035, q_mvar=0.0035, name="Load at Bus 4")
    pp.create_load(net, bus=bus_map[5], p_mw=0.0035, q_mvar=0.0035, name="Load at Bus 5")
    pp.create_load(net, bus=bus_map[6], p_mw=0.0014, q_mvar=0.0014, name="Load at Bus 6")
    pp.create_load(net, bus=bus_map[7], p_mw=0.0014, q_mvar=0.0014, name="Load at Bus 7")
    pp.create_load(net, bus=bus_map[8], p_mw=0.0105, q_mvar=0.0106, name="Load at Bus 8")
    pp.create_load(net, bus=bus_map[9], p_mw=0.0014, q_mvar=0.0014, name="Load at Bus 9")
    pp.create_load(net, bus=bus_map[12], p_mw=0.0035, q_mvar=0.0035, name="Load at Bus 12")
    pp.create_load(net, bus=bus_map[13], p_mw=0.0105, q_mvar=0.0106, name="Load at Bus 13")
    pp.create_load(net, bus=bus_map[14], p_mw=0.0035, q_mvar=0.0035, name="Load at Bus 14")
    pp.create_load(net, bus=bus_map[15], p_mw=0.0035, q_mvar=0.0035, name="Load at Bus 15")
    pp.create_load(net, bus=bus_map[16], p_mw=0.0035, q_mvar=0.0035, name="Load at Bus 16")
    pp.create_load(net, bus=bus_map[17], p_mw=0.0210, q_mvar=0.0211, name="Load at Bus 17")
    pp.create_load(net, bus=bus_map[20], p_mw=0.0014, q_mvar=0.0014, name="Load at Bus 20")
    pp.create_load(net, bus=bus_map[21], p_mw=0.0105, q_mvar=0.0106, name="Load at Bus 21")
    pp.create_load(net, bus=bus_map[23], p_mw=0.0105, q_mvar=0.0106, name="Load at Bus 23")
    pp.create_load(net, bus=bus_map[26], p_mw=0.0210, q_mvar=0.0211, name="Load at Bus 26")
    pp.create_load(net, bus=bus_map[27], p_mw=0.0105, q_mvar=0.0106, name="Load at Bus 27")
    pp.create_load(net, bus=bus_map[29], p_mw=0.0105, q_mvar=0.0106, name="Load at Bus 29")
    pp.create_load(net, bus=bus_map[32], p_mw=0.0210, q_mvar=0.0211, name="Load at Bus 32")
    pp.create_load(net, bus=bus_map[34], p_mw=0.0210, q_mvar=0.0211, name="Load at Bus 34")
    pp.create_load(net, bus=bus_map[36], p_mw=0.0014, q_mvar=0.0014, name="Load at Bus 36")
    pp.create_load(net, bus=bus_map[37], p_mw=0.0070, q_mvar=0.0070, name="Load at Bus 37")
    pp.create_load(net, bus=bus_map[39], p_mw=0.0028, q_mvar=0.0028, name="Load at Bus 39")
    pp.create_load(net, bus=bus_map[41], p_mw=0.0105, q_mvar=0.0106, name="Load at Bus 41")
    pp.create_load(net, bus=bus_map[44], p_mw=0.0070, q_mvar=0.0070, name="Load at Bus 44")
    pp.create_load(net, bus=bus_map[45], p_mw=0.0070, q_mvar=0.0070, name="Load at Bus 45")
    pp.create_load(net, bus=bus_map[46], p_mw=0.0070, q_mvar=0.0070, name="Load at Bus 46")
    pp.create_load(net, bus=bus_map[48], p_mw=0.0175, q_mvar=0.0176, name="Load at Bus 48")
    pp.create_load(net, bus=bus_map[49], p_mw=0.0210, q_mvar=0.0211, name="Load at Bus 49")
    pp.create_load(net, bus=bus_map[51], p_mw=0.0175, q_mvar=0.0176, name="Load at Bus 51")
    pp.create_load(net, bus=bus_map[52], p_mw=0.0105, q_mvar=0.0106, name="Load at Bus 52")
    pp.create_load(net, bus=bus_map[53], p_mw=0.0140, q_mvar=0.0070, name="Load at Bus 53")
    pp.create_load(net, bus=bus_map[56], p_mw=0.0035, q_mvar=0.0035, name="Load at Bus 56")
    pp.create_load(net, bus=bus_map[59], p_mw=0.0210, q_mvar=0.0211, name="Load at Bus 59")
    pp.create_load(net, bus=bus_map[62], p_mw=0.0014, q_mvar=0.0014, name="Load at Bus 62")
    pp.create_load(net, bus=bus_map[65], p_mw=0.0210, q_mvar=0.0211, name="Load at Bus 65")
    pp.create_load(net, bus=bus_map[66], p_mw=0.0315, q_mvar=0.0317, name="Load at Bus 66")
    pp.create_load(net, bus=bus_map[67], p_mw=0.0070, q_mvar=0.0070, name="Load at Bus 67")
    pp.create_load(net, bus=bus_map[68], p_mw=0.0140, q_mvar=0.0141, name="Load at Bus 68")
    pp.create_load(net, bus=bus_map[69], p_mw=0.0070, q_mvar=0.0070, name="Load at Bus 69")
    pp.create_load(net, bus=bus_map[71], p_mw=0.0070, q_mvar=0.0070, name="Load at Bus 71")
    pp.create_load(net, bus=bus_map[72], p_mw=0.0210, q_mvar=0.0211, name="Load at Bus 72")
    pp.create_load(net, bus=bus_map[74], p_mw=0.0014, q_mvar=0.0014, name="Load at Bus 74")
    pp.create_load(net, bus=bus_map[75], p_mw=0.0063, q_mvar=0.0063, name="Load at Bus 75")
    pp.create_load(net, bus=bus_map[76], p_mw=0.0105, q_mvar=0.0106, name="Load at Bus 76")
    pp.create_load(net, bus=bus_map[77], p_mw=0.0210, q_mvar=0.0211, name="Load at Bus 77")
    pp.create_load(net, bus=bus_map[80], p_mw=0.0070, q_mvar=0.0070, name="Load at Bus 80")
    pp.create_load(net, bus=bus_map[82], p_mw=0.0210, q_mvar=0.0211, name="Load at Bus 82")
    pp.create_load(net, bus=bus_map[83], p_mw=0.0105, q_mvar=0.0106, name="Load at Bus 83")
    pp.create_load(net, bus=bus_map[84], p_mw=0.0315, q_mvar=0.0317, name="Load at Bus 84")
    pp.create_load(net, bus=bus_map[86], p_mw=0.0014, q_mvar=0.0014, name="Load at Bus 86")
    pp.create_load(net, bus=bus_map[87], p_mw=0.0210, q_mvar=0.0211, name="Load at Bus 87")
    pp.create_load(net, bus=bus_map[88], p_mw=0.0105, q_mvar=0.0106, name="Load at Bus 88")
    pp.create_load(net, bus=bus_map[89], p_mw=0.0091, q_mvar=0.0091, name="Load at Bus 89")
    pp.create_load(net, bus=bus_map[90], p_mw=0.0035, q_mvar=0.0035, name="Load at Bus 90")
    pp.create_load(net, bus=bus_map[91], p_mw=0.0035, q_mvar=0.0035, name="Load at Bus 91")
    pp.create_load(net, bus=bus_map[92], p_mw=0.0035, q_mvar=0.0035, name="Load at Bus 92")
    pp.create_load(net, bus=bus_map[94], p_mw=0.0154, q_mvar=0.0155, name="Load at Bus 94")
    pp.create_load(net, bus=bus_map[96], p_mw=0.0210, q_mvar=0.0211, name="Load at Bus 96")
    pp.create_load(net, bus=bus_map[98], p_mw=0.0070, q_mvar=0.0070, name="Load at Bus 98")
    pp.create_load(net, bus=bus_map[100], p_mw=0.0014, q_mvar=0.0014, name="Load at Bus 100")
    pp.create_load(net, bus=bus_map[101], p_mw=0.0021, q_mvar=0.0021, name="Load at Bus 101")
    pp.create_load(net, bus=bus_map[103], p_mw=0.0175, q_mvar=0.0176, name="Load at Bus 103")
    pp.create_load(net, bus=bus_map[105], p_mw=0.0420, q_mvar=0.0423, name="Load at Bus 105")
    pp.create_load(net, bus=bus_map[106], p_mw=0.0210, q_mvar=0.0211, name="Load at Bus 106")
    pp.create_load(net, bus=bus_map[107], p_mw=0.0014, q_mvar=0.0014, name="Load at Bus 107")
    pp.create_load(net, bus=bus_map[109], p_mw=0.0035, q_mvar=0.0035, name="Load at Bus 109")
    pp.create_load(net, bus=bus_map[110], p_mw=0.0210, q_mvar=0.0211, name="Load at Bus 110")
    pp.create_load(net, bus=bus_map[111], p_mw=0.0035, q_mvar=0.0035, name="Load at Bus 111")
    pp.create_load(net, bus=bus_map[112], p_mw=0.0070, q_mvar=0.0070, name="Load at Bus 112")
    pp.create_load(net, bus=bus_map[113], p_mw=0.0105, q_mvar=0.0106, name="Load at Bus 113")
    pp.create_load(net, bus=bus_map[114], p_mw=0.0105, q_mvar=0.0106, name="Load at Bus 114")
    pp.create_load(net, bus=bus_map[115], p_mw=0.0105, q_mvar=0.0106, name="Load at Bus 115")
    pp.create_load(net, bus=bus_map[116], p_mw=0.0014, q_mvar=0.0014, name="Load at Bus 116")
    pp.create_load(net, bus=bus_map[117], p_mw=0.0091, q_mvar=0.0091, name="Load at Bus 117")
    pp.create_load(net, bus=bus_map[119], p_mw=0.0154, q_mvar=0.0155, name="Load at Bus 119")
    pp.create_load(net, bus=bus_map[120], p_mw=0.0091, q_mvar=0.0091, name="Load at Bus 120")
    pp.create_load(net, bus=bus_map[121], p_mw=0.0091, q_mvar=0.0091, name="Load at Bus 121")
    pp.create_load(net, bus=bus_map[122], p_mw=0.0091, q_mvar=0.0091, name="Load at Bus 122")
    pp.create_load(net, bus=bus_map[123], p_mw=0.0140, q_mvar=0.0141, name="Load at Bus 123")
    pp.create_load(net, bus=bus_map[124], p_mw=0.0175, q_mvar=0.0176, name="Load at Bus 124")
    pp.create_load(net, bus=bus_map[127], p_mw=0.0105, q_mvar=0.0106, name="Load at Bus 127")
    pp.create_load(net, bus=bus_map[128], p_mw=0.0105, q_mvar=0.0106, name="Load at Bus 128")
    pp.create_load(net, bus=bus_map[129], p_mw=0.0154, q_mvar=0.0155, name="Load at Bus 129")
    pp.create_load(net, bus=bus_map[130], p_mw=0.0157, q_mvar=0.0159, name="Load at Bus 130")
    pp.create_load(net, bus=bus_map[132], p_mw=0.0014, q_mvar=0.0014, name="Load at Bus 132")
    pp.create_load(net, bus=bus_map[133], p_mw=0.0063, q_mvar=0.0063, name="Load at Bus 133")
    pp.create_load(net, bus=bus_map[134], p_mw=0.0049, q_mvar=0.0049, name="Load at Bus 134")
    pp.create_load(net, bus=bus_map[135], p_mw=0.0035, q_mvar=0.0035, name="Load at Bus 135")
    pp.create_load(net, bus=bus_map[136], p_mw=0.0105, q_mvar=0.0106, name="Load at Bus 136")
    pp.create_load(net, bus=bus_map[137], p_mw=0.0077, q_mvar=0.0078, name="Load at Bus 137")
    pp.create_load(net, bus=bus_map[138], p_mw=0.0070, q_mvar=0.0070, name="Load at Bus 138")
    pp.create_load(net, bus=bus_map[139], p_mw=0.0014, q_mvar=0.0014, name="Load at Bus 139")
    pp.create_load(net, bus=bus_map[140], p_mw=0.0210, q_mvar=0.0211, name="Load at Bus 140")
    pp.create_load(net, bus=bus_map[141], p_mw=0.0105, q_mvar=0.0106, name="Load at Bus 141")
        
    net.bus["min_vm_pu"] = 0.95
    net.bus["max_vm_pu"] = 1.15

    return net


def DFLieee141(wind_power, sunny_power):
    net = ieee141()
    pi_G = 10
    pi_T = 20
    pi_S = 5

    # 放大所有负荷
    net.load['p_mw'] *= 15
    net.load['q_mvar'] *= 15

    # 将线路阻抗除以2
    net.line['r_ohm_per_km'] /= 2
    net.line['x_ohm_per_km'] /= 2

    # print(f"总有功负荷: {net.load['p_mw'].sum():.2f} MW")
    # print(f"总无功负荷: {net.load['q_mvar'].sum():.2f} Mvar")

    # DG 发电机 - 记录创建的索引
    # DG 发电机 - 随机选择15个节点
    # DG 发电机 - 随机选择15个节点
    dg_buses = [8, 15, 23, 34, 47, 56, 62, 71]
    dg_bus_indices = [bus - 1 for bus in dg_buses]
    dg_sgen_indices = []  # 记录DG在sgen表中的索引
    for i in dg_bus_indices:
        idx = pp.create_sgen(net, bus=i, p_mw=1.0, q_mvar=0.0, name=f"DG at Bus {i+1}",
                            controllable=True, min_p_mw=0.0, max_p_mw=2, min_q_mvar=-0.5, max_q_mvar=0.5)
        dg_sgen_indices.append(idx)

    # 风电
    wind_buses = [8, 28, 30, 68]
    for bus in wind_buses:
        pp.create_sgen(net, bus=bus-1, p_mw=wind_power, q_mvar=0.0, controllable=True, 
                    max_p_mw=wind_power, min_p_mw=0.0, name=f"Wind_{bus}")

    # 太阳能
    solar_buses = [12, 36, 50, 62]
    for i, bus in enumerate(solar_buses):
        pp.create_sgen(net, bus=bus-1, p_mw=sunny_power, q_mvar=0.0, controllable=True, 
                    max_p_mw=sunny_power, min_p_mw=0.0, name=f"Solar_{bus}")

    # 储能
    storage_buses = [10, 25, 40, 58]
    for bus in storage_buses:
        pp.create_storage(net, bus=bus-1, p_mw=0.0, max_e_mwh=1.0, soc_percent=50,
                        q_mvar=0.0, min_e_mwh=0.0, name=f"Storage_{bus}")

    # 删除现有的成本函数
    if len(net.poly_cost) > 0:
        net.poly_cost.drop(net.poly_cost.index, inplace=True)

    # 为外部电网设置购电成本函数
    for idx in net.ext_grid.index:
        pp.create_poly_cost(net, element=idx, et="ext_grid", cp1_eur_per_mw=pi_T)

    # 为DG设置成本函数（使用正确的DG索引）
    for idx in dg_sgen_indices:
        pp.create_poly_cost(net, element=idx, et="sgen", cp1_eur_per_mw=pi_G)
    
    # 为储能设置成本函数
    for idx in net.storage.index:
        pp.create_poly_cost(net, element=idx, et="storage", cp1_eur_per_mw=pi_S)
    
        
    net.bus["min_vm_pu"] = 0.9
    net.bus["max_vm_pu"] = 1.1
    pp.runopp(net)

    # 计算总成本
    ext_grid_cost = sum(net.res_ext_grid['p_mw'] * pi_T)

    # 只计算DG发电机成本（使用正确的索引）
    dg_cost = sum(net.res_sgen.iloc[dg_sgen_indices]['p_mw'] * pi_G)

    storage_cost = sum(abs(net.res_storage['p_mw']) * pi_S)
    total_cost = ext_grid_cost + dg_cost + storage_cost

    # 提取电压
    vm_pu = net.res_bus['vm_pu'].values

    # 提取决策变量
    ext_grid_p = net.res_ext_grid['p_mw'].values
    sgen_p = net.res_sgen['p_mw'].values
    storage_p = net.res_storage['p_mw'].values

    decision_vars = np.concatenate([ext_grid_p, sgen_p, storage_p])
    combined_array = np.concatenate([vm_pu, decision_vars])


    # 计算总发电量
    ext_grid_generation = sum(net.res_ext_grid['p_mw'])  # 外部电网发电量
    dg_generation = sum(net.res_sgen.iloc[dg_sgen_indices]['p_mw'])  # DG发电量
    wind_generation = sum([net.res_sgen.iloc[i]['p_mw'] for i, name in enumerate(net.sgen['name']) if 'Wind' in str(name)])  # 风电发电量
    solar_generation = sum([net.res_sgen.iloc[i]['p_mw'] for i, name in enumerate(net.sgen['name']) if 'Solar' in str(name)])  # 太阳能发电量
    storage_discharge = sum([p for p in net.res_storage['p_mw'] if p > 0])  # 储能放电量

    total_generation = ext_grid_generation + dg_generation + wind_generation + solar_generation + storage_discharge

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
    predicted_p_mw = [
    0.12, 0.15, 0.10, 0.14, 0.16, 0.11, 0.09, 0.10, 0.13, 0.12,
    0.10, 0.11, 0.14, 0.13, 0.17, 0.12, 0.16, 0.15, 0.18, 0.11,
    0.19, 0.13, 0.12, 0.15, 0.14, 0.16, 0.13, 0.11, 0.17, 0.12,
    0.14, 0.18, 0.15, 0.13, 0.19, 0.10]
    cost,vm_pu=DFLieee141(predicted_p_mw)
    print(cost)

    plt.plot(vm_pu)
    plt.show()

