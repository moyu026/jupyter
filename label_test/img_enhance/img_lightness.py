import cv2
import os
import numpy as np

img_folder = r'F:\PythonWork\dataset\firedataset\firedataset_640_640\train0_fire_exp_500_enhance_img\100_all'
img_save_folder = r'F:\PythonWork\dataset\firedataset\firedataset_640_640\train0_fire_exp_500_enhance_img\100_enhance\8lightness'

img_list = os.listdir(img_folder)
for imgs in img_list:
    img_path = os.path.join(img_folder, imgs)
    img = cv2.imread(img_path)



    image = np.power(img, 0.89)			# 对像素值指数变换

    cv2.imwrite(img_save_folder + '\\' + imgs[:-4] + '_8.jpg', image)

    print(img_path)
