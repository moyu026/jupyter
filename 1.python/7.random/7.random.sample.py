# 从指定序列中随机获取指定长度的片断。sample函数不会修改原有序列。
import random

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
slice = random.sample(list, 5)  #从list中随机获取5个元素，作为一个片断返回
print(slice)
print(list) #原有序列不会改变。