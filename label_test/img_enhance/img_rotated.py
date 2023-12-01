import cv2
import os


img_folder = r'F:\PythonWork\dataset\electrical_cabinet_all\classify\button_rotate\train\top'
img_save_folder = r'F:\PythonWork\dataset\electrical_cabinet_all\classify\button_rotate\train\top_rotate1'

img_list = os.listdir(img_folder)

for imgs in img_list:
    img_path = os.path.join(img_folder, imgs)

    img = cv2.imread(img_path)
    height, width, channel = img.shape

    # 旋转参数：旋转中心，旋转角度，scale
    M = cv2.getRotationMatrix2D((width / 2, height / 2), 90, 1)
    # 参数：原始图像，旋转参数，元素图像宽高
    rotated = cv2.warpAffine(img, M, (width*2, height*2))

    cv2.imwrite(img_save_folder + '\\' + imgs, rotated)
    print(img_path)







