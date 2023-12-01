import albumentations as A
import cv2
import os

img_folder = r'F:\PythonWork\0.other\label_test\file\1'
save_img_folder = r'F:\PythonWork\0.other\label_test\file\save'

img_list = os.listdir(img_folder)

for imgs in img_list:
    img_path = os.path.join(img_folder, imgs)
    save_img_path = os.path.join(save_img_folder, imgs)
    image = cv2.imread(img_path)
    height, width, channels = image.shape
    print(img_path)

    # 图像变换
    transform = A.Compose(
        [
            # A.Equalize(mode='cv', by_channels=True, always_apply=False, p=1),
            # A.GaussNoise(var_limit=(0, 50), p=1.0),
            # A.GaussianBlur(blur_limit=(1, 5), sigma_limit=5, p=1.0),
            # A.RandomBrightnessContrast(p=1.0),
            A.Rotate(limit=4, p=1)
        ]
    )
    transformed = transform(image=image)
    cv2.imwrite(save_img_path, transformed['image'])
