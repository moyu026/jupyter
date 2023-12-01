class Human:
    # 添加成员属性
    def __init__(self):
        self.name = 'tom'
        self.age = 16

    # 添加魔术方法__getattribute__
    def __getattribute__(self, item): # item接收的是访问成员的名称字符串
        # print('getattribute method start')
        # 一定不能使用当前对象的成员访问，会再次触发当前魔术方法进入递归循环
        result = object.__getattribute__(self, item)
        newname = result[0] + '*' + result[-1]
        return newname

    # 添加成员方法
    def eat(self):
        print('eat sth')

# 实例化对象
one = Human()
# print(one)

print(one.name)