import os
import shutil


def traverse_folders(folder_path, save_folder):
    # 获取当前文件夹下的所有文件和文件夹
    contents = os.listdir(folder_path)

    for item in contents:
        item_path = os.path.join(folder_path, item)

        if os.path.isfile(item_path):
            # 处理文件
            print("文件:", item_path)
            shutil.copy(item_path, save_folder)
        elif os.path.isdir(item_path):
            # 处理文件夹，并递归遍历子文件夹
            # print("文件夹:", item_path)
            traverse_folders(item_path, save_folder)


# 调用遍历文件夹函数
folder_to_traverse = r'F:\PythonWork\1.detection\5.eletrical_cabinet\pointer\number_detect\data\0.9'  # 替换为要遍历的文件夹路径
save_folder = r'F:\PythonWork\1.detection\5.eletrical_cabinet\pointer\number_detect\data\num_ocr\images_point'
traverse_folders(folder_to_traverse, save_folder)
