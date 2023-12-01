import numpy as np
import cv2

# 创建一个黑色背景
image = np.zeros((400, 400, 3), dtype=np.uint8)

# 定义三角形的三个顶点坐标
pts = np.array([[132, 316], [165, 316], [165, 352], [132, 352]], np.int32)

# 将三角形的顶点坐标转换为合适的维度
pts = pts.reshape((-1, 1, 2))

# 画出多边形
cv2.polylines(image, [pts], isClosed=True, color=(255, 255, 255), thickness=2)

# 显示绘制的图像
cv2.imshow('Polygon', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
