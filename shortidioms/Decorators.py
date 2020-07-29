import time
import math
import functools

"""
First decorator timer version
using timer library
"""
def calculate_time(func):

    def inner1(*args, **kwargs):
        begin = time.time()

        value = func(*args, **kwargs)

        end = time.time()
        run_time = end - begin

        print(f"Your code took: {run_time:.2f} seconds")

    return inner1

"""
 Second decorator for calculate time 
 to took inside a function
"""
def timer(func):

    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)

        end_time = time.perf_counter()
        run_time = end_time - start_time

        print(f"Your code took: {run_time:.2f} seconds")
        return value

    return wrapper_timer


#@calculate_time
@timer
def factorial(num):

    time.sleep(2)
    print(math.factorial(num))

@calculate_time
#@timer
def doSomething(repeatNTimes):

    for _ in range(repeatNTimes):
        sum([i**2 for i in range(10000)])


factorial(10)

doSomething(400)
