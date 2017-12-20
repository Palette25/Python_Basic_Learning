#----------------------------Inside Library Data Type and Functions---------------------------------#
#list (similar to the array in C++)
classmates = ["Michael", "Bob", "Tracy"]
print(classmates)
print(len(classmates))
#len() show the length of the list
i = 0
while  i<len(classmates) :
    print(classmates[i])
    i += 1
#To output all the element in classmates, using while loop , and we need to focus on the
# operation character "++" and "--" aren't been used in Python
classmates.insert(1, "Clown")
#The insert Function of a list
print(classmates)
classmates.pop(0)
#The pop Function of a list
friends = ["Bob", 12]
classmates[2] = friends
print(classmates)
#The members in a list can be different data type , also other complex type including list
print(classmates[2][0])
#Try to get the member of a sublist of the classmates list, just a little bit like the two-dimentional
#array in C++


#Tuple(A kind of list that the members cannot be changed since it is founded)
t = (1, 2)
print(t)
t = (1)
print(t)
#Oops! Since the ( ) can also be the little bracket in math, so (1) is to estabilsh a num which is 1
#To avoid this wrong way, we need to define the tuple in the method below
t = (1, )
print(t)
#Truly define a tuple
t = (1, 2, [3, 4])
t[2][0] = 5
t[2][1] = 6
print(t)
#Although we cannot change the direct members in tuple, we can change the members of the
#list in tuple
input("Please click enter to exit...")