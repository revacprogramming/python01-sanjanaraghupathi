
#sum of n numbers
'''n=int(input('Enter a number(n):'))
n=n*(n+1)/2
print('the sum of n numbers is:',n)'''

#sum of even and odd number
'''a=int(input("enter a number"))
even_sum=0
odd_sum=0
count=0
count1=0
for number in range(1,a+1):
    if(number%2==0):
        even_sum=even_sum+number
        count=count+1
    else:
        odd_sum=odd_sum+number
        count1=count1+1
print('sum of even number ',even_sum)
print('sum of odd number ',odd_sum)
print(count,count1)'''
#quetion number 12
'''def computearea(a,b):
    if a==b:
        s=a*b
    else:
        print('not square')
    return s
a=int(input('enter 1st side'))
b=int(input('enter 2nd side'))
s=computearea(a,b)
print('area:',s)'''
#question 14
'''a=int(input('enter a number'))
b=int(input('enter a number'))
c=float(input('enter a number'))
d=float(input('enter a number'))
print('the sum of integers:',a+b)
print('the sum of floating point number :',c+d)'''
#question 16
'''a=float(input('enter the score'))
if 0.0<a<1.0:
    if a>=0.9:
        print('A')
    elif a>=0.8:
        print('B')
    elif a>=0.7:
        print('C')
    elif a>=0.6:
        print('D')
    elif a<=0.6:
        print('F')
else:
    print('error')'''

#question number 17



'''a=str(input('enter a string'))
def reverse(a):
    b=""
    for i in a:
        b=i+b
    return b
b=reverse(a)
if a==b:
    print('palindrome')
else:
    print('not palindrome')'''

#question 20
'''fruit='banana'
index=0
while index<len(fruit):
    letter=fruit[index]
    print(index,letter)
    index=index+1
print(fruit)
x=letter[:3]
print(x)'''

#program 22
'''a=str(input('enter a sentence'))
b= a.split()
print(b[0])'''


#program 8
'''n=10
a=0
b=1
count=0
while (count<=n) :
    sum=a+b
    a=b
    b=sum
    print(a)
    
    count=count+1'''

#square root of a number
'''from math import sqrt


a=float(input('Enter a number'))
b=sqrt(a)
print(b) '''

'''b=float(input('Enter a number'))
a=b/2
a2=b
while(a2!=a):
    a2=a
    a=((a+b/a))/2
print(a)'''

#sum of n different numbers 

b=int(input('enter the values of n'))
n=1
sum=0
while(n<=b):
    c=int(input('enter the number'))
    
    sum=sum+c
    n=n+1
print('the sum of numbers is',sum)

a=int(input("enter a number"))
b=int(input("enter a number"))
c=int(input("enter a number"))
if a>b and a>c:
    print('largest',a)

elif b>c:
     print('largest',b)
else:
    print('largest',c)

    
#finonacci
'''n=10
x,y=0,1
sum=0
count=1
while(sum<=n):
    print(sum)
    count=count+1
    x=y
    y=sum
    sum=x+y'''
#list
'''wrong
l=list([1,2,3,4,5])
for i in l:
    print(l)'''
#area of a square
'''a=int(input('enter side'))
area=a*a
print('the area of the square is:',area)'''

#sum of n numbers
'''n=int(input('Enter a number(n):'))
n=n*(n+1)/2
print('the sum of n numbers is:',n)'''

#sum of even and odd number
'''a=int(input("enter a number"))
even_sum=0
odd_sum=0
for number in range(1,a+1):
    if(number%2==0):
        even_sum=even_sum+number
    else:
        odd_sum=odd_sum+number
print('sum of even number ',even_sum)
print('sum of odd number ',odd_sum)'''

#compare 3 numbers
'''a=int(input("enter a number"))
b=int(input("enter a number"))
c=int(input("enter a number"))
if a>b and a>c:
    print('largest',a)
elif b>c:
     print('largest',b)
else:
    print('largest',c)'''


#voting
'''age=int(input('enterthe age :'))
if (age>=18):
    print('eligible')
else:
    print('not eligible')'''

jjj={'chuck':1,'fred':42,'jan':100}
print(jjj)
ooo={}
print(ooo)


'''friends=['joseph','glen','sally']
for friend in friends:
    print('happy new year:',friend)
for i in range(len(friends)):
    friend=friends[i]
    print('happy new year:',friend)'''

'''a='Reva cse@bangalore new'
x=a.find('@')
y=a.find(' ',x)
b=a[x+1:y]
print(b)'''

p=int(input('principle'))
r=int(input('rate'))
t=int(input('time'))
SI=p*t*r
print(SI)








       
