# 声明一个类
class MakeCake:
    def makecake(self):
        print('制作')

    def eat(self):
        print('吃')

    # 将上面所有的方法放到一个方法里，在实例化的时候就不需要一个一个调用上面的方法，
    # 只需要调用该方法即可
    # def func_all(self):  # 结合步骤的操作
    #     self.makecake()
    #     self.eat()

    # 魔术方法__call__等同于上面的func_all方法
    def __call__(self, flavor):
        self.makecake()
        self.eat()
        print(flavor)

dg = MakeCake()

# 一个一个调用类中的方法
# dg.makecake()
# dg.eat()

# 调用一个综合的方法
# dg.func_all()

# 使用魔术方法__call__
dg('milk')