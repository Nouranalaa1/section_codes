import time
import multiprocessing

def calc_square(numbers):
    for n in numbers:
        print('square ' + str(n*n))
        time.sleep(3)

def calc_cube(numbers):
    for n in numbers:
        print('cube ' + str(n*n*n))
        time.sleep(3)


if __name__ == "__main__":
    arr = [2,3,8]
    
    t = time.time()
    p1 = multiprocessing.Process(target=calc_square, args=(arr,))
    p2 = multiprocessing.Process(target=calc_cube, args=(arr,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
  
     
    print("done in : ",time.time()-t)

    print("The number of CPU currently working in system : ", multiprocessing.cpu_count()) 

import time
import multiprocessing

def calc_square(numbers):
    for n in numbers:
        print('square ' + str(n*n))
        time.sleep(3)

def calc_cube(numbers):
    for n in numbers:
        print('cube ' + str(n*n*n))
        time.sleep(3)


if __name__ == "__main__":
    arr = [2,3,8]
    
    t = time.time()
    p1 = multiprocessing.Process(target=calc_square, args=(arr,))
    p2 = multiprocessing.Process(target=calc_cube, args=(arr,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
  
     
    print("done in : ",time.time()-t)

    print("The number of CPU currently working in system : ", multiprocessing.cpu_count()) 

import multiprocessing

# Define a function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

if __name__ == "__main__":
    # Define the range of numbers to check for primality
    numbers = range(1000000)

    # Create a multiprocessing Pool with as many processes as CPU cores
    num_processes = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(processes=num_processes)

    # Map the is_prime function to the list of numbers using multiprocessing
    results = pool.map(is_prime, numbers)

    # Close the pool to free up resources
    pool.close()
    pool.join()

    # Count the number of prime numbers found
    num_primes = sum(results)

    print("Number of prime numbers found:", num_primes)
#This example demonstrate communications between processes
"""
Effective use of multiple processes usually requires some communication between them, so that work can be divided and results can be aggregated.
multiprocessing supports two types of communication channel between processes:
-Queue
-Pipe
"""
"""
Pipes : A pipe can have only two endpoints. Hence, it is preferred over queue when only two-way communication is required. 
multiprocessing module provides Pipe() function which returns a pair of connection objects connected by a pipe. 
The two connection objects returned by Pipe()represent the two ends of the pipe. Each connection object has send() 
and recv() methods (among others).
"""
# Pipe Example

import multiprocessing 

def sender(conn, msgs): 
	""" 
	function to send messages to other end of pipe 
	"""
	for msg in msgs: 
		conn.send(msg) 
		print("Sent the message: {}".format(msg)) 
	conn.close() 

def receiver(conn): 
	""" 
	function to print the messages received from other 
	end of pipe 
	"""
	while 1: 
		msg = conn.recv() 
		if msg == "END": 
			break
		print("Received the message: {}".format(msg)) 

if __name__ == "__main__": 
	# messages to be sent 
	msgs = ["hello", "hey", "hru?", "END"] 

	# creating a pipe 
	parent_conn, child_conn = multiprocessing.Pipe() 

	# creating new processes 
	p1 = multiprocessing.Process(target=sender, args=(parent_conn,msgs)) 
	p2 = multiprocessing.Process(target=receiver, args=(child_conn,)) 

	# running processes 
	p1.start() 
	p2.start() 

	# wait until processes finish 
	p1.join() 
	p2.join() 
