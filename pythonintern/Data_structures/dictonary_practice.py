'''
Created on 12 Apr 2025

@author: bhavani

''
Dictonary :collection of key values pairs
1.Empty dictionary can be created
2.dictionary doesn't allow duplicates elements
3.dictionary allows duplicate values but not keys
dict_name={key1:value1, key2:value2, key3:value3...}
'''


stds={1:"bhavani",2:"chitra",3:"sanjana",4:"sandeep",5:"yogitha"}
print(stds)
print(stds)

d1={}
print(d1)
print(type(d1))

d3=dict.fromkeys([1,2,3,4],"xyz",)
print(d3)
d4=dict.fromkeys("abc", 1)
print(d4)
d5={1:"bhavani",2:"chitra",3:"sanjana",4:"sandeep",5:"yogitha"}
print(d5)
iquest={"bhavani":1,"chitra":2}
print(iquest["bhavani"])
print(d5[1])
print(stds.keys())
print(stds.items())

for ele in stds:
    print(ele)

for a in d5:
    print(a)              # using for loop we call 'a' has the fetching element and to print elements
    
for ele in d5.values():
    print(ele)           #fetching elements with for loop
    

print(d5)
d5[3]="manju"                  #modifing sanjana as manju
print(d5)

d6=d5.copy()
print(d6)                      #coping d5 elements and storing d6 

print(d5.items())      #calling items of d5

print(d5.pop(4))
print(d5)             #pop -->removing one elements form d5

print(d5.popitem())
print(d5)               #pop item removing last item in d5

d5.update(d3)
print("updated d4 as----->",d3)     #updating d5 dictionary to d3

'''
num1=10
num2=20
print(num1)
print(num2)
add=num1+num2
print("addion of num1 and num2=",add)
'''

num =11
num =22
num1=num2=33
print(num1)











    
    
    
    
    
    
    
    
   

    
    
    
    
    
    
    
    








