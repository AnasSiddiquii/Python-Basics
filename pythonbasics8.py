# modules

from ctypes import pointer
from email.utils import collapse_rfc2231_value
from multiprocessing import RLock


def sum(a,b):
    c=a+b
    return c

def sub(a,b):
    c=a-b
    return c

def mul(a,b):
    c=a*b
    return c

def div(a,b):
    c=a//b
    return c

# Rock/Paper/Scissor game
import random
print()
print('Rock/Paper/Scissor game')
l=['Rock','Paper','Scissor']

while True:
    cp=0
    up=0

    print('''
        1 Start game
        2 Exit
        ''')
    print()

    s=int(input())

    if s==1:
        print('Game started')
        print()
        for x in range(1,5):
            a=int(input('''
            1 Rock
            2 Paper
            3 Scissor
            '''))
            print()
            

            if a==1:
                q='Rock'
            if a==2:
                q='Paper'
            if a==2:
                q='Scissor'
            if a<1 or a>3:
                print('Invalid')

            p=random.choice(l)
            
            print('Com :-',p)
            print('You :-',q)
            print()

            if q==p:
                print('Match draw')
                up+=1
                cp+=1
                print('Your points :- ',up)
                print('Com. points :- ',cp)
            
            elif (q=='Rock' and p=='Scissor') or (q=='Paper' and p=='Rock') or (q=='Scissor' and p=='Paper'):
                print('You win')
                up+=1
                print('Your points :- ',up)
                print('Com. points :- ',cp)
            
            else:
                print('Com. win')
                cp+=1
                print('Your points :- ',up)
                print('Com. points :- ',cp)
            print()

        if up>cp:
            print('You are the winner')
        elif up<cp:
            print('Com. is the winner')
        else:
            print('Draw')

    else:
        break
