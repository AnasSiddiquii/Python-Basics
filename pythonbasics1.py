# print function
from msilib import sequence
import numbers
from re import T
from sqlite3 import IntegrityError
import string
from tkinter import W
from urllib.parse import parse_qs


print()
print("print function")
print("hello world",20+40,"20+30",10>5)
print()

# same memory allocation
print("same memory allocation")
a=10
b=10
print(id(a),id(b))
print()

# concatenate
print("concatenate")
print("hello"+" "+"world")
print()

# arithmetic operators
print("arithmetic operators")
print(20+10, 20-10, 20/10, 20//10, 20*10, 20**2, 20%10)
print()

# assignment operators
print("assignment operators")
x,y,z=10,20,30
x+=10
y-=10
z=10
print(x, y, z)
print()

#comparison operators
print("comparison operators")
print(10>20, 10<20, 10>=20, 10<=20, 10==20, 10!=20)
print()

#logical operators
print("logical operators")
print(10==10 and 10<20 and 10!=20)
print(10==20 or 10<20)
print(not(10==20 and 10<20)) #reverse
print()

#membership operators
print("membership operators")
sub1="python"
print('p' in sub1)
print('p' not in sub1)
print()

#identity operators
print("identity operators")
sub2="java"
print(sub1 is sub2) #same as ==
print(sub1 is not sub2) #same as !=
print()

#bitwise operators
print("bitwise operators")


# truth table
'''
a  b  &  |  ^
0  0  0  0  0
1  0  0  1  1
0  1  0  1  1
1  1  1  1  0
'''

ten=10
eight=8
print(bin(ten))
print(bin(eight))
print()

print(bin(ten & eight)) #1000
print(bin(ten | eight)) #1010
print(bin(ten ^ eight)) #10
print()

# datatypes

'''
1.numbers
    a.integer
    b.float
    c.complex
2.sequence
    a.string
    b.list*
    c.tuple
3.dictionary*
4.set
'''

# number
print("number")
p=10
q=10.5
r=10j
print(type(p))
print(type(q))
print(type(r))
print()

# sequence
print("sequence")
s="hello"
t=[1,2.5,'c',1+2]
u=(1,2.5,'c',1+2)
print(type(s))
print(type(t))
print(type(u))
print()

# dictionary
print("dictionary")
v={1:'apple','a':100,'c':'mango'}
print(type(v))
print()

# set
print("set")
w={1,2.5,'c',1+2}
print(type(w))
print()

#input
print("input")
i=input() # only string
j=int(input('enter no')) # only integer
k=float(input('enter float')) # integer n float
l=eval(input('enter any no.')) # int, float n binary
print()