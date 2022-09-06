import errno


print()
print('Bike Rental System')

class bikeshop:

    def __init__(self,stock):
        self.stock=stock

    def amount(self,q):
        if q<1:
            print('Invalid request!')

        elif q>self.stock:
            print('Sorry we dont have that much stock avaliable right now!')
            print('Total avaliable stock :- ',self.stock,'bikes')

        else:
            self.stock=self.stock-q
            amount=q*100
            print('Your total rent amount is :-',amount)
            print('Total avaliable stock :- ',self.stock,'bikes')
    
    def display(self):
        print('Total avaliable stock :- ',self.stock,'bikes')

while True:
    obj=bikeshop(100)

    req=int(input('''
        1 Display avaliable stocks
        2 Request a bike for rent(100rs/bike)
        3 Exit
        '''))
    print()


    if req<1 or req>3:
        print('Invalid')

    elif req==1:
        obj.display()

    elif req==2:
        n=int(input("Enter no. of bikes :- "))
        obj.amount(n)

    else:
        break

print()

# exception handling

# # # errors

# # syntax error (devloper error cant be handled) (1.compile time errors)
# a=10
# b=20
# if a==b      # no :
# print('no')  # no indent

# # logical error (computer error can be handled) (2.logical error)
# a=10/0       # zero division error
# print(a)
# l=[10,20,30,]  # index error
# print(l[5])

# 1. ZeroDivisionError - divide by zero
# 2. IndexError        - out of index range
# 3. NameError         - varible not defined
# 4. TypeError         - concatinate diff. datatype
# 5. ValueError        - string inside int(input)
# 6. KeyError          - key not defined in dictionary
# 7. ModuleError       - module not defined
# 8. ImportError       - module function not defined

# # clint error (clint error can be handled) (3.run time errors)

try:
    print()
    print('open')
    print(10/0)
except ZeroDivisionError as e:
    print('Dont divide by 0 :-',e)
finally:
    print('close')


try:
    print()
    print('open')
    i=int(input('Eneter a no. :-'))
except ValueError as e:
    print('Invalid input :-',e)
finally:
    print('close')

try:
    print()
    print('open')
    print(b)
except Exception as e:
    print('Something went Wrong :-',e)
finally:
    print('close')

print()
print('hi')
print()

