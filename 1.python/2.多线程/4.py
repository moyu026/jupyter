from threading import Thread
import cv2
from paddleocr import PaddleOCR

frame = None
ocr = PaddleOCR(use_angle_cls=True, lang="ch")

def read_video(filename):
    global frame
    cap = cv2.VideoCapture(filename)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

def detect_video():
    global frame
    while True:
        if frame is not None:
            result = ocr.ocr(frame)
            print(result)

if __name__ == "__main__":
    video_path = r'F:\PythonWork\dataset\electrical_cabinet_all\detect\electrical_cabinet_test/button1.mp4'

    t1 = Thread(target=read_video, args=(video_path,))
    t2 = Thread(target=detect_video)

    t1.start()
    t2.start()

    t1.join()
    t2.join()
