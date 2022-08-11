#Examples of For Loop
#List
"""a=[1,2,3,4,56,77]
for x in a:
    print(x)

#Set
b={'Apple','Mango','Banana'}
for xy in b:
    print(xy)

#Tuple
t=('abc',34,'asd')
for x in t:
    print(x)

#String
n="Nakshathra"
for x in n:
    print(x)

#Dictionary
d={'name':'For loop','language':'Python','category':'Programming'}
for x in d:
    print(x,':',d[x])

#*********************************************************************************************

#To find the sum of all numbers in a list
l=[2,3,4,5,6,7,8,9,10,1]
sum=0
for x in l:
    sum=sum+x
print('The total sum is',sum)"""

#**********************************************************************************************

#How to use a for loop for a range of a number
for i in range(6):  #Range defines 0 to 5
    print(i)

for i in range(3,9): #Range defines 3 to 8
    print(i)

for i in range(1,9,2): #Range defines 1 to 8 with the diffrence of 2
    print(i)
