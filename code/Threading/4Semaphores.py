import threading
import time

'''Shared Resource: shared_counter is the shared resource accessed by multiple threads.
Semaphore Object: A Semaphore object semaphore is created with a counter value of 2, allowing up to two threads to access the shared resource concurrently.
CounterThread Class: Inherits from threading.Thread.

    run Method: Overrides the run method. Inside the method, the thread:
        Acquires the semaphore using semaphore.acquire().
        Increments the shared_counter.
        Releases the semaphore using semaphore.release().
    The try-finally block ensures that the semaphore is released even if an exception occurs.

Creating Threads: Instances of CounterThread are created with specific names.
Starting Threads: The start() method is called on each thread to begin execution.
Joining Threads: The join() method is called to ensure the main program waits for the threads to complete.'''

# Shared resource
shared_counter = 0

# Create a Semaphore object with a counter value of 2
semaphore = threading.Semaphore(2)

class CounterThread(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        global shared_counter
        for _ in range(5):
            time.sleep(1)
            semaphore.acquire()  # Acquire the semaphore before accessing the shared resource
            try:
                print(f"{self.name} acquired the semaphore")
                shared_counter += 1
                print(f"{self.name} incremented counter to {shared_counter}")
            finally:
                print(f"{self.name} releasing the semaphore")
                semaphore.release()  # Release the semaphore after accessing the shared resource

# Create new threads
thread1 = CounterThread("Thread-1")
thread2 = CounterThread("Thread-2")
thread3 = CounterThread("Thread-3")

# Start new Threads
thread1.start()
thread2.start()
thread3.start()

# Wait for all threads to complete
thread1.join()
thread2.join()
thread3.join()

print("Final counter value:", shared_counter)
print("Exiting Main Thread")
