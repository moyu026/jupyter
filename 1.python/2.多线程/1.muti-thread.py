from threading import Thread
from time import sleep, ctime

def func(name, sec):
    print('---开始---', name, '时间', ctime())
    sleep(sec)
    print('***结束***', name, '时间', ctime())

# 创建 Thread 实例
'''
Thread 实例化时需要接收 target，args（kwargs）两个参数。
target 用于接收需要使用多线程调用的对象。
args 或 kwargs 用于接收调用对象的需要用到的参数，args接收tuple，kwargs接收dict。
'''
t1 = Thread(target=func, args=('第一个线程', 1))
t2 = Thread(target=func, args=('第二个线程', 2))

# 启动线程运行
t1.start()
t2.start()

# 等待所有线程执行完毕
'''
如果当你的主线程还有其他事情要做，而不是等待这些线程完成，就可以不调用join()。
join()方法只有在你需要等待线程完成然后在做其他事情的时候才是有用的。'''
t1.join()  # join() 等待线程终止，要不然一直挂起
t2.join()