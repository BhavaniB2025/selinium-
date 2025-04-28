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

print(c.remove("bhavani"))
print(c)
print(c.remove("chitra"))
print(c)

even_list=[]
for i in range(1,25):
    if i%2==0:
        even_list.append(i)
        print(even_list)
    
#list comprehention
even_list_comp=[i for i in range(1,25) if i%2==0]
print(even_list_comp)








