class Employee:
    up = 0.1

    def __init__(self, name, salary):
        self.username = name
        self.salary = salary

    def up_salary(self):
       # self.salary = self.salary * (1 + Employee.up) # 类变量的方法
        self.salary = self.salary * (1 + self.up) # 实例变量的方法

if __name__ == '__main__':

    # Employee.up = 0.2 # 1.通过访问类变量的方法修改参数, 后面实例化类的对象都有影响

    p1 = Employee('xiaozhang', 10000)
    p1.up = 0.2         # 2.通过访问实例变量的方法修改参数，只影响当前实例化的类对象
    p1.up_salary()
    print('xiaozhang new salary', p1.salary)

    p2 = Employee('小明', 8000)
    p2.up_salary()
    print('小明 new salary', p2.salary)

