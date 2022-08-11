#Examples of Nested if condition
"""i=10
if(i==10):
    if(i<15):
        print('i is smaller than 15')
    if(i<12):
        print('i is smaller than 12 too')
else:
    print('i is greater than 15')"""

#********************************************

n=float(input('Enter the number : '))
if(n>=0):
    if n==0:
        print('The number is zero')
    else:
        print('The number is a positive number')
else:
    print('The number is a negative number')