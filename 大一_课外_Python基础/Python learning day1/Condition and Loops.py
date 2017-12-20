#----------------------------------------------Condition and Loop------------------------------------------#
#If and Else
age = int(input('Please input your age:'))
print("Your age is", age)
if age >= 18:
    print("You are an adult")
else :
    print("You are a teenager")
#BMI exercises, controlling the percision of the float varibles
height = float(input("Please input your height: "))
weight = float(input("Please input your weight: "))
BMI = weight / (height * height)
print(round(BMI, 2))


#For Loop
sum = 0
for x in range(101):#from 0 to 100
    sum += x
print(sum)
names = [1, 1 , 1, 1, 1]
for name in names:
    print(name)
#range controller, range(x, y) means from x to y - 1
#print function always add a \n in the end , but we can use end = "" to change the final element
sum = int(input("Please input a number: "))
for x in range(0, sum):
   time = sum
   for x in range(0, time):
     print("*", end ="")
     time -= 1
   print()
   sum -= 1


#While  Loop
sum = int(input("Please input a number: "))
while sum > 0:
    time = sum
    while time > 0:
        print("*", end = "")
        time -= 1
    print()
    sum -= 1


#dict ( A kind of dictionary that use key-value to store the varible), it provides high speed
#searching, but costs a lot of memory
#And the key in dict cannot be changed , so them cannot be varibles, and this is different
#from list, and the members of a dict can be a list.
d = {"Michael" : [43, 32], "Bob" : 75, "Tracy" : 85}
print(d["Bob"])
d["Tracy"] = 100
print(d["Tracy"])
d.pop("Bob")
print(d)

#set
s = set([1,1,2,3,4,2])
print(s)
s.add(5)
print(s)
s.remove(1)
s1 = set([0,89])
s2 = s1 & s
s3 = s1 | s
input("Please click enter to exit...")
