class Animal:
    def __init__(self, name, legs):
        self.name = name
        self.legs = legs

    def info(self):
        print(f'name:{self.name}, legs:{self.legs}')

class Dog(Animal):
    # 通过定义相同的名字重写父类中的方法
    def info(self, other):
        print(f'name:{self.name}, legs:{self.legs}, {other}')

class Cat(Animal):
    def walk(self):
        print(f'{self.name} walks {self.legs}')

if __name__ == '__main__':
    d = Dog('a', 4) # 实例化子类的时候要传与父类中对应的参数
    d.info('wwww')    # 调用子类中重写的方法时要传与子类中方法对应的参数

    c = Cat('B', 9)
    c.info()
    c.walk()