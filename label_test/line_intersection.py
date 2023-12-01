def find_intersection(point1_line1, point2_line1, point1_line2, point2_line2):
    # 计算直线1的斜率和截距
    slope_line1 = (point2_line1[1] - point1_line1[1]) / (point2_line1[0] - point1_line1[0])
    intercept_line1 = point1_line1[1] - slope_line1 * point1_line1[0]

    # 计算直线2的斜率和截距
    slope_line2 = (point2_line2[1] - point1_line2[1]) / (point2_line2[0] - point1_line2[0])
    intercept_line2 = point1_line2[1] - slope_line2 * point1_line2[0]

    # 计算交点的x坐标
    x_intersection = (intercept_line2 - intercept_line1) / (slope_line1 - slope_line2)

    # 计算交点的y坐标
    y_intersection = slope_line1 * x_intersection + intercept_line1

    return x_intersection, y_intersection

# 例子
point1_line1 = (-1, 0)
point2_line1 = (0, 1)
point1_line2 = (1, 0)
point2_line2 = (0, 1)

intersection = find_intersection(point1_line1, point2_line1, point1_line2, point2_line2)
print("交点坐标:", intersection)
