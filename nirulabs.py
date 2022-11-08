#!/usr/bin/env python3
"""
!! DO NOT DELETE THE FILE !!
!! This is a Module for many Other scripts
This is the main file for calling function modules
Add below two line in your pythin script to import modules. 
import sys
sys.path.insert(0, '/jnr/python') 
"""
import os
# For findin IPaddress
def myIP():
    coM = ('hostname -i')
    os.system(coM)
    return None
if __name__=="__main__":
    myIP()

############ End of myIP simple Function
############ Begining of Decorator examples
import nirulabs,os
def decor1(func):
    def inner1():
        print("Decorator1 Execution")
    return inner1

def decor2(func):
    def inner2():
        print("Decorator2 Execution")
    return inner2

def decor3(func):
    def inner3():
        print("Decorator3 Execution")
        
    return inner3

@decor3
@decor2
@decor1 
def f():
    print(f"Original Function")
if __name__=="__main__":
    f()
############ End of Decorator examples
