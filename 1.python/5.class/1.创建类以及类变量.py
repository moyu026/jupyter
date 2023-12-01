class Person(object):  # 类名首字母一般大写, 所有类方法都默认继承object类
    name = 'xiaoming' # 类变量
    # 定义方法
    def say_hello(self):
        print(f'hello {Person.name}')


if __name__ == '__main__':
    # 1.访问类变量
    print(Person.name) # 通过类名加点的方式访问类变量

    # 通过类名加点的方式修改类变量会影响每一个实例化类的使用
    Person.name = '小明'

    # 2.访问类中的方法
    # 实例化类 对象名=类名()
    p = Person()
    p.say_hello()

    # 修改类中的变量, 只影响当前实例化的类的使用
    p.name= 'sansna'
    print('p name', p.name)

    # 可以实例化多个类的对象
    p1 = Person()
    print(p1.name)

    print(p.__dict__)