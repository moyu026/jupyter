# 修改json文件内容

import os
import json

json_folder = r'F:\PythonWork\dataset\obj\seg\0.facilities_seg_label\val_seg'   # json_label文件夹
save_folder = r'F:\PythonWork\dataset\obj\seg\0.facilities_seg_label\val'   # 保存文件夹

json_list = os.listdir(json_folder)

for jsons in json_list:
    json_path = os.path.join(json_folder, jsons)
    save_path = os.path.join(save_folder, jsons)

    with open(json_path, 'r') as load_f:
        json_dict = json.load(load_f)
        json_dict['imagePath'] =r'F:\PythonWork\dataset\obj\facilities_seg\images\val' + '\\' + json_dict['imagePath'].split('\\')[-1]
        # print(json_dict['imagePath'])


    with open(save_path, 'w') as file:
        json.dump(json_dict, file, indent=2)
