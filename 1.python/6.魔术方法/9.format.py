# 创建一个类
class Human:
    # 成员属性
    color = 'yellow'
    age = 18
    str = '------'
    name = '@#$%'

    # 成员方法
    def eat(self):
        print('eat')

    def say(self):
        print('****')

    # 魔术方法__format__
    def __format__(self, format_spec): # format_spec接收的是限定符号的字符串
        # print('format method start')
        # print('format_spec的内容', format_spec)
        # return self.str

        # 实现format自带的对齐和填充功能
        # 1.接收限定符号
        flag = format_spec
        # 2.拆分限定符号
        fillchar = flag[0] # 填充字符
        align = flag[1]   # 对齐方式
        length = int(flag[2:])
        # 3.根据不同的符号进行不同的填充操作
        if align == '>':  # 右对齐
            newname = self.name.rjust(length, fillchar)
            return newname
        elif align == '^': # 居中对齐
            newname = self.name.center(length, fillchar)
            return newname
        elif align == '<': # 左对齐
            newname = self.name.ljust(length, fillchar)
            return newname
        else:
            return ''

# 实例化对象
one = Human()
print(one)

# 使用format来操作对象
line = 'asdfajl{:@^10}af'
result = line.format(one)
print(result)