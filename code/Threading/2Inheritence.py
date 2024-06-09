import threading
import time

'''important points to consider
    Threading module vs multiprocessing module
    Thread Safety using locks, semaphores, and conditions.
    >Deadlocks
    >Daemon Threads thread.setDaemon(True)  Daemon threads run in the background and do not prevent the program from exiting.
    >Thread Communication: queue.Queue
    >concurrent.futures.ThreadPoolExecutor
    >threading.Condition
    >There are no thread priorities in py
    '''

class CustomThread(threading.Thread):
    def __init__(self, name, delay):
        threading.Thread.__init__(self)
        self.name = name
        self.delay = delay

    def run(self):
        print(f"Starting {self.name}")
        self.print_time()
        print(f"Exiting {self.name}")

    def print_time(self):
        count = 0
        while count < 5:
            time.sleep(self.delay)
            count += 1
            print(f"{self.name}: {time.ctime(time.time())}")

thread1 = CustomThread("Thread-1", 1)
thread2 = CustomThread("Thread-2", 2)

print(threading.current_thread()) #gives the name of the current running thread


thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Exiting Main Thread")
