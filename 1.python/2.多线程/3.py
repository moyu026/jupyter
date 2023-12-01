import threading
import time

# 假设商品数量
goods = 0

condition = threading.Condition()


def consumer():
    global goods
    while True:
        condition.acquire()  # 获取底层锁。
        if goods <= 0:
            # 仓库空了，即特定条件满足了，通知生产者生产
            condition.notify()
            condition.wait()
        time.sleep(2)
        goods -= 1
        print('consume 1， left {}'.format(goods))
        time.sleep(2)

        condition.release()  # 释放底层锁。


def producer():
    global goods
    while True:
        condition.acquire()
        if goods >= 5:
            # 仓库满了，即特定条件满足了，通知消费者消费
            condition.notify()
            condition.wait()

        time.sleep(2)
        goods += 1
        print('produce 1, already {}'.format(goods))
        time.sleep(2)

        condition.release()


if __name__ == '__main__':
    thread_consumer = threading.Thread(target=consumer)
    thread_producer = threading.Thread(target=producer)

    thread_consumer.start()
    thread_producer.start()

    thread_consumer.join()
    thread_producer.join()

    print('consumer-producer example end.')