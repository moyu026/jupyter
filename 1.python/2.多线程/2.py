from threading import Thread, Condition

# 创建条件变量
condition = Condition()

# 初始化标志，表示当前应该输出字母
should_output_letter = True

def output_letter():
    global should_output_letter
    for i in range(26):
        with condition:
            while not should_output_letter:
                condition.wait()
            letter = chr(ord('A') + i)  # 大写字母
            print(letter, end=' ')
            should_output_letter = False
            condition.notify()
'''
condition.notify()
唤醒一个或多个等待此条件变量的线程。此方法只会在调用线程已经获取锁之后调用，
而且如果没有正在等待的线程，它就什么也不做。'''


def output_number():
    global should_output_letter
    for i in range(26):
        with condition:
            while should_output_letter:
                condition.wait()
            print(i, end=' ')
            should_output_letter = True
            condition.notify()


if __name__ == "__main__":
    t1 = Thread(target=output_letter)
    t2 = Thread(target=output_number)

    t1.start()
    t2.start()

    t1.join()
    t2.join()
