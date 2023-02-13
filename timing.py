#decorator to measure the execution time of a function. 
import time
def time_calc(func):
    def inner():
        start = time.perf_counter()
        func()
        finish = time.perf_counter()
        total = finish - start
        print(total)
    return inner
@time_calc
def function():

    print("this function took so much time to run")

function()