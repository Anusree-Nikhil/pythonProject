#Arbitary Arguments

def greet(*names):
    for n in names:
        print('Helloo..',n)
greet('Anu','Nakshathra','Nikhil','Anaysha')

def my_fn(*kids):
    print('The youngest one is : ',kids[1])
my_fn('Anu','Nakshathra','Nikhil','Anaysha')

def my_fn2(*kids):
    print('The eldest one is : ',kids[2])
kids=('Anu','Nakshathra','Nikhil','Anaysha')
my_fn2(*kids)

def fruits(*fruit):
    for f in fruit:
        print(f)
fruits('Apple','Orange','Banana','Mango')


#Keyword Arguments
def my_fn(ch1,ch2,ch3):
    print('The youngest child is : '+ch3)
my_fn(ch1='Emil',ch2='Tobias',ch3='Linus')

def team(name,project):
    print(name+' is working on '+project)
team('Anu','Secure Health')



#** Argument
def my_fn1(**kid):
    print('Her last name is :',kid['lname'])
my_fn1(fname='Nakshathra',lname='Nikhil')

def intro(**data):
    #print(Data type of argument:, type(data))
    for key,value in data.items():
        print('{} is {}'.format(key,value))
intro(fname='Sita',lname='Sharma',age=22,PhNo=134567892)


def fn(**a):
    for i in a.items():
        print(i)
fn(numbers=5,colour='Blue',fruit='Apple')


#Passing an argument
def food(food):
    for x in food:
        print(x)
fruit=['apple','banana','cherry','mango']
food(fruit)


