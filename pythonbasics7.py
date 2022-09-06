# user defined module

# import pythonbasics8 as a
# print(a.sum(10,10))
# print(a.sub(10,10))
# print(a.mul(10,10))
# print(a.div(10,10))
# print()

from pythonbasics8 import * 
print(sum(10,10))
print(sub(10,10))
print(mul(10,10))
print(div(10,10))
print()

# math module

import math
x=-11.4
print(math.ceil(x)) # next no.
print(math.floor(x)) # current no.
print(math.fabs(x)) # positive no
y=5
print(math.factorial(y)) # 5+4+3+2+1
l=[10,20,30,40,50]
print(math.fsum(l)) # works any type of list # adds elements
z=16
print(math.sqrt(z)) # square root
print()

# random module

import random
print(random.randint(5,10)) # 5 t0 10
print()
# same
print(random.randrange(5,10)) # 5 to 9
print()

l=[10,20,30,40,50]
print(random.choice(l)) # any no. from list
print()

print(random.random()) # any float no. from 0 to 1
print()

random.shuffle(l)
print(l) # shuffle list
print()

print(random.uniform(3,9)) # any float no. 3 to 9
print()

# date n time module

import datetime
print(datetime.datetime.now()) # current date n time
print()

print(datetime.datetime(2020,2,20,12,12,12)) # costom date n time
print()

# print(datetime.datetime.now().strftime("%y"))
# same
t=datetime.datetime.now()

print(t.strftime("%B")) # month
print(t.strftime("%m")) # date 
print(t.strftime("%y")) # 22
print(t.strftime("%Y")) # 2022
print(t.strftime("%H")) # hr in 24hr
print(t.strftime("%I")) # hr in 12hr
print(t.strftime("%p")) # am pm
print(t.strftime("%M")) # min
print()

# no. guessing game

print('no. guessing game')
q=random.randrange(1,11)
p=int(input('Enter a no. 1 to 10 :- '))

if p<1 or p>10:
    print('Invalid')
elif q<p:
    print('Com. no. :- ',q)
    print('Your no. :- ',p)
    print('Your guess is high')
elif q>p:
    print('Com. no. :- ',q)
    print('Your no. :- ',p)
    print('Your guess is low')
else:
    print('Com. no. :- ',q)
    print('Your no. :- ',p)
    print('Your guess is correct')
print()