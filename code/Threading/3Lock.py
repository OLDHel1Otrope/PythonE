import threading
import time

# Shared resource
shared_counter = 0

# Create a Lock object
lock = threading.Lock()

class CounterThread(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        global shared_counter
        for _ in range(5):
            time.sleep(1)
            lock.acquire(timeout=5)  # Acquire the lock 
            try:
                print(f"{self.name} acquired the lock")
                shared_counter += 1
                print(f"{self.name} incremented counter to {shared_counter}")
            finally:
                print(f"{self.name} releasing the lock")
                lock.release()  # Release the lock 

# Create new threads
thread1 = CounterThread("Thread-1")
thread2 = CounterThread("Thread-2")

# Start new Threads
thread1.start()
thread2.start()

# Wait for all threads to complete
thread1.join()
thread2.join()

print("Final counter value:", shared_counter)
print("Exiting Main Thread")


'''Shared Resource: shared_counter is the shared resource accessed by multiple threads.
    Lock Object: A Lock object lock is created to ensure synchronization.
    CounterThread Class: Inherits from threading.Thread.

    run Method: Overrides the run method. Inside the method, the thread:
        Acquires the lock using lock.acquire().
        Increments the shared_counter.
        Releases the lock using lock.release().
    The try-finally block ensures that the lock is released even if an exception occurs.

    Creating Threads: Instances of CounterThread are created with specific names.
    Starting Threads: The start() method is called on each thread to begin execution.
    Joining Threads: The join() method is called to ensure the main program waits for the threads to complete.'''