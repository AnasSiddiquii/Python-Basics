from audioop import minmax
from cgi import print_arguments
from itertools import count
from os import popen, remove
from turtle import clear


a={'name':'anas','class':'10th','roll_no':46}
print()

print(a['name'])    # same 1
print(a['class'])
print(a['roll_no'])
print()

for b in a:
    print(b)        # same 2
    print(a[b])     # same 3
    print()

# get function
n=a.get('name')     # same 1
print(n)
print()

# key function
for c in a.keys():   # same 2
    print(c)
print()

# value function
for d in a.values(): # same 3
    print(d)
print()

# items function
for e in a.items():
    print(e)
print()

# delete function
del a['class']
print(a)
print()

# pop function
print(a.pop('name'))
print(a)
print()

# nested dictionary
course={
    'php':{'duration':'2 months','fees':15000},
    'java':{'duration':'2 months','fees':15000},
    'python':{'duration':'2 months','fees':15000}
}
print(course)
print()
print(course['php'])
print()
print(course['php']['fees'])
print()

for i,j in course.items():           # important
    print(i,j['duration'],j['fees'])
    print()

course['java']['fees']=12000
print(course['java'])
print()

del course['php']['duration']
print(course['php'])
print()

# tuple
print('tuple')
r=(10,20,30,10,50) # digit doesnt repeat
print(r)
s=r[3]
print(a)
print()

t=len(r)
for a in range(t):
    print(a)
    print(r[a])
    print()

for b in r:
    print(b)
print()

# tuple functions
print(min(r))
print(max(r))
print(r.count(10))
print(r.index(30))
print(sum(r))
print()

# set
print('set')
h={20,10,40,30,50,10} # random indexing # digit doesnt repeat
print(h)
print()

for c in h:
    print(c)
print()

# set functions
print(set(r)) # converts to set
print()

h.add(80) # new no. , not list no.
print(h)
print()

print(h.pop()) # returns value
print(h)
print()

print(h.remove(50)) # doesnt returns value
print(h)
print()
# same
print(h.discard(80)) # doesnt returns value
print(h)
print()

print(h.clear()) # doesnt returns value
print(h) # retunrs as set even as {}
print()

h={10,20,30,40,50}
l={60,70,80,90,50} # 50 wont repeat
m={600,700,800,900} 
h.update(l,m) # can add more than two sets
print(h)
print()