# __del__ 析构方法
import random
class Human:
    # 属性
    eye = 2
    skin = 'yellow'

    def eat(self):
        print('eat')

    # 析构方法
    def __del__(self):
        print('del method start')

# 实例化一个对象
one = Human()

# 将对象同时赋值给另外一个变量
two = one

# 主动删除对象
del one # 删除变量，系统回收对象的时候触发__del__方法
print('==========')
# print(one)