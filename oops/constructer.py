#!/usr/bin/env python3
class Test:
    def __init__(self):
        print("COnstructor")
    
    def m1(self,x):
        print("The x value is: ", x)
t = Test()
t.m1(10)