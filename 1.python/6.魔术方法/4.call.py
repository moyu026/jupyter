# 声明一个类
class Human:
    # 成员属性
    name = 'xiaoming'
    age = 18

    # 成员方法
    # 魔术方法
    def __call__(self, ):
        print('call method start')

    def eat(self):
        print('eat')

# 实例化对象
a = Human()
print(a)

a() # 正常情况下，对象不能当作函数调用