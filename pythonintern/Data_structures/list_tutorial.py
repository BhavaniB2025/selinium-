'''
Created on 6 Apr 2025

@author: Bhavani
'''

#List :

#1.creation of list

a=[]
print(type(a))

a={1}
print(type(a))

a=()
print(type(a))

# creation of list
 
b=[1, 2, 3, 4, 5]  #homogeneous data structure
print(type(b))
print(b)

c=[1, "abc", 4.27, True, 3+8j]    #heterogeneous structure
print(c)

d=list(range(1,20))
print(d)

#ACCESSING THE ELEMENTS USING INDEX
print(c[4])
print(c[-1])

#not modified for set

z=(1,3,7,9,11)
#z[2]=22
print(z)    #not modified for tuple

print(c[::])
print(d[3:9])

#slicing operator-list_name[start : stop : step] --->index
#

print('d[::]-->', d[::])
print('d[3:9]-->', d[3:9])
print('d[:12]-->', d[:12])
print('d[6:]-->', d[6:])
print('d[-12:-6]-->', d[-12:-6])
print('d[::2]-->', d[::2])
print('d[::-1]-->', d[::-1])
print('d[-12:-6:-1]-->', d[-12:-6:-1])

#accessing for loops

#for loop:
print("====for loop===")
for ele in c:
    print(ele)
    
#====while loop====
i=0
while i<5:
    print(c[i])
    i+=1
    
    print("====while loop====")
    print(c[0])
    print(c[1])
    print(c[2])
    print(c[3])

    
for n in d:
    if n%2==1:
        print(n)
        
        
e=["Bhavani", "chithra","sandeep","yogitha","vivek","sanjana"]
for g in e:
    if 'a' in g:
        print(g)
        
        
h=["bhavani", "chitra", "sandeep", "sanjana", "vivek" ,"yogitha", "manju"]
h.append("vinu")
print(h)

h.insert(4,"padma")
print(h)

f=[15,30,22,10,60,13]
for n in f:
    if n%2==1:
        print(n**2)
        
j=[]
k=[15,30,22,10,60,13]
for n in k:
    if n%2==1:
        j.append(n**2)
print(j)
        

city={530068:"bangalore",570001:"Mysore",573201:"hassan",571401:"mandya",574142:"managalore",573134:"sakaleshpura",577101:"Chikmagalore",643001:"ooty",571234:"kushalnagara",571201:"madikeri"}
for s in city:
    print(s)