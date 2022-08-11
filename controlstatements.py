#Examples of Control Statements
# Continue
fruits=['Apple','Banana','Cherry']
for x in fruits:
    #print(x)
    if(x=='Banana'):
        continue
    print(x)

for i in 'geeksforgeeks':
    if i=='e':
        continue
    print(i)

#*********************************************************

#Break
fruits=['Apple','Banana','Cherry']
for x in fruits:
    #print(x)
    if(x=='Banana'):
        break
    print(x)

for i in'Nakshathra':
    if(i=='k'):
        break
    print(i)

#***************************************************

#Pass
a=33
b=200
if b>a:
    pass
print('hai')

for i in 'Ammu':
    if i=='m':
        pass
        #print('pass block')
    else:
        print(i)