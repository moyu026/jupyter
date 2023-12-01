## yolo标签中的坐标转为图像上实际的坐标

import cv2


def yolo_to_image_coordinates(yolo_coordinates, image_shape):
    x, y, w, h = yolo_coordinates
    image_height, image_width = image_shape
    # 计算中心点的实际坐标
    center_x = int(x * image_width)
    center_y = int(y * image_height)

    # 计算宽度和高度的实际值
    width = int(w * image_width)
    height = int(h * image_height)

    # 计算边界框的左上角和右下角坐标
    x1 = center_x - (width // 2)
    y1 = center_y - (height // 2)
    x2 = center_x + (width // 2)
    y2 = center_y + (height // 2)

    return x1, y1, x2, y2


img_path = 'file/yolo_bbox/1-1_0.jpg'
label_path = 'file/yolo_bbox/1-1_0.txt'

img = cv2.imread(img_path)
image_shape = img.shape[0:2]
draw_img = img.copy()

with open(label_path, 'r') as f:
    for label in f:
        parts = label.strip().split()
        # x, y, w, h = parts[1], parts[2], parts[3], parts[4]
        yolo_coordinates = (float(parts[1]), float(parts[2]), float(parts[3]), float(parts[4]))

        # print(yolo_coordinates)

        x1, y1, x2, y2 = yolo_to_image_coordinates(yolo_coordinates, image_shape)
        cv2.rectangle(draw_img, (x2, y2), (x1, y1), (255, 0, 0), thickness=2)

        print("左上角坐标 (x1, y1):", x1, y1)
        print("右下角坐标 (x2, y2):", x2, y2)

cv2.imshow('d', draw_img)
cv2.waitKey()
