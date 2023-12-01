from PIL import Image
import os

img_folder = r'F:\PythonWork\dataset\electrical_cabinet_all\detect\add_small_light\images\val'
save_img_folder = r'F:\PythonWork\dataset\electrical_cabinet_all\detect\add_small_light\scale_img'

img_list = os.listdir(img_folder)

for imgs in img_list:
    img_path = os.path.join(img_folder, imgs)
    save_img_path = os.path.join(save_img_folder, imgs)


    # 打开图像文件
    image = Image.open(img_path)

    # 获取原始图像的宽度和高度
    width, height = image.size

    # 指定新的宽度和高度（原始尺寸的两倍）
    new_width = width * 2
    new_height = height * 2

    # 调整图像大小
    resized_image = image.resize((new_width, new_height))

    # 保存调整大小后的图像
    resized_image.save(save_img_path)
    print(save_img_path)

    # 关闭原始图像
    image.close()
