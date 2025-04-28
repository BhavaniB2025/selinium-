'''
Created on 13 Apr 2025

@author: Bhavani
'''
a={2,3}     
print(a)                              #to represent the set,we can denoted set as in {} flower bracket
print(type(a))                         # this is a set type

# creation of set
 
b={1, 2, 3, 4, 5}           #homogeneous data 
print(type(b))
print(b)

c={1, "abc", 4.27, True, 3+8j}   #heterogeneous data 
print(c)

#ACCESSING THE ELEMENTS USING INDEX
#print(c[4])
#print(c[-1])

#not modified for set

z={1,3,7,9,11}
#z[3]=7
print(z)    #not modified for tuple

#modification

b.add(6)      #adding elements in set by using add keyword
print(b)

b.update([1,2,3])   #adding multiple elements by using update keyword              
print(b)

b.add("d")
print(b)

b.update("d","e","f")
print(b)

b.discard(6)     #to remove the elements from set
print(b)

#iterate over a set in python

for n in b:        #fecting all elements fron the set
    print(n)
    
#finding elements
print(len(b))  
#print(b[6])        #not abel to find the element from the set

e={"bhavani","chitra","sandeepa","bhavani"}                    #set cannaot stores the duplicate values
f={"yogita","sanjana","shrelaxmi"}
print(e)
print(f)
print(e|f)     #union of set e and f
print(e&f)     #intersection of set e and f
set1={2,4,6,8,10}
set2={2,4,5,7,9}
g=set1.union(set2)
print(g)
h=set2.difference(set1)
print(h)



