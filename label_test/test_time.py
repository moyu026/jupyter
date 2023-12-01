from paddleocr import PaddleOCR, draw_ocr
import time
import os

# Paddleocr目前支持的多语言语种可以通过修改lang参数进行切换
# 例如`ch`, `en`, `fr`, `german`, `korean`, `japan`
time_start_model =time.time()
ocr = PaddleOCR(use_angle_cls=True, lang="ch")  # need to run only once to download and load model into memory
time_end_model = time.time()
time_model = time_end_model - time_start_model

time_detect_start = time.time()
img_folder = r'/home/nvidia/pythonwork/paddle/ppocr_img/test_img'
img_list = os.listdir(img_folder)
for img in img_list:
    img_path = os.path.join(img_folder,img)

    result = ocr.ocr(img_path, cls=True)
    time_detect_end = time.time()
    for idx in range(len(result)):
        res = result[idx]
        for line in res:
            print(line)

time_detect = time_detect_end - time_detect_start

print('time_model:',time_model)
print('time_detect:',time_detect)

