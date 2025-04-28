'''
Created on 14 Apr 2025

@author: bhavani

'''
age=26                         #declaring the element
name="bhavani"                 #declaring string
print(name)
print("name:",name)            #printing the name of string
nick_name=" "                  #declaring the empty string
print("nick_name:",nick_name)  #printing nick_name
print(type(nick_name))         #printing type --it creates the class
print("bhavani:",age)          #printing  the name and age 

#accessing the element
print(name[0])                 #printing the 1st letter os name what ever in the 0Th place

#Accessing by the for loop
print("====accessing the for loop======")
for letter in name:
    print(letter)

#Accessing using slicing operator
print("=====accessing using slicing opertor=====")
print(name[1:4])                   
#printing the stating  position  means 1st of string name and stops in 3rd position of string
print(type(name[1:4]))   #printing the class string

adress="""IQUEST

hebbal industrial area,

mysore
"""
print(adress)
#modification

name.replace('v','s')       #not replacing the letter
print(name)
modified_name=name.replace('v','s')
print("name", name)
print("modified_name:", modified_name)

print(name.capitalize())  #1st letter of character is capitalized,if we have space in 1st letter then it will not 
print(adress.casefold()) #is going to change whatever adress we gave as upper case to lower case
print(name.count('bhavani',))
print(name.upper())     #changes into upper case
print(name.find('v'))    #finds where the letter is present
print(name.index('h'))
#print(name.isa1num()) 
print(name.split())
name_list=["my","name","is","bhavani"]
name_sentence='   '.join(name_list)
print(name_sentence) 
print(name.isnumeric())     #it check the condition whether given statement contains any numbers
print(name.isalpha())





