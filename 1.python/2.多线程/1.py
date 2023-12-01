from threading import Thread

def output_letter():
    for i in range(26):
        letter = chr(ord('A') + i)  # 大写字母
        print(letter, end=' ')

def output_number():
    for i in range(26):
        print(i)




if __name__ == "__main__":
    t1 = Thread(target=output_letter)
    t2 = Thread(target=output_number)

    t1.start()
    t2.start()

    t1.join()
    t2.join()