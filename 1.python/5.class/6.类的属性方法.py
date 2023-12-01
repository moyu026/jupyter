class Person:
    def __init__(self,name):
        self.__name = name

    @property
    def name(self):  # 由于私有变量不能在类外被访问，可以通过类内的方法访问，传递出去
        return self.__name

    @name.setter  # 修改属性变量的参数， name与上面@property中的方法名一致
    def name(self,value):
        self.__name = value

if __name__ == '__main__':
    p1 = Person('xxx')
    # print(p1.name())
    print(p1.name) #类中的方法添加@property后，可以像访问属性一样访问该方法，不用在方法名后加()
    p1.name = 'xiaoming'
    print(p1.name)