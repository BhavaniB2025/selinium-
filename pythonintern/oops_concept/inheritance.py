'''
Created on 7 May 2025

@author: bhavani
'''
class Grandfather:
    def gf_method(self):
        print("this is grand father method")                                                             
        
class mother:
    def m_method(self):
        print("this is a mother method")
        
class father:                                                        
    def f_method(self):
        print("this is a father method")
        
class child:
    def c_method(self):
        print("this is a child method")
        
amma=mother()
amma.m_method()         
paapu=child() 
paapu.c_method()                                                     
print("this is a child class")                                                                                     