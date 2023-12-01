# 在图像上画框并显示中文

import cv2
from PIL import Image, ImageDraw, ImageFont
import numpy as np


def draw_img(image, label, left_top, right_bottom, color=(255, 0, 0), txt_color=(255, 255, 255)):
    draw_img = image.copy()

    pillow_image = Image.fromarray(cv2.cvtColor(draw_img, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(pillow_image)
    font = ImageFont.truetype('STZHONGS.TTF', size=30)
    w, h = draw.textsize(label, font)

    draw.rectangle([left_top[0], left_top[1] - h, left_top[0] + w, left_top[1]], outline=color, fill=color)
    draw.rectangle([left_top[0], left_top[1], right_bottom[0], right_bottom[1]], outline=color, width=2)

    draw.text((left_top[0], left_top[1] - h-5), label, fill=txt_color, font=font)

    result_image = cv2.cvtColor(np.array(pillow_image), cv2.COLOR_RGB2BGR)

    return result_image

if __name__ == '__main__':
    img_path = '../file/1-1.jpg'
    label = '左上'
    left_top = (451, 1958)
    right_bottom = (609, 2133)

    image = cv2.imread(img_path)
    image = draw_img(image, label, left_top, right_bottom)

    if isinstance(image, np.ndarray):
        print('is opencv')

    # cv2.imwrite('test1.jpg', image)


# color = (0, 0, 255)
#
# img = cv2.imread(img_path)
# draw_img = img.copy()
#
# cv2.rectangle(draw_img, left_top, right_bottom, color, thickness=2)
#
# w, h = cv2.getTextSize(label, 0, fontScale=1.5, thickness=2)[0]
#
# p1 = (left_top[0], left_top[1] - h-17)
# p2 = (left_top[0] + w, left_top[1])
#
# cv2.rectangle(draw_img, p1, p2, color, -1, cv2.LINE_AA)
#
# cv2.putText(draw_img, label, (left_top[0], left_top[1]-15), 0, 1.5, (255, 255, 255), thickness=2, lineType=cv2.LINE_AA)
#
# cv2.imwrite('test.jpg', draw_img)