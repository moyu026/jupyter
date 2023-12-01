import cv2

def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:  # 点击鼠标左键
        bgr_value = img[y, x]
        print(bgr_value)


img_path = 'file/1-1.jpg'
img = cv2.imread(img_path)
img = cv2.resize(img, dsize=(512, 512), interpolation=cv2.INTER_LINEAR)

print(img[2, 3])

cv2.namedWindow('Image')
cv2.setMouseCallback('Image', mouse_callback)

while True:
    cv2.imshow('Image', img)
    key = cv2.waitKey(1) & 0xFF
    if key == 27:  # 按下Esc键退出循环
        break