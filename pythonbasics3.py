a="hello world"
print()

# indexing
print(a[4])
print(a[-5])
print()

# slicing
print(a[:])
print(a[0:5])
print(a[::2])
print()

print(a[::-1])
print(a[-7:-12:-1])
print(a[::-2])

print()

# # iteration
a=a[::-1] #1 reverse
l=len(a)  #2 length
print(l)  #  11
for r in range(l): #3 range-1
    print(r)       #  0 to 10
    print(a[r])    #4 indexing
    print()

for r in range(l-1,-1,-1): # 4 lines to 3 lines 
    print(a[r]) 
    print()

for r in a:  # 4 lines to 3 lines
    print(r) # pre-reverse only
    print()

# string functions
z='PythOn ProGramming LangUage'
print(z.upper())
print(z.lower())
print(z.title())
print(z.capitalize())
print(z.find('n',7)) # index, start (-1 if false)
print(z.index('n',7)) # same as find (error if false)
print(z.isalpha())
print(z.isdigit())
print(z.isalnum())
print()


# ASCII value starts from 65 as 'A' n 97 as 'a'
d=chr(65) # integer to ASCII 
print(type(d))
print(d)
print()

f=ord('a') # ASCII to integer
print(type(f))
print(f)
print()

# formating function
h="it {} a very {} car".format("was","big")
print(h)
h="it {1} a very {0} car".format("was","old")
print(h)
h="it {s:^11} a very {s} car".format(f="was",s="nice")
print(h)
print()

# list slicing
print('list slicing')
l=[2,3,'hello',[4,5,6]]
print(l[3][1])
print(l[-2])
print(l[::-1])

n=[1,2,3,4,5,6]
print(n[::2])
print(n[2],n[4])
print(n[-1::-2])
print()

# list iteration
print('list iteration')
o=[10,20,30,40,50,60]
t=len(o)
print(t)
print()

for f in range(t-1,-1,-1): #can reverse
    print(o[f])
print()

for e in o: #cant reverse
    print(e)
print()

# list comprehension
print('list comprehension')
j=[] # normal method
for d in range(1,11):
    j.append(d)
print(j)

k=[h for h in range(1,11) if h%2==0] # comprehension method
w=[h for h in range(1,11) if h%2!=0] # comprehension method
print('even no.:-',k,'odd no.:-',w)

u='comprehension' # normal method
p=[]
for i in u:
    p.append(i)
print(p)

g="hello" # comprehension method
q=[h for h in g]
print(q)
print()