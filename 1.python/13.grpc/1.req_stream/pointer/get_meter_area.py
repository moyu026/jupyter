import torch
import numpy as np
from yolov5.models.experimental import attempt_load
from yolov5.utils.general import non_max_suppression, scale_coords
from yolov5.utils.augmentations import letterbox
from yolov5.utils.torch_utils import select_device
import cv2
from random import randint
import os
import time


class Detector(object):

    def __init__(self):
        self.img_size = 640
        self.threshold = 0.6
        self.max_frame = 160
        self.init_model()

    def init_model(self):

        self.weights = 'yolov5/best.pt'
        self.device = '0' if torch.cuda.is_available() else 'cpu'
        self.device = select_device(self.device)
        model = attempt_load(self.weights, map_location=self.device)
        model.to(self.device).eval()
        model.half()
        # torch.save(model, 'test.pt')
        self.m = model
        self.names = model.module.names if hasattr(
            model, 'module') else model.names
        self.colors = [
            (randint(0, 255), randint(0, 255), randint(0, 255)) for _ in self.names
        ]

    def preprocess(self, img):

        img0 = img.copy()
        img = letterbox(img, new_shape=self.img_size)[0]  # [1080,1920,3]->[384,640,3]
        img = img[:, :, ::-1].transpose(2, 0, 1)  # img[:, :, ::-1]将图像的颜色通道转换顺序，bgr转换成rgb
        img = np.ascontiguousarray(img)  # ascontiguousarray函数将一个内存不连续存储的数组转换为内存连续存储的数组，使得运行速度更快。
        img = torch.from_numpy(img).to(self.device)
        img = img.half()  # 半精度
        img /= 255.0  # 图像归一化
        if img.ndimension() == 3:
            img = img.unsqueeze(0)

        return img0, img

    def plot_bboxes(self, image, bboxes, line_thickness=None):
        tl = line_thickness or round(
            0.002 * (image.shape[0] + image.shape[1]) / 2) + 1  # line/font thickness
        for (x1, y1, x2, y2, cls_id, conf) in bboxes:
            color = self.colors[self.names.index(cls_id)]
            c1, c2 = (x1, y1), (x2, y2)
            cv2.rectangle(image, c1, c2, color,
                          thickness=tl, lineType=cv2.LINE_AA)
            tf = max(tl - 1, 1)  # font thickness
            t_size = cv2.getTextSize(
                cls_id, 0, fontScale=tl / 3, thickness=tf)[0]
            c2 = c1[0] + t_size[0], c1[1] - t_size[1] - 3
            cv2.rectangle(image, c1, c2, color, -1, cv2.LINE_AA)  # filled
            cv2.putText(image, '{} ID-{:.2f}'.format(cls_id, conf), (c1[0], c1[1] - 2), 0, tl / 3,
                        [225, 255, 255], thickness=tf, lineType=cv2.LINE_AA)
        return image

    def detect(self, im,i):


        im0, img = self.preprocess(im)  # im0:读取的原图像， img:经过处理后的图像[1,3,384,640]

        pred = self.m(img, augment=False)[0]  # pred:[1,15120,7]
        pred = pred.float()
        pred = non_max_suppression(pred, self.threshold, 0.3) # pred:[1,6] [xyxy, conf, cls]

        pred_boxes = []
        image_info = {}
        count = 0

        digital_list,meter_list=[],[]
        for det in pred:
            if det is not None and len(det):  # det[:, :4]:det中第二维度的前四个值，也就是xyxy
                det[:, :4] = scale_coords(         # 缩放后检测的目标的坐标还原到原图上目标的坐标
                    img.shape[2:], det[:, :4], im0.shape).round()

                for *x, conf, cls_id in det:
                    lbl = self.names[int(cls_id)]


                    x1, y1 = int(x[0]), int(x[1])
                    x2, y2 = int(x[2]), int(x[3])

                    region=im0[y1:y2,x1:x2]
                    if lbl =="meter":
                        meter_list.append(region)
                    else:
                        digital_list.append(region)

                    pred_boxes.append(
                        (x1, y1, x2, y2, lbl, conf))
                    count += 1
                    key = '{}-{:02}'.format(lbl, count)
                    image_info[key] = ['{}×{}'.format(
                        x2-x1, y2-y1), np.round(float(conf), 3)]

        im = self.plot_bboxes(im, pred_boxes)
        return im, image_info, digital_list, meter_list


if __name__=="__main__":
    det=Detector()
    path='/home/sy/ocr/datasets/all_meter_image/'
    img_list=os.listdir(path)
    total_time=0
    num=0
    for i in img_list:
        img=cv2.imread(path+i)
        start_time=time.time()
        image,image_info,digital_list, meter_list=det.detect(img,i)
        end_time=time.time()
        total_time += end_time - start_time
        fps = (num + 1) / total_time
        num+=1
        print("fps",fps)

