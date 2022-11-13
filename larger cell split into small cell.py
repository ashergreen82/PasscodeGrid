import numpy as np

my_dict = {'A1': 'HCZ', 'B1': 'DAL', 'C1': 'CSF', 'D1': 'NHU', 'E1': 'HZE', 'A2': 'XFK', 'B2': 'WCC', 'C2': 'KKU', 'D2': 'GQF', 'E2': 'XBS', 'A3': 'GFU', 'B3': 'OTJ', 'C3': 'XHN', 'D3': 'ZXS', 'E3': 'JZM', 'A4': 'RVK', 'B4': 'NNM', 'C4': 'NKV', 'D4': 'XFP', 'E4': 'AIM', 'A5': 'RUK', 'B5': 'HPE', 'C5': 'PQA', 'D5': 'HVB', 'E5': 'VPF'}


def create_matrix(matrix):
    transition_list = list(my_dict.values())
    cell_text = [transition_list[x:x+5] for x in range(0, len(transition_list),5)]
    # cell_text = np.array_split(transition_list, 5)
    print(transition_list)
    print(cell_text)

create_matrix(my_dict)