
### 1.占位符 %
'''
    %.3f: 保留3位小数
    %4d: 在数字前面加空格，一共占4位
    %-4d: 在数字后面加空格，一共占4位
'''
print("%s  %d  %f" % ("hello", 3, 3.1415))




### 2. .format()
'''
    占位的变量名要加大括号
'''
print("{name} {age}".format(name="Li hua", age=24))




### 3. f表达式
'''
    f表达式中的变量名要加大括号
'''
name = 'a'
age = 12
print(f'{name} is {age} years old')