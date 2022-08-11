#Examples of elif conditions
"""a=int(input('Enter the number : '))
if (a>0):
    print('The number is positive')
elif(a<0):
    print('The number is Negative')
else:
    print('The number is zero')"""

#**************************************************

mark=float(input('Enter your mark :'))
if(mark<100 and mark>=90):
    print('You are passed with A grade')
elif(mark<90 and mark>=80):
    print('You are passed with B grade')
elif(mark<80 and mark>=70):
    print('You are passed with C grade')
elif(mark<70 and mark>=60):
    print('You are passed with D grade')
elif(mark<50):
    print('Sorry!!.. You are failed')
else:
    print('Invalid Mark!!!!')

