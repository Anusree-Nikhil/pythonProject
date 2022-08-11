"""def my_function():  #To define a function
    print('Hello my World') #Statements

my_function()    #To call a function

def my_prgm():
    print('Haii hello... Good morning..')
my_prgm()

#Examples of fuctions
def substraction():
    print(20-30)
substraction()
def subs():
    a=10
    b=20
    c=b-a
    print(c)
subs()

#Functions with arguments
def name(fname):
    print(fname)
name('Anu')

def name2(fn):
    print('Hai..',fn)
name2('Nakshathra')

def name3(fnm):
    print(fnm+' Nikhil')
name3('Nakshathra')

def sum():
    a=int(input('enter first no. : '))
    b=int(input('enter second no. : '))
    c=a+b
    print(c)
sum()

def sum1(x,y):
    z=x+y
    return z
x=int(input('enter first no. : '))
y=int(input('enter second no. : '))
print('sum is' ,sum1(x,y))


def even(x):
    if(x%2==0):
        print('The given number is even')
    else:
        print('The given number is odd number')
x=int(input('Enter the number :'))
even(x)

#Vowels count
def vowel(s):
    vw='aeiouAEIOU'
    vc=0
    for i in s:
        if i in vw:
            vc=vc+1
    return vc
s=input('Enter a string : ')
print(vowel(s))


def wordcount(x):
    c=1
    for i in s:
        c=c+1
    return c
x=input('Enter the string : ')
print('Total words in string :',wordcount(x))

def my_fun(fname, lname):
    print(fname + 'and' +lname)
my_fun('Anu ',' Nakshathra')

def my_fun2(name,msg):
    print('Helloo..',name,msg)
my_fun2('Nakshathra','Good morning')"""

#To find the sum of n Natural numbers
def sum(num):
    s=0
    while num>=0:
        s=s+num
        num=num-1
    return s
num=int(input('Enter the number: '))
print('The sum is: ',sum(num))

def sum1(n):

    if n==0:
        return n
    else:
        return n*(n+1)/2

n=int(input('Enter the number: '))
print('The sum of',n ,'numbers is',sum1(n))

def sum2(*numbers):
    sum=0
    for x in numbers:
        sum=sum+x
    print('The sum is ',sum)
sum2(2,3,4,5,6)



