# 修改yolo分割标签中的类别数字

import random
import os

def read_lines_to_lists(file_path):
    result_lists = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()  # 去除行末尾的换行符和空白字符
            line_list = line.split()  # 使用空格分隔行内容，并创建一个子列表
            result_lists.append(line_list)
    return result_lists


label_file_folder = r'F:\PythonWork\dataset\firedataset\segment\seg4_640_random\labels\val'
save_label_folder = r'F:\PythonWork\dataset\firedataset\segment\seg4_640_random\labels\val_random'

label_file_list = os.listdir(label_file_folder)

for label_file in label_file_list:
    label_file_path = os.path.join(label_file_folder, label_file)
    save_label_path = os.path.join(save_label_folder, label_file)

    lists = read_lines_to_lists(label_file_path)

    with open(save_label_path, 'w') as f:
        for line_list in lists:
            # print(line_list[1])
            x = []
            y = []
            for i in range(1, len(line_list)):

                if i % 2 == 0:
                    y.append(line_list[i])
                else:
                    x.append(line_list[i])
            points = list(zip(x, y))

            random.shuffle(points)
            label_str = str(points)
            label_str = label_str.replace('[', '')
            label_str = label_str.replace('(', '')
            label_str = label_str.replace(')', '')
            label_str = label_str.replace(']', '')
            label_str = label_str.replace(',', '')
            label_str = label_str.replace("'", '')

            f.write('0' + ' ' + label_str + '\n')
    print(save_label_path)



