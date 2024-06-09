from concurrent.futures import ThreadPoolExecutor
import time

'''The concurrent.futures module provides a high-level interface for asynchronously executing callables.'''

def print_numbers():
    for i in range(10):
        print(i)
        time.sleep(1)

def print_letters():
    for letter in 'abcdefghij':
        print(letter)
        time.sleep(1)

with ThreadPoolExecutor(max_workers=2) as executor:
    executor.submit(print_numbers)
    executor.submit(print_letters)

print("Done!")
