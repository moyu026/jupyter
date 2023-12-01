# 声明一个类
class Car:
    # 成员属性
    color = 'red'
    weight = '2t'
    circle = ['qian', 'hou', 'zuo', 'you']

    # 成员方法
    def playmusic(self):
        print('music')

    def move(self):
        print('gogo')

    # 魔术方法__len__, 必须有一个整数的返回值
    def __len__(self):
        circle_num = len(self.circle)
        # print('len method start')
        return circle_num

# 实例化一个对象
mycar = Car()

r = len(mycar)
print(r)