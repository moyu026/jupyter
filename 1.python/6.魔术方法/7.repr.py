# 创建一个类
class Human:
    # 成员属性
    color = 'yellow'
    age = 18

    def __init__(self):
        self.test1 = 'test1'
        self.test2 = 'test2'

    # 成员方法
    def eat(self):
        print('eat')

    def say(self):
        print('aaaa')

    # 魔术方法__repr__， 一般情况下，重载repr的方法相当于重载str的方法
    def __repr__(self):
        print('repr method start')
        return str(self.__dict__)

    # 所有类默认都有存在一个等式
    # __str__ = __repr__  # 将repr的方法赋值给str方法， 完全一样

# 实例化对象
one = Human()
print(one)