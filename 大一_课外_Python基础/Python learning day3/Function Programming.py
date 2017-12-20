#----------------------------------------Higher-order function-----------------------------------------------#
#Simple introduction
#We can let a varible store the name of a function
def abs(x):
    if x > 0: return x
    else: return -x
x = int(input("Please enter a number: "))
print("This number's abs is ", abs(x))
k = abs
print("This function's address is ", k)
#As the varible can store name of the function, then we can make a function accept another function
#name as its parameter, we call this kind of functions as higher-order function
def add(x, y, f):
    return f(x) + f(y)
print(add(-1, 2, k))
def do_some(add, k, x, y):
    return add(x, y, k) + k(x) + k(y)
print(do_some(add, k, 1, 2))

#Map and Reduce
#map(function's name, order structure), this map(square, r) return an iterator, we often change it
#into the list
def square(x):
    return x*x
r = [1, 2, 3, 4, 5]
s = list(map(square, r))
print(s)
s = list(map(str, r))
#change number into string
print(s)

#reduce(function's name, order structure), just like add(add(add(x1, x2), x3), x4), accumulation using
#the function given in.
from functools import reduce
def add(x, y):
    return x+y
x = reduce(add, r)
print(x)

