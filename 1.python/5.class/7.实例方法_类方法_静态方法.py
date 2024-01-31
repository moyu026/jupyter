class Dog:
    dogbook = {'黄色':30, '黑色':20, '白色':0}  # 类变量

    def __init__(self, name, color, weight):  # 实例变量
        self.name = name
        self.color = color
        self.weight = weight
        #此处省略若干行，应该更新dogbook的数量

    #实例方法: 定义时,必须把self作为第一个参数，可以访问实例变量，只能通过实例名访问
    def bark(self):
        print(f'{self.name} 叫了起来')

    #类方法：定义时,必须把cls作为第一个参数，可以访问类变量，可以通过实例名或类名访问
    @classmethod
    def dog_num(cls):
        num = 0
        for v in cls.dogbook.values():
            num = num + v
        return num

    #静态方法：不强制传入self或者cls, 他对类和实例都一无所知。不能访问类变量，也不能访问实例变量；可以通过实例名或类名访问
    @staticmethod
    def total_weights(dogs):
        total = 0
        for o in dogs:
            total = total + o.weight
        return total

print(f'共有 {Dog.dog_num()} 条狗')   # 可以通过类名访问“类方法”
d1 = Dog('大黄', '黄色', 10)
d1.bark()                           # 只能能通过实例名访问”实例方法“
print(f'共有 {d1.dog_num()} 条狗')    # 也可以通过实例名访问”类方法“

d2 = Dog('旺财', '黑色', 8)
d2.bark()

print(f'狗共重 {Dog.total_weights([d1, d2])} 公斤')  # 通过实例名访问”静态方法“

total_weight = Dog.total_weights([Dog('XIAO', 'JIH', 80)]) # 也可以通过类名访问”静态方法“
print(total_weight)