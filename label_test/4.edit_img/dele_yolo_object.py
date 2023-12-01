# 根据yolo标枪删除图片中的目标

import os
import cv2
import numpy as np

def mask_unannotated_regions(image_folder, label_folder, output_folder):
    image_files = os.listdir(image_folder)

    for image_file in image_files:
        if image_file.endswith('.jpg') or image_file.endswith('.JPG') or image_file.endswith('.png'):
            # 构建图片和标签的完整路径
            image_path = os.path.join(image_folder, image_file)
            label_file = os.path.splitext(image_file)[0] + '.txt'
            label_path = os.path.join(label_folder, label_file)

            # 读取图像
            image = cv2.imread(image_path)

            # 获取图像尺寸
            img_height, img_width, _ = image.shape

            # 创建一个白色掩码图像
            mask = np.zeros(image.shape[:2], dtype=np.uint8)

            if os.path.exists(label_path):
                # 读取YOLO标签
                with open(label_path, 'r') as f:
                    lines = f.readlines()

                for line in lines:
                    # 解析标签行，格式为：'class_id x_center y_center width height\n'
                    class_id, x_center, y_center, width, height = map(float, line.split())

                    # 计算目标区域的边界框坐标（以像素为单位）
                    left = int((x_center - width / 2) * img_width)
                    top = int((y_center - height / 2) * img_height)
                    right = int((x_center + width / 2) * img_width)
                    bottom = int((y_center + height / 2) * img_height)

                    # polygon_points = [(left, top), (right, top), (right, bottom), (left, bottom)]
                    # points = np.array([polygon_points], dtype=np.int32)
                    #
                    # cv2.fillPoly(mask, points, 255)
                    #
                    # result = np.copy(image)
                    # result[mask == 0] = 255

                    image[top:bottom, left:right] = (0, 0, 0)


                    # 保存结果图像
                    output_path = os.path.join(output_folder, image_file)
                    cv2.imwrite(output_path, image)

# 用法示例
image_folder = r'F:\PythonWork\dataset\obj\220kv_v5_add_bg\images\val'
label_folder = r'F:\PythonWork\dataset\obj\220kv_v5_add_bg\labels\val'
output_folder = r'F:\PythonWork\dataset\obj\220kv_v5_add_bg\crop\images\val'
mask_unannotated_regions(image_folder, label_folder, output_folder)
