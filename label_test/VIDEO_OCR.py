from paddleocr import PaddleOCR, draw_ocr

ocr = PaddleOCR(use_angle_cls=True, lang="ch")  # need to run only once to download and load model into memory
img_path = './imgs/11.jpg'
result = ocr.ocr(img_path, cls=True)
for idx in range(len(result)):
    res = result[idx]
    for line in res:
        print(line)



# 打开视频文件
video_path = 'video/1.mp4'
cap = cv2.VideoCapture(video_path)

while cap.isOpened():
    # 读取一帧
    ret, frame = cap.read()

    if not ret:
        break

    # 在图像上检测文本
    results = reader.readtext(frame)

    print(results)

#     # 处理检测结果
#     for (bbox, text, prob) in results:
#         # 在图像上绘制边界框和文本
#         pts = bbox.astype(int).reshape((-1, 1, 2))
#         cv2.polylines(frame, [pts], isClosed=True, color=(0, 255, 0), thickness=2)
#         cv2.putText(frame, text, (pts[0][0][0], pts[0][0][1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
#
#     # 显示结果
#     cv2.imshow('Video OCR', frame)
#
#     # 按'q'键退出
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# # 清理
# cap.release()
# cv2.destroyAllWindows()
