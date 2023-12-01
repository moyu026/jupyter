import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import random
import os

# 创建保存图片的文件夹
if not os.path.exists('random_images'):
    os.makedirs('random_images')

# 设置图片大小
width, height = 180, 100

# DS-DIGIB.TTF 字体路径
font_path = 'DS-DIGIB.TTF'

# 循环生成并保存图片
for i in range(10000):
    # 生成随机的两位小数
    random_number = round(random.uniform(0, 1000), 1)

    # 显示 2 位小数
    text_to_display = "{:.1f}".format(random_number)

    # 创建空白图片
    fig, ax = plt.subplots(figsize=(width / 100, height / 100), dpi=100)
    ax.set_xlim(0, width)
    ax.set_ylim(0, height)
    ax.axis('off')  # 隐藏坐标轴

    # 使用指定字体显示文本
    font_prop = FontProperties(fname=font_path)
    ax.text(width / 2, height / 2, text_to_display, fontproperties=font_prop,
            horizontalalignment='center', verticalalignment='center', fontsize=50)

    # 保存图片
    image_name = f'img/{text_to_display}.png'
    plt.savefig(image_name, bbox_inches='tight', pad_inches=0)
    plt.close()

print("图片已生成并保存到 random_images 文件夹中。")
