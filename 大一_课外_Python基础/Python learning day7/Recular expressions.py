#------------------------------------------Regular Expression-----------------------------------------------#
#Regular expression
#\d ------ a number
#\w ----- a letter
#\s ------ a space or a tab
#\, ------ , (just a escape character)
#+ ------ added at the end of other, just to show that there are more the same characters

#re part
import re
x = int(input('Please input the number of cases: '))
for n in range(0, x):
    s = input('Please input the string to check: ')
    result = re.match(r'^\d{3}\-\d{3,8}$', s)
    print(result)

#Split
string = re.split(r'\s+', 'a b   c')
print(string)
#Using split function to cut the part that satisfies the pattern of the regular expression
string = re.split(r'[\s\,\;]+', 'a, b, c; d')
print(string)

#Group
x = int(input('Please input the number of cases: '))
for n in range(0, x):
    s = input('Please input the string to check: ')
    result = re.match(r'^(\d{3})-(\d{3,8})$', s)
    print(result)
    if result!=None:
      print(result.group(0))
      print(result.group(1))
      print(result.group(2))
#Using (） to devide the expression to some groups, and then using group funcion to get the substr
