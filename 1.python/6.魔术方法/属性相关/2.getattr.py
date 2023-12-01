class Human:
    # 添加成员属性
    def __init__(self):
        self.name = 'tom'
        self.age = 16

    # 添加成员方法
    def eat(self):
        print('eat sth')

    # 魔术方法__getattr__
    def __getattr__(self, item):
        # print('getattr method start')
        # 检测用于访问与name相关的信息都返回名称(name)
        if 'name' in item:
            return self.name


# 实例化对象
one = Human()
# print(one)

# 访问对象成员
print(one.name2)