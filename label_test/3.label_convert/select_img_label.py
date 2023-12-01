import os
import shutil
'''已知val_img的图片，将label中的val_label挑选出来'''

train_img_folder = r'F:\PythonWork\dataset\electrical_cabinet_all\detect\7.pointer\seg\images\train'
val_img_folder = r'F:\PythonWork\dataset\electrical_cabinet_all\detect\7.pointer\seg\images\val'

# 总的图片或者标签的路径
label_folder = r'F:\PythonWork\dataset\electrical_cabinet_all\detect\7.pointer\seg\labels'

# 保存文件夹的路径
train_label_folder = r'F:\PythonWork\dataset\electrical_cabinet_all\detect\7.pointer\seg\train'
val_label_folder = r'F:\PythonWork\dataset\electrical_cabinet_all\detect\7.pointer\seg\val'

val_img_list = os.listdir(val_img_folder)
for val_img in val_img_list:
    val_label_path = label_folder + '\\' + str(val_img[:-3]) + 'txt'
    shutil.copy(val_label_path, val_label_folder)
    print(val_label_path)


train_img_list = os.listdir(train_img_folder)
for train_img in train_img_list:
    train_label_path = label_folder + '\\' + str(train_img[:-3]) + 'txt'
    shutil.copy(train_label_path, train_label_folder)
    print(train_label_path)



