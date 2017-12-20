#--------------------------------------------OOP in Python--------------------------------------------------#
#Class and Instance
#We declare a class in Python using "class XXX(Interhitant class)" type.
class student(object):
    def __init__(self, name, score):#special class function
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))
    
    def get_level(self):
        if self.score>=90:
            return 'A'
        elif self.score>=60:
            return 'B'
        else: return 'C'

bart = student('Clown', 100)

bart.print_score()

print(bart.get_level())

#Visit Limit
#In OOP of Python, if we want to make a varible private, just add __ before its name
class human():
    def __init__(self, name, age, sex):
        self.__name = name
        self.__age = age
        self.__sex = sex
    def print_self(self):
        print('%s: %s, %s' % (self.__name, self.__sex, self.__age))
    def get_name(self):
        return self.__name
    def get_sex(self):
        return self.__sex
    def get_age(self):
        return self.__age
    def set_age(self, age):
        if 0 <= age <= 100:
            self.__age = age
        else:
            raise ValueError('bad input')
bath = human('Clown', 18, 'Man')
bath.print_self()
bath.set_age(20)
bath.print_self()

#Inheritance and Polymorphism
class animal():
    def __init__(self, name):
        self.__name = name
    def run(self):
        print('Animal is runnig....')

class dog(animal):
    def __init__(self, name, weight):
        self.__name = name
        self.__weight = weight
    def run(self):
        print('Dog %s is runnig....' % self.__name)

class cat(animal):
    def __init__(self, name, weight):
        self.__name = name
        self.__weight = weight
    def run(self):
        print('Cat %s is runnig....' % self.__name)

dog = dog('Clown1', 40)
cat = cat('Clown2', 54)
animal = animal('SUN')
dog.run()
cat.run()
#Atuomatically distinguish the type of parameters
def run(animal):
    animal.run()
run(dog)
run(cat)
run(animal)
dir(dog)

#Properties of instances and class
dog.age = 12
class phone():
    name = 'phone'
#This name belongs to this class, similar to the static varible of C++
    
#__slots__
#If we want to limit the varibles added to the instance, we can use __slots__
class ken():
    __slots__ = ('name', 'age')
s = ken()
s.name = 'Michael' #Valid
#Invalid behavior : s.score = 99 

#Some other special types of functions can be added to a class
#__str__
class School():
    def __init__(self, name):
        self.__name__ = name
    def __str__(self):
        return 'School object (name: %s)' % self.__name__
    __repr__ = __str__
m = School('SYSU')
print(m)
#When we add a __str__ function to a class, if we use print to output an object, we can design the
#output pattern


#__iter__
#To get an iteration from the instance
class fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100 :
            raise StopIteration()
        return self.a
#Now let's test this iter function
for n in fib():
    print(n)

#__getitem__
#To correctly get the elements of the index like f[0]
class fib(object):
    def __getitem__(self, index):
        a, b = 1, 1
        for x in range(index):
            a, b = b, a+b
        return a
#Now we can get the elements
f = fib()
for n in range(0, 5):
    print(f[n])
    
#__getattr__
#Sometimes we don't correctly call the attributes existing in the class, now if we want to
#dynamically return a varible, we can use __getattr__
class fib(object):
    def __getattr__(self, attr):
        if attr == 'num':
            return 10
f = fib()
print(f.num)

#__call__
class fib(object):
    def __getitem__(self, index):
        a, b = 1, 1
        for x in range(index):
            a, b = b, a+b
        return a
    
    def __call__(self, length):
        for n in range(length):
            print(self[n])
f = fib()
f(9)
#When we define the __call__ function, we can directly use instance to use the methods in the class


#Enum class
#The first step ---- using the enum class provided by the library
from enum import Enum, unique
Month = Enum('month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
#Now we get a simple enum class Month
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)
#The special function items() return a dict, and we can use every varible in it

#The second step --- make our own enum class
@unique
class weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
for name, member in weekday.__members__.items():
    print(name, '=>', member, ',', member.value)


#Metaclass
#If we want to change something or add some funcitons to the class, we can use metaclass,
#Because we regard class as an instace from the metaclass
