#Sum of squares of n Natural numbers
def sumsq(n):

    if n==0:
        return n
    else:
        return (n*(n+1)*(2*n+1))/6

n=int(input('Enter the number: '))
print('The sum of squares of',n ,'numbers is',sumsq(n))

#Check whether the given number is prime or not
a=int(input('Enter the number :'))
def prime(a):
    for x in range(1,a):
        if(a%x==0):
            print('The given number is not prime')
            break
        else:
            print('The given number is prime')
prime(a)

