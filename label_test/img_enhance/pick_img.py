import os
import numpy as np
import shutil

img_folder = r'F:\PythonWork\dataset\obj\CT2\images\train'
save_img_folder = r'F:\PythonWork\dataset\obj\CT2\images\val'

img_list = os.listdir(img_folder)

split_img = [img_list[x:x+20] for x in range(0, len(img_list), 20)]


for i in range(len(split_img)):
    x = np.random.choice(split_img[i], size=4, replace=False)
    for img in x:
        img_path = os.path.join(img_folder, img)
        shutil.move(img_path, save_img_folder)
        print(img_path)
