import cv2
import os

# 读取图片
img_folder = r'F:\PythonWork\dataset\electrical_cabinet_all\classify\button_rotate\val\top'
save_img_folder = r'F:\PythonWork\dataset\electrical_cabinet_all\classify\button_rotate\train\top_rotate'

img_list = os.listdir(img_folder)

for img in img_list:
    img_path = os.path.join(img_folder, img)
    save_img_path = os.path.join(save_img_folder, img)

    image = cv2.imread(img_path)

    # 旋转图片
    rotated_image = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)

    # 保存旋转后的图片
    cv2.imwrite(save_img_path, rotated_image)

    print(save_img_path)

