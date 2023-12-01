# 创建一个类
class Human:
    # 成员属性
    color = 'yellow'
    age = 18

    # 成员方法
    def eat(self):
        print('eat')

    def say(self):
        print('aaaa')

    # 魔术方法__bool__
    def __bool__(self):
        print('bool method start')
        # 判断 根据某些数据返回不同的bool值，实现bool转换的作用
        if self.color == 'yellow':
            return True
        else:
            return False

# 实例化对象
one = Human()
print(one)

# 转换对象
result = bool(one) # 一般情况下，对象转换的结果默认就是True
print(result)