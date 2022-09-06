# class/object/constructor
from cgi import print_arguments
from unicodedata import name


print()

print('class/object/constructor  :-')
print()

class abc:  # class
    a=10

    def sum(self):   # self argument its self is an object
        print(20+30) # method inside class function outside

    def show_a(self):        # without self it givs an error
        self.c=self.a*self.a # without self it givs an error
        print(self.c)        # without self it givs an error

    def show_b(self,x,y,z):  # multiple arguments
        print(x+y+z)         # no need for self

    def __init__(self):      # always inti constructor     # also need self arg.
        print('hello world') # no need to call constructor unlike method 
                            # printing 2 times cz of x & x1

print()
x=abc()     # object 1
x1=abc()    # object 2
print(x.a)  # calling class element
print(x1.a) # calling class element

print()
x.sum()          # calling method
x.show_a()       # calling method
x.show_b(1,2,3)  # calling method
print()



# inheritance
print('inheritance :-')
print()

class A:
    def displayA(self1):
        print('Hello A')

class B(A): # single level inherihance
    def displayB(self):
        print('Hello B')

class C(B): # multi level inherihance
    def displayC(self):
        print('Hello C')

# class C(A,B): # multiple inherihance
#     def displayC(self):
#         print('Hello C')

C().displayA() # same class
C().displayB() # same class
C().displayC() # same class
print()



# encapsulation means hiding elements for better exprience 
# encapsulation works on getter n setter
print('encapsulation :-')

class std:
    def __init__(self): #constructor is used to view private element
        self.__name=''            # to make variable/method private use __
    def getname(self):       # 1st getter
        return self.name     # self is must
    def setname(self,new):   # then setter
        self.name=new        # self is must

obj1=std()                   # error without object 
obj1.setname('Anas')
print(obj1.getname())
print()

class std:
    name='Amaan'
    __name='Iqra'
    def __init__(self):    # object is must n no need to call
        print(self.__name) # show private variable
        self.__display()   # show private method
    
    def display(self):     # object is must n no need to call
        print('Hello')
    def __display(self):   # object is must n no need to call
        print('Goodbye')
    
obj2=std()
i=obj2.name                # for public element
print(i)
# no need to call for private elements here
obj2.display()
print()



# polymorphism same function for different operations
# polymorphism works on overloading n overriding

l=[1,2,3,4,5,6,7,8,9]
print(len(l))
s='polymorphism'
print(len(s))
print()

class ijk:
    def display3(self,name=''):
        print('my name is '+name)

obj5=ijk()
obj5.display3()        # 1st call
obj5.display3('anas')  # 2nd call i.e. overloading by giving name
print()

class nmo:
    def display3(self):
        print('Hi')

class pqr(nmo):
    def display3(self):
        print('Bye')

obj5=pqr()
obj5.display3() # inherit class n call function with same name i.e. overriding
print()

# overloading
class area:
    def find_area(self,a=None,b=None):
        if a!=None and b!=None:
            print('Area of rectangle :- ',(a*b))
        elif a!=None:
            print('Area of square :- ',(a*a))
        else:
            print('Nothing to find')

obj6=area()
obj6.find_area()
obj6.find_area(5)
obj6.find_area(5,10)
print()

# overriding
class x:
    def displayy(self):
        print('Hello')

class y(x):
    def displayy(self):
        print('Mello')

obj5=y()
obj5.displayy() # inherit class n call function with same name i.e. overriding
print()
