# 根据yolo标签把图片中的目标裁剪出来并保存

import os
import cv2 as cv

img_folder = r'F:\PythonWork\dataset\obj\CT-val\220kv_crop\img'
label_folder = r'F:\PythonWork\dataset\obj\CT-val\220kv_crop\labels'
save_folder = r'F:\PythonWork\dataset\obj\CT-val\220kv_crop\save_img'

img_list = os.listdir(img_folder)

for imgs in img_list:
    img_path = os.path.join(img_folder, imgs)
    label_file = os.path.splitext(imgs)[0] + '.txt'
    label_path = os.path.join(label_folder, label_file)
    # print(img_path)

    img = cv.imread(img_path)
    img_height, img_width, _ = img.shape

    # print(img_width, img_height)

    if os.path.exists(label_path):
        with open(label_path) as f:
            lines = f.readlines()

            num = 0
            for line in lines: # 框的中心坐标和框的宽高
                class_id, x_center, y_center, width, height, _ = map(float, line.split())

                # 框的左上和右下点坐标
                left = int((x_center - width/2) * img_width)
                top = int((y_center - height/2) * img_height)
                right = int((x_center + width/2) * img_width)
                bottom = int((y_center + height/2) * img_height)

                # print(left,top,right,bottom)

                crop_img = img[top:bottom, left:right]

                crop_img_name = f"{os.path.splitext(imgs)[0]}_class_{num}.jpg"
                crop_img_path = os.path.join(save_folder, crop_img_name)

                # cv.imshow('img', crop_img)
                # cv.waitKey(0)

                cv.imwrite(crop_img_path, crop_img)

                num = num + 1



