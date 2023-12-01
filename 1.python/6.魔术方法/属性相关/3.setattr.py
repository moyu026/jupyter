class Human:
    # 添加成员属性
    def __init__(self):
        self.name = 'tom'
        self.age = 16

    # 添加成员方法
    def eat(self):
        print('eat sth')

    # 魔术方法__setattr__， object中本来就有的
    def __setattr__(self, key, value):
        # print('setattr method start')
        # 1.禁止修改年龄， 2.修改名称最多使用三个字符多余的舍弃
        if key == 'age':
            pass
        else:
            object.__setattr__(self, key, value)
# 实例化对象
one = Human()
print(one.__dict__)

# 修改对象成员
one.name = 'joy'
print(one.__dict__)

