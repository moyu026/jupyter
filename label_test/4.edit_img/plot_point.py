import matplotlib.pyplot as plt

# 定义四个点的坐标
points = [(86, 170), (120, 173), (117, 200), (85, 198)]
# 提取x坐标和y坐标
x_coords, y_coords = zip(*points)
# 创建一个新的图形
plt.figure()
plt.gca().invert_yaxis()  # 反转y轴，让y轴向下
# 绘制四个点
plt.plot(x_coords, y_coords, 'ro')  # 'ro' 表示红色圆点
# 在每个点旁边显示坐标
for (x, y) in points:
    plt.text(x, y, f'({x}, {y})')
# 设置坐标轴标签
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.xlabel('X坐标')
plt.ylabel('Y坐标')

# 显示图形
plt.grid(True)
plt.show()
