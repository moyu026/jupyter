import cv2
import os
import PIL
import shutil

img_folder = r'F:\PythonWork\dataset\firedataset\1\move'
save_folder = r'F:\PythonWork\dataset\firedataset\1\rgb_white'
move_path = r'F:\PythonWork\dataset\firedataset\1\move'
img_list = os.listdir(img_folder)

num = 0
for imgs in img_list:
    img_path = os.path.join(img_folder, imgs)
    img = PIL.Image.open(img_path)
    save_path = os.path.join(save_folder, imgs)

    print(save_path)

    img.load()
    background = PIL.Image.new("RGB", img.size, (255, 255, 255))
    background.paste(img, mask=img.split()[3])
    background.save(save_path, quality=100)

    # shutil.move(img_path, move_path)





