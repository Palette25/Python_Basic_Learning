#------------------------------------------------Functions----------------------------------------------------#
#Self-design functions
def my_abs(x):
#parameters check
    if not isinstance(x, (int, float)):
       raise TypeError('bad operand type')
    if x >= 0:
        return x
    else :
        return -x
x = int(input("Please input a number: "))
print("The abs of the number is :", my_abs(x))
import math
#get the inside math functions, and the default parameter 
def move(x, y, step, angle = 0):
    nx = x + step*math.cos(angle)
    ny = y  + step*math.sin(angle)
    return nx, ny
#functions can return many values, and to be honest it return a tuple, then get the vlaues of the
#tuple and assign them to the corresponding positions
x, y = move(1, 2, 5, math.pi / 6)
r = move(0,0,0)
print(r)
print(x, y)
def quadratic(a, b, c):
    if b*b - 4*a*c < 0:
        return None
    x1 = (-b + math.sqrt(b*b-4*a*c)) / (2 * a)
    x2 = (-b -  math.sqrt(b*b-4*a*c)) / (2 * a)
    return x1, x2
a = int(input("Please input the first number: "))
b = int(input("Please input the second number: "))
c = int(input("Please input the third number: "))
if b*b - 4*a*c < 0:
    print("Oops!")
else :
    x1, x2 = quadratic(a, b, c)
    print(x1, x2)


#Parameters in functions
#1.Flexible parameters（可变参数）
def calc(*numbers) :
        sum = 0
        for n in numbers:
            sum = sum + n * n
        return sum
numbers = [1, 2, 3, 4]
number = (1, 2, 3, 4)
print(calc(*numbers))
print(calc(*number))
print(calc(1, 2, 3, 4))
#By using the * before the parameter, we can make the type of real parameter be flexible,
#be some different types, including list, tuple, and int

#2.Key-value parameters（关键字参数）
def person(name, age, **kw):
    print('name:', name,'age:', age, 'other:', kw)
name = input("Please enter your name:")
age = int(input("Please enter your age:"))
flag = int(input("If you can, please enter your city and gender:"))
if flag is 1:
    city1 = input()
    gender1 = input()
    person(name, age, city = city1, gender = gender1)
    person(name, age, city = city1)
    extra = {'city': city1 , 'gender':gender1}
    person(name, age, **extra)
#can also store the informations into the dict and then give it to the function
else:
   person(name, age)
#Key-value parameters can expand the numbers of parameters to no matter how many we
#input, just use ** and put them into a dict

#Name key-value parameters（命令关键字参数）
location = input('Please input your location:')
job = input('Please input your job:')
def person1(name, age, *, location, job = 'NUll'):
      print('name:', name, 'age:', age, location, job)
person1(name, age, location = location)
person1(name, age, location = location, job = job)
#input the prescribed parameters

#The compositions of  the parameters, five different parameters
#必选参数，默认参数，可变参数，关键字参数，命令关键字参数
def f1(a, b, c=0, *args, **kw):
    print('a =',a,'b =',b,'c =',c,'args =' ,args,'kw =',kw)
def f2(a, b, c=0, *, d, **kw):
    print('a =',a,'b =',b,'c =',c,'d =',d,'kw =',kw)
f1(1, 2)
f1(1, 2, 3)
f1(1, 2, 3,*numbers, name = 'cml')
f2(1, 2, 3, d= 99, ext =None)

#Every functions can be represented by func(*args, **kw)


#Tail recursion（尾递归）
def fac(n):
    if n is 1:
        return 1
    return n * fac(n-1)
#FAC function, it use calculating expressions in the end of the return sentence,
#so it may cause the stackoverflow while t is too big
def fac1(n):
    return fac_iter(n, 1)
def fac_iter(num, pro):
    if num==1:
        return pro
    return fac_iter(num - 1, num * pro)
#This is the way we call tail recursion, although it's more complex, moving the
#expression into the tail of another function can reduce the number of stacks
#being used while calculating to the only one（只调用一个栈帧）
print(fac(7))
print(fac1(10))
input("Please click enter to exit...")
