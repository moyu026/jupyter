import cv2

img_path = r'../file/662.jpg'
image = cv2.imread(img_path)
image = cv2.resize(image, (512, 512))

circle_centers = [(101, 315), (96, 269), (161, 262), (166, 307)]
radius = 10

# 在图像上绘制四个圆
for center in circle_centers:
    cv2.circle(image, center, radius, (0, 0, 255), -1)  # 参数：图像、圆心坐标、半径、颜色、厚度（-1表示填充）

# 显示绘制好圆的图像
cv2.imshow("Four Circles", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
