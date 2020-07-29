import time

def lambdaSorted():
    my_list = ["cat", "dog", "bird", "alligator"]

    # Sorted with natural order
    #sortedList = sorted(my_list)

    #sorted with an specific criteria
    sortedList = sorted(my_list, key= lambda item: item[-1])

    return sortedList

# Decorator for Timer
def my_decorator(func):

    def wrapper_time(*args, **kwargs):
        begin = time.time()

        value = func(*args, **kwargs)

        end = time.time()
        run_time = end - begin

        print(f"Your code took: {run_time:.2f} seconds")

    return wrapper_time

@my_decorator
def execute_sum(repeatNTimes):
    for _ in range(repeatNTimes):
        sum([i ** 2 for i in range(10000)])

print(lambdaSorted())
print("*" *60)
execute_sum(400)