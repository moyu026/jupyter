# 删除txt文件中的某一行

import os

folder_path = r'F:\PythonWork\dataset\electrical_cabinet_all\detect\new_light\label\val' # 1280

file_list = os.listdir(folder_path)
dict1 = {}
for file in file_list:
    file_path = os.path.join(folder_path, file)
    fw = open(r"F:\PythonWork\dataset\electrical_cabinet_all\detect\new_light\label\val1" + "\\" + file, 'w')  # 1280
    fileHandler = open(file_path, "r")
    listOfLines = fileHandler.readlines()

    # Iterate over the lines
    for line in listOfLines:
        print(line.strip())
        if line[0] == '0' or line[0] == '1':
            fw.write(line)
        # elif line[0] == '2':
        #     fw.write('1' + line[1:])
