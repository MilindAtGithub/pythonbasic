# Decorator Function
# In Python, functions are the first class objects, which means that –

# Functions are objects; they can be referenced to, passed to a variable and returned from other functions as well.
# Functions can be defined inside another function and can also be passed as argument to another function.
# Decorators are very powerful and useful tool in Python since it allows programmers to modify the behavior of function or class.
# Decorators allow us to wrap another function in order to extend the behavior of wrapped function, without permanently modifying it.
#
# In Decorators, functions are taken as the argument into another function and then called inside the wrapper function.


# Lets try to create basic one

import time

def f1(f):
    def f2():
        print(" F2 Called Before")
        f()
        print('F2 Called After')
    return f2
@f1
def f3():
    print('F3 Called')

x = f1(f3)
x()

f3()

# Use Case Let create the wrapper function to calculate the response time of the call


def responseTime(f):
    def wrapper():
        x = time.time()
        f()
        y= time.time()
        print(f"Time Taken : {y-x}")
    return  wrapper

@responseTime
def sum():
    for i in range(10000):
        i += i

sum()