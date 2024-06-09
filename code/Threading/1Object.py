import threading
import time

def print_numbers():
    for i in range(10):
        print(i)
        time.sleep(1)

def print_letters():
    for letter in 'abcdefghij':
        print(letter)
        time.sleep(1)

def my_function():
    print(threading.current_thread().name)

#creation
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)
thread3 = threading.Thread(target=my_function, name="MyThread")

thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()






print("Done!")
