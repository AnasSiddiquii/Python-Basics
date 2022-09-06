# print()
# l=[]
# while True:
#     c=int(input('''
#             Stack - LIFO
#         1 Add element at the last
#         2 Display the last element
#         3 Detete the last element
#         4 Display full stack
#         5 Exit
#         '''))
#     if c==1:
#         n=input("Enter the value :- ")
#         l.append(n)
#     elif c==2:
#         if len==0:
#             print('Empty stack')
#         else:
#             print("last stack element :- ",l[-1])
#     elif c==3:
#         if len(l)==0:
#             print('Empty stack')
#         else:
#             print(l.pop(-1))
#     elif c==4:
#         print("Full stack :- ",l)
#     elif c==5:
#         break
#     else:
#         print('Invalid')
# print()

print()
l=[]
while True:
    c=int(input('''
            Queue - FIFO
        1 Add element at the last
        3 Display the first element
        2 Detete the first element
        4 Display full queue
        5 Exit
        '''))
    if c==1:
        n=input("Enter the value :- ")
        l.append(n)
    elif c==2:
        if len==0:
            print('Empty queue')
        else:
            print("First queue element :- ",l[0])
    elif c==3:
        if len(l)==0:
            print('Empty queue')
        else:
            print(l.pop(0))
    elif c==4:
        print("Full queue :- ",l)
    elif c==5:
        break
    else:
        print('Invalid')
print()