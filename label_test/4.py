import re
import os


img_dir = r'F:\PythonWork\1.detection\5.eletrical_cabinet\pointer\number_detect\data\num_ocr\images_point'
save_dir = r'F:\PythonWork\1.detection\5.eletrical_cabinet\pointer\number_detect\data\num_ocr\rename'

indx_char = '_'
for imgs in os.listdir(img_dir):
    img_name = str(os.path.splitext(imgs)[0])
    indx = [substr.start() for substr in re.finditer(indx_char, str(img_name))]

    rename = img_name[indx[2]+1:] + '_' + img_name[:indx[0]] + '.png'
    save_path =os.path.join(save_dir, rename)
    img_path = os.path.join(img_dir, imgs)
    os.rename(img_path, save_path)
    print(save_path)



