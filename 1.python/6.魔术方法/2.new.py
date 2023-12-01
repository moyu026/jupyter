# __new__ 构造方法
import random
class Human:
    # 属性
    eye = 2
    skin = 'yellow'

    # 魔术方法__new__ ，重载object类中自带的__new__方法
    def __new__(cls, sex):
        # print('new method start')
        # 控制对象的生成过程
        if sex == 'famale':
            #生成对象并返回
            return object.__new__(cls)
        else:
            #不生成对象
            ...

    def eat(self):
        print('eat')

gender = ['male', 'famale']
sex = random.choice(gender)
#实例化对象
one = Human('famale') # 实例化对象过程：1.制作一个对象(new方法触发) 2.初始化对象(init方法触发)
print(one)