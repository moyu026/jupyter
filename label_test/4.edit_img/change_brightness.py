import cv2
import numpy as np

# 读取图像
image = cv2.imread(r'F:\jupyter\opencv\image_file\demo_img\1.jpg')

# 调整亮度
brightness_factor = 50  # 可以根据需要进行调整

# 增加或减少亮度（加法或减法操作）
brightened_image = np.where((255 - image) < brightness_factor, 255, image + brightness_factor)
darkened_image = np.where(image < brightness_factor, 0, image - brightness_factor)

cv2.imwrite(r'F:\jupyter\opencv\image_file\demo_img\rgba.jpg', darkened_image)
