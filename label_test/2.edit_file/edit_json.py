# 编辑json文件内容

import os
import json

json_folder = r'F:\PythonWork\dataset\obj\facilities_seg\labels\train_seg'
save_folder = r'F:\PythonWork\dataset\obj\facilities_seg\labels\train_seg_1'

json_list = os.listdir(json_folder)

for jsons in json_list:
    json_path = os.path.join(json_folder, jsons)
    save_path = os.path.join(save_folder, jsons)

    with open(json_path, 'r') as load_f:
        json_dict = json.load(load_f)
        for shape_dict in json_dict['shapes']:
            label = shape_dict['label']
            if label[-2] != '_':
                shape_dict['label'] = label[:-1] + '_' + label[-1]
    with open(save_path, 'w') as file:
        json.dump(json_dict, file, indent=2)
