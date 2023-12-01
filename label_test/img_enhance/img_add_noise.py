import cv2
import numpy as np
from skimage import util
import os

img_folder = r'F:\PythonWork\dataset\firedataset\firedataset_640_640\train0_fire_exp_500_enhance_img\100_enhance\flip'
img_save_folder = r'F:\PythonWork\dataset\firedataset\firedataset_640_640\train0_fire_exp_500_enhance_img\100_enhance\7flip_noise'

img_list = os.listdir(img_folder)

for imgs in img_list:
    img_path = os.path.join(img_folder, imgs)

    img = cv2.imread(img_path)
    noise_gs_img = util.random_noise(img, mode='gaussian')
    noise_gs_img = noise_gs_img * 255

    cv2.imwrite(img_save_folder + '\\' + imgs[:-4] + '_1.jpg', noise_gs_img)
    print(img_path)





