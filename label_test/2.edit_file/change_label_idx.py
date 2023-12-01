# 修改yolo标签中的标签数字

import os

def change_idx(input_file, output_file):
    with open(input_file, 'r') as input_f, open(output_file, 'w') as output_f:
        for label in input_f:
            parts = label.strip().split()
            class_id = int(parts[0])
            if class_id == 0:
                class_id = 1
            else:
                class_id = 0

            parts[0] = str(class_id)
            new_label = " ".join(parts)
            output_f.write(new_label + "\n")


label_folder = r'F:\PythonWork\dataset\electrical_cabinet_all\detect\light\labels\val'
new_label_folder = r'F:\PythonWork\dataset\electrical_cabinet_all\detect\traffic_light\traffic_light\val'

label_list = os.listdir(label_folder)

for label_file in label_list:
    label_file_path = os.path.join(label_folder, label_file)
    new_label_path = os.path.join(new_label_folder, label_file)
    change_idx(label_file_path, new_label_path)







