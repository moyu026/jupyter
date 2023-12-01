import albumentations as A
import cv2
import os

image_folder = r'C:\Users\liu\Desktop\crop_mianban\images\val'
label_folder = r'C:\Users\liu\Desktop\crop_mianban\labels\val'
save_image_path = r'C:\Users\liu\Desktop\crop_mianban\isr_images\val'
save_label_folder = r'C:\Users\liu\Desktop\crop_mianban\isr_labels\val'

img_list = os.listdir(image_folder)

for imgs in img_list:
    img_path = os.path.join(image_folder, imgs)
    label_path = label_folder + '\\' + str(imgs[:-3]) + 'txt'
    new_label_path = save_label_folder + '\\' + str(imgs[:-3]) + 'txt'
    new_img_path = os.path.join(save_image_path, imgs)
    bboxes = []
    image = cv2.imread(img_path)
    height, width, channels = image.shape

    # 读取标签文件
    with open(label_path, 'r') as f:
        for label in f:
            parts = label.strip().split()
            parts = parts[1:] + [parts[0]]
            parts = [float(item) for item in parts]
            # print(parts)
            bboxes.append(parts)

    # 图像变换
    transform = A.Compose(
        [
            # A.Flip(p=0.8),
            A.Resize(width=width*2, height=height*2),
            # A.ShiftScaleRotate(shift_limit=0.0625, scale_limit=0.1, rotate_limit=10, interpolation=1, border_mode=0, value=None, mask_value=None, always_apply=False, p=0.6),
            # A.RandomRain (slant_lower=-10, slant_upper=10, drop_length=20, drop_width=1, drop_color=(200, 200, 200), blur_value=3, brightness_coefficient=0.8, rain_type=None,always_apply=False, p=0.6),
            # A.RandomSnow (snow_point_lower=0.1, snow_point_upper=0.3, brightness_coeff=2.5, always_apply=False, p=1)
            # A.RandomFog (fog_coef_lower=0.3, fog_coef_upper=1, alpha_coef=0.08, always_apply=False, p=0.5)
        ],
        bbox_params=A.BboxParams(format='yolo'))
    transformed = transform(image=image, bboxes=bboxes)

    # 写入变换后的标签
    with open(new_label_path, 'w') as f_out:
        for new_label in transformed['bboxes']:
            new_label = list(new_label)
            new_label = [int(new_label[-1])] + new_label[:-1]
            print(new_label)
            f_out.write((str(list(new_label))[1:-1].replace(",", "")) + '\n')

    # 保存变换后的图片
    cv2.imwrite(new_img_path, transformed['image'])
