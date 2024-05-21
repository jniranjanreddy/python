#!/usr/bin/env python3
class Test:
    schoolname = "Durgasoft"  # Static Variable
    a = 10  # Static Variable
    print("Static Variable: ", a)
    
    def __init__(self):
        Test.a = 20  # Instance Variables # Inside Constructor
        print("Instance Variable: ", Test.a)

    def m1(self):
        Test.a = 30  # Instance Variables
        print("Instance", Test.a)

    @classmethod  # Class Method
    def m2(cls):
        cls.a = 40  # Static Variable
        print("Class Method: ", cls.a)
        # Test.a = 50

    @staticmethod  # Static Method
    def m3():
        Test.a = 60  # Static Variable
        print("Static Method: ", Test.a)
.
t = Test()
t.m1() # m1 method
Test.m2() # m2 method
Test.m3() # m3 method
Test.a = 70  
print(t.a)  