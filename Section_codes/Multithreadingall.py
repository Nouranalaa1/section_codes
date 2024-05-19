"""Example 1: Multithreading for Parallel Execution"""
import threading

# Define a function to print numbers from 1 to 5
def print_numbers():
    for i in range(1, 6):
        print("Number:", i)

# Create two threads to execute the print_numbers function
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_numbers)

# Start both threads
thread1.start()
thread2.start()

# Wait for both threads to finish
thread1.join()
thread2.join()

print("Execution complete!")

"""Example 2: Multithreading with Thread Pool Executor"""
import concurrent.futures

# Define a function to print numbers from 1 to 5
def print_numbers():
    for i in range(1, 6):
        print("Number:", i)

# Create a ThreadPoolExecutor with 2 threads
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
    # Submit the print_numbers function twice to the executor
    executor.submit(print_numbers)
    executor.submit(print_numbers)

print("Execution complete!")

"""Example 3: Multithreading for I/O-Bound Tasks"""
import threading
import requests

# Define a function to fetch a URL
def fetch_url(url):
    response = requests.get(url)
    print("URL:", url, "| Status Code:", response.status_code)

# List of URLs to fetch
urls = [
    "https://www.google.com",
    "https://www.openai.com",
    "https://www.python.org"
]

# Create a thread for each URL and start them
threads = []
for url in urls:
    thread = threading.Thread(target=fetch_url, args=(url,))
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

print("All URLs fetched!")

import time

def calc_square(numbers):
    print("calculate square numbers \n")
    for n in numbers:
        print('square:',n*n , '\n')
        time.sleep(0.2) #simulate an I/O-bound task

def calc_cube(numbers):
    print("calculate cube of numbers \n")
    for n in numbers:
        print('cube:',n*n*n , '\n')
        time.sleep(0.2) #simulate an I/O-bound task

arr = [2,3,8,9]

t = time.time()

calc_square(arr)
calc_cube(arr)


print("done in : ",time.time()-t)
print("Hah... I am done with all my work now!")

"""
A thread pool is a collection of threads that are created in advance and can be reused to execute multiple tasks. 
The concurrent.futures module in Python provides a ThreadPoolExecutor class that makes it easy to create and manage a thread pool. 
"""
# Simple example

import concurrent.futures

def worker():
	print("Worker thread running")

pool = concurrent.futures.ThreadPoolExecutor(max_workers=2)

pool.submit(worker) 
pool.submit(worker)

pool.shutdown(wait=True)

print("Main thread continuing to run")


#Race Condition Problem

import threading 

# global variable x 
x = 0

def increment(): 
	""" 
	function to increment global variable x 
	"""
	global x 
	x += 1

def thread_task(): 
	""" 
	task for thread 
	calls increment function 1000 times. 
	"""
	for _ in range(100000): 
		increment() 

def main_task(): 
	global x 
	# setting global variable x as 0 
	x = 0

	# creating threads 
	t1 = threading.Thread(target=thread_task) 
	t2 = threading.Thread(target=thread_task) 

	# start threads 
	t1.start() 
	t2.start() 

	# wait until threads finish their job 
	t1.join() 
	t2.join() 

if __name__ == "__main__": 
	for i in range(10): 
		main_task() 
		print("Iteration {0}: x = {1}".format(i,x)) 

import threading

# Shared counter variable
counter = 0

# Define a function to increment the counter using a lock
def increment_counter(lock):
    global counter
    # Acquire the lock
    lock.acquire()
    try:
        # Increment the counter
        counter += 1
    finally:
        # Release the lock
        lock.release()

if __name__ == "__main__":
    # Create a lock
    lock = threading.Lock()

    # Create multiple threads to increment the counter
    threads = []
    for _ in range(100):
        thread = threading.Thread(target=increment_counter, args=(lock,))
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    # Print the final value of the counter
    print("Final Counter Value:", counter)
