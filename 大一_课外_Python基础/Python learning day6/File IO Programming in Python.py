#------------------------------------File I/O Programming in Python---------------------------------------#
#Files Write and Read
with open('/Users/Lenovo/Desktop/test.txt', 'r') as f:
    print(f.read())
with open('/Users/Lenovo/Desktop/test.txt', 'w') as f:
    f.write('Jam Jam')
with open('/Users/Lenovo/Desktop/test.txt', 'r') as f:
    print(f.read())

#StringIO and BytesIO
from io import StringIO
f = StringIO()
f.write('Palette')
print(f.getvalue())
#getvalue function is used to get the string after writen
f = StringIO('Hello!\nNight\nLetter!')
while 1 :
    s = f.readline()
    if s == '':
        break
    print(s.strip())
#strip function is used to delete the useless '\n' at the end
from io import BytesIO
f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())
#Just get the bytes in binary way

#Files operations and contents
#We can get to watch some environment varibles using os.environ.get('key')
import os
print(os.name, os.environ.get('Path'))

#Files Operations
print(os.path.abspath('.'))#get the absolute path to current file
print(os.path.join(os.path.abspath('.'), 'test'))#build a new dir in current file, firstly add its path
#to current file
os.mkdir(os.path.join(os.path.abspath('.'), 'test'))#Now we can mkdir a new file using the
#absolute path get before
os.rmdir(os.path.join(os.path.abspath('.'), 'test'))
if 0:
  os.rename('test.txt', 'test1.txt')
  os.remove('test1.txt')
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])
#os.path.spiltext() return a turple and the element of index 1 is the suffix


#Serialize
import pickle
d = dict(name='Bob', age=20, score=100)
f = open('/Users/Lenovo/Desktop/test.txt', 'wb')
pickle.dump(d, f)
f.close()
#We just can see some ugly bytes in the txt, so we must use unserialize to get back
f = open('/Users/Lenovo/Desktop/test.txt', 'rb')
d = pickle.load(f)
f.close()
print(d)
#But we cannot change the contents in the txt directly, we just decode it to be readable
f = open('/Users/Lenovo/Desktop/test.txt', 'w')
f.write('SUN')
f.close()
#Remember to close a file wherever you quit operating on it

#JSON
#When we need to get a standard pattern of transitive instance,  we need to turn thing into json
import json
d = dict(name='Clown', age=18)
string = json.dumps(d)#this function returns a string in json pattern, like dict -> json
print(string)
json_str = string
print(json.loads(json_str))#to unserialize the json str back to the python dict, json -> dict

#More about JSON
#We can use the instance as the value to change into json
class Student(object):
    def __init__(self, name, age):
        self.__name__ = name
        self.__age__ = age
    def get_name(self):
        return self.__name__
    def get_age(self):
        return self.__age

s = Student('Clown', 18)
string = json.dumps(s, default=lambda obj: obj.__dict__)
#Change the default parameter of the dumps to accept the instance
print(string)
string = json.loads(string)
print(string)
