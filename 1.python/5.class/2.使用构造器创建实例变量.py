class Person:
    def __init__(self, name):  # 类似于函数中的传参
        self.username = name  # self.username:实例变量，通过self.的方法引用
        self.age = 10
        self.email = f'{name}@xx.com'

    def say_hello(self):
        print(f'hello {self.username}, age:{self.age}, email:{self.email}')

if __name__ == '__main__':
   p1 = Person('小明')
   p1.say_hello()

   p2 = Person('xianzhang')
   p2.say_hello()