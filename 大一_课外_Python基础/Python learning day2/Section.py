#----------------------------------------------Section-----------------------------------------------#
#切片
ID = [12, 43 ,65, 32, 54, 78, 98, 23, 65, 21]
print(ID[0:4])
print(ID[:4])
print(ID[0:10:2])
#from 0 to 9 ,every two numbers get one
print(ID[0:9:3])
#different section way

#------------------------------------List Generation and Interations------------------------------#
#List generation（列表生成式）
list1 = [x * x for x in range(1, 10) if x%2 ==0]
print(list1)
#Quickly generate the list which satisfies the conditions， remember that we use [ ] to get
# a new list
str1 = input("Please enter the string:")
str2 = input("Please enter another string:")
list1 = [ m + n for m in str1 for n in str2]
print(list1)
#Double loop
d = {'x' : 'key1', 'y' : 'key2', 'z' : 'key3'}
list1 = [ k+ '=' + v for k, v in d.items()]
#For the elements in a dict, the output order may be different
print(list1)
#For loop can iterate many varibles in the meantime

#Generator（生成器）
g = (x * x for x in range (10))
print(g)
for x in g:
    print(x)
#Remember that we use ( ) to get a new generator
#Simply use loop to print the members in generator
def fib(k):
    n, a, b = 0, 0, 1
    while n < k:
        print(b)
        a, b = b, a+b
        n += 1
    return 'done'
#A Fibonacci sequence function, now we change this into a generator
def fib_g(k):
    n, a, b = 0, 0, 1
    while n<k:
        yield b;
        a, b = b, a+b
        n += 1
    return 'done'
#Everytime we want to use this generator function, we need to build a object
print('Simple Fibonacci Function: ', fib(5))
g = fib_g(5)
print('Generator Fibonacci Function: ', g)
for n in g:
    print(n)
#Truly use iteration to output elements

#Iterator(迭代器）
#We call all the objects that can be iterated by loop as iterable.And use isinstance( ) to
#check whether the varible is iterable or not
from collections import Iterable
a = isinstance([], Iterable)
print(a)
b = isinstance({}, Iterable)
print(b)
c = isinstance('abc', Iterable)
print(c)
#But iterable objects don't always be iterator
from collections import Iterator
a = isinstance([], Iterator)
print(a)
b = isinstance({}, Iterator)
print(b)
c = isinstance('abc', Iterator)
print(c)
#For example, x for x in range(10) is an iterator, but dict, list, string are not iterator, thousgh
#they are iterable, but we can use iter() to change them into iterator
a = isinstance(iter([ ]), Iterator)
print(a)
input('Click enter to exit...')
