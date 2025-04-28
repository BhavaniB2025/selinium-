'''
Created on 2 Apr 2025

@author: KATWA

#from itertools import count
'''
'''
count=5
while count>0:
    print("hi world")
    count=count-1
    
    
# looping statement  
#while loop- repeated actions
count=0
while count<=100:
    if count == 50:
        count+=1
        continue 
    print(count)
    count+=1
    

#for loop - To iterate collections or range

print (range(10))   

    
    
print(range(10))
'''
'''

for n in range(1,50):
    print(n)    
'''

for n in range(1,100):
    if n==50:
        continue
    print(n)
  
# for even number
'''
for n in range(1,100):
    if n%2==0:
        print(n)
    
#for odd number
for n in range(1,100):
    if n%2==1:
        if n==11:       #To check the condition 
            continue
        print(n)
    
for n in range(1,100,2):
    print(n) 
    
    
    
    
    
    
*                *****
**               ****
***              ***
****             **
'''
'''

for n in range(1, 6):
   
    for m in range (n): 
        print("*", end=" ")
        print()

'''

for n in range(5,0,-1):
    
    for m in range (n):
        print("*", end=" ")
        
    print()


        
for n in range(1, 6):
    
    
    for m in range(6-n):
        print(" ", end="")
    
    for i in range(n):
        print("*", end=" ")
        
    print()
    

for n in range(1, 6):    
    
    
    for m in range(6-n):
        print(" ", end="")
        
    for i in range(n):
        print("1", end=" ")   
        
    print()
  

for i in range(1,6):
    print("*")
    
    print("*",end=" ")
    
    print(" *",  end="  ")
'''
    *
   **
  ***
 ****
*****
'''
for j in range(5):
    for k in range(5-j):           #j represents row  ,switching lines
        print(" ",end=" ")
    
    for i in range(j):
        print("*", end=" ")
    print()
        
for j in range(5):
    for k in range(5-j):           #j represents row  ,switching lines
        print(" ",end=" ")
        
    for i in range(j):
            print("*", end=" ")
            print()
    
        

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
        
        
        
        
       
       
       
       
       
       
       
       
       
        