# # pickle library

# import pickle
# l={10,20,30,40}
# file=open('writedata.txt','wb')
# pickle.dump(l,file)
# file.close()



# json

# dictionary to json
import json
print()

print('dictionary to json :-')
print()

d={"course":"python", "fees":12000}
f=json.dumps(d) # converts to json format

print(type(d))  # dictionary
print(d)        # dictionary {' '}
print()

print(type(f))  # json (string)
print(f)        # json {" "}
print()
print()

# json to dictionary
import json
print()


print('json to dictionary :-')
print()

e='{"course":"python","fees":12000}'
h=json.loads(e) # converts to dictionary

print(type(e))  # json (string)
print(e)        # json {" "}
print()

print(type(h))  # dictionary
print(h)        # dictionary {' '}
print()

# read/write json
import json
print()

file=open("posts.json","r") # location
print()


print('whole list :-')
print()
x=json.loads(file.read()) # conversion
print(x) # converted to list cz of []
print()

print('all dictionaries :-')
print()
for a in x: # access all dictionaries from the list
    print(a)
    print()

print('all elements :-')
print()
for a in x: # access all dictionaries from the list
    print(a['id'],a['title'])
    print()