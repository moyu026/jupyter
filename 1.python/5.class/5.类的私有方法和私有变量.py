class Animal:
    def __init__(self, name, legs):
        self.name = name
        self.legs = legs
        self.__age = 10  # 在变量名前加__表示为私有变量，只能在自己的类中使用，不能在子类和实例化对象中被访问

    def info(self):
        print(f'name:{self.name}, legs:{self.legs}，{self.__age}')
        self.__private_info() # 在类内访问私有方法

    def __private_info(self):  # 在方法名前加__表示为私有方法，只能在自己的类中使用，不能在子类和实例化对象中被访问
        print(f'this is private_info')

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

    c = Cat('ASS', 99)
    c.info()
