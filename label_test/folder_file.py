# 遍历子文件夹中的文件

import os
import shutil

# 指定要遍历的根文件夹路径
root_folder = r"F:\PythonWork\dataset\electrical_cabinet_all\detect\add_small_light"

img_folder = r'F:\PythonWork\dataset\electrical_cabinet_all\detect\11\images'
label_folder = r'F:\PythonWork\dataset\electrical_cabinet_all\detect\11\labels'

# 使用os.walk遍历文件夹及其子文件夹
for root, dirs, files in os.walk(root_folder):
    for file in files:
        file_path = os.path.join(root, file)
        if file_path.split('.')[-1] == 'png':
            shutil.copy(file_path, img_folder)
            print(file_path)

        # if file_path.split('.')[-1] == 'txt':
        #     shutil.copy(file_path, label_folder)
        #     print(file_path)

