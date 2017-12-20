#Hannota in python
def move(n, a, b, c):
   k = n
   if n==1: 
   	print(a,'->',c)
   else :
   	move(n-1, a, c, b)
   	print(a,'->',c)
   	move(n-1, b, a, c)
n = int(input("Please enter the number of the disks:"))
a = input("Please enter the letter of the first disk:")
b = input("Please enter the letter of the second disk:")
c = input("Please enter the letter of the third disk:")
move(n, a, b, c)
input("Please click enter to exit...")