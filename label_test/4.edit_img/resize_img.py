import cv2
import os

img_folder = r'F:\PythonWork\dataset\firedataset\fire_bg\rgb_black'
save_folder = r'F:\PythonWork\dataset\firedataset\fire_bg\fire_640'
img_list = os.listdir(img_folder)

for imgs in img_list:
    img_path = os.path.join(img_folder, imgs)
    save_img_path = os.path.join(save_folder, imgs)
    img = cv2.imread(img_path)

    img_resize = cv2.resize(img, (640, 640))

    cv2.imwrite(save_img_path, img_resize)

    print(save_img_path)
