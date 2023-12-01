import cv2
import os
'''
图像翻转
# 0以X轴对称翻转，>0以Y轴对称翻转，<0以X轴Y轴同时翻转
image1 = cv2.flip(scr, 0)
image2 = cv2.flip(scr, 1)
image3 = cv2.flip(scr, -1)
'''

img_folder = r'F:\PythonWork\dataset\electrical_cabinet_all\classify\button_flip\val\left_top'
img_save_folder = r'F:\PythonWork\dataset\electrical_cabinet_all\classify\button_flip\val\left_flip'

img_list = os.listdir(img_folder)

for imgs in img_list:
    img_path = os.path.join(img_folder, imgs)

    img = cv2.imread(img_path)
    image = cv2.flip(img, 1)

    cv2.imwrite(img_save_folder + '\\' + imgs, image)
    print(img_path)






