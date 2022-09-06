# conditional statement
print('if')
a=int(input('enter no.'))
if a%2==0:
    print('even')
print()



print('if else')
a=int(input('enter no.'))
if a%2==0:
    print('even')
else:
    print('odd')
print()



# result
print('elif')
a=int(input('enter marks'))
if a>=60:
    print('1st div')
elif a>=50:
    print('2nd div')
elif a>=40:
    print('3rd div')
elif a<40:
    print('fail')
else:
    print('invalid')
print()

# calculator
x=int(input('enter 1st no.  :- '))
y=input('enter operator :- ')
z=int(input('enter 2nd no.  :- '))
print()

if y=='+':
    print('your no. is :- ',x+z)
elif y=='-':
    print('your no. is :- ',x-z)
elif y=='*':
    print('your no. is :- ',x*z)
elif y=='/':
    print('your no. is :- ',x/z)
else:
    print('invalid')
print()


#range
# range(6)      #start = 0,end-1 = 6,gap = 1
# range(1,6)    #start = 1,end-1 = 6,gap = 1
# range(1,6,2)  #start = 1,end-1 = 6,gap = 2
# range(1,6,-2) #start = 1,end-1 = 6,gap = -2

for n in range(6):
    print(n)
print()

for n in range(1,6):
    print(n)
print()

for n in range(1,6,2):
    print(n)
print()

# for loop - table
a=int(input('enter no. :- '))
# for n in range(1,11):
for n in range(10,0,-1):
    print(a,'x',n,'=',a*n)
print()

# while loop
i=1
while i<=10:
    print(i,'hi')
    i+=1
print(i)
print()

j=10
while j>=1:
    print(j,'bye')
    j-=1
print(j)
print()
