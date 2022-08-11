"""x=0
while x<=18:
    x=x+3
print(x)

a=100/5
b=20//3
print(a*b)

def fun():
    for x in range(22,23,24):
        print(x)
fun()

a=~4
b=a+4
print(b)

def fun():
    return 55+int(55.55)
print(fun())

print('abc.DEF'.capitalize())

x='python'
y='pythoN'
print(x>y)

s1=str('python')
s2='python'
print(s1==s2,s1 is s2)
print(type(s1))
print(type(s2))
print(s1,s2)
print(s1.upper())

def add(a,b):
    return a+5,b+5
result=add(3,2)
print(result)

c=1/3
d=3/1
print(c*d)

l=list('1234')
l[0]=l[1]=5
print(l)

e='butter'
def f(a): print(a+e)
f('bitter')"""

l=[1,6,8,20,12,34]
m1=min(l)
print(m1)
m2=max(l)
print(m2)
p1=l.index(min(l))
print(p1)
p2=l.index(max(l))
print(p2)

n=int(input('Enter the number : '))
temp=n
length=len(str(n))
sum=0
while n>0:
    sum=sum+(n%10)**length
    n=n//10
if(temp==sum):
    print('The given number is amstrong')
else:
    print('The given number is not amstrong')


s='ANU'
b=s[::-1]
print(b)

for i in range(8,0,-1):
    for j in range(i):
        print('*',end=' ')
    print()
for i in range(0,8):
    for j in range(0,i+1):
        print('*',end=' ')
    print()

n=10
k=n-1
for i in range(0,n):
    for j in range(0,k):
        print(end=' ')
    k=k-1
    for j in range(0,i+1):
        print('*',end=' ')
    print()

num=1
for i in range(0,8):
    num=1
    for j in range(0,i+1):
        print(num,end=' ')
        num=num+1
    print()