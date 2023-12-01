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

    # 魔术方法__str__,是object类中自带的
    def __str__(self): # 重载object中的__str__方法，必须返回一个字符串类型
        print('str method start')
        return self.color



# 实例化对象
one = Human()

# 打印对象时触发__str__方法
# print(one)

# 第二个触发__str__的方法
str(one)  # 类型转换