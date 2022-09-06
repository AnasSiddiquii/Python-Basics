# list functions

# delete list functions

a=[20,30,40,50,60]
del a[1] # works on index no. bt dont return value
print()

print(a)
print()

print(a.pop(3)) # works on index no. bt do return value
print(a)
print()

a.remove(20)  # works on value
print(a)
print()

a.clear()  # clears whole list
print(a)
print()

# update list functions

b=[20,30,40,50,60] # normal update
b[0]=60
print(b)
print()

b.insert(3,30) # works on index n value
print(b)
print()

b.append(10) # adds no. to the last 
print(b)
print()

c=[1,2,3,4]
b.extend(c) # adds 2nd list at the last 
print(b)
print()

# other list function

d=[10,20,30,10,40]
z=d.count(10)
print(z)
print()

d.sort()
print(d)
print()

d.reverse() # sort+reverse
print(d)
print()

w=d.index(20)
print(w)
print()


e=['hello', 'world']
y=max(e)
print(y)
print()

x=min(e)
print(x)
print()


i=[10,20,30]
j=[40,50,60,70]
k=[80,90]
for a,b,c in zip(i,j,k):
    print(a,b,c)
print()

t=len(k)
for a in range(t):
    print(i[a],j[a],k[a])
print()

# string to list conversion
h="assignment"
r=len(h)

t=[] # normal method
for a in range(r):
    t.append(h[a])
print(t)

g=[h[a] for a in range(r)] # pro method
print(g)

s="python programing assignment" # word to list
l=s.split()
print(l)
print()

v=[]
for a in range(1,4):
    n=input('enter the value '+str(a)+':- ')
    v.append(n)
    print()
print(v)
print()
