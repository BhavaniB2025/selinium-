'''
Created on 12 Apr 2025

@author: bhavani


'''
c=["bhavani","chitra","yogitha","sanjana","sandeep","vivek","manju"]

print(c)

c.append(1)
print(c)

(c.count("bhavani"))
c.extend(c)
print('e.extend(c):',c)

print(len(c))

print(c[10])
print(c[0])
print(c[7])

#c.index()
print(c.index('vivek'))

print(c.count("bhavani"),c.count("sandeep"))

print(c.index("bhavani"))

print('c--->',c)

print(c.pop(2))
print(c.pop(3))

print(c.remove("bhavani"),c.remove("manju"))
print(c)



