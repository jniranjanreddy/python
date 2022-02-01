#!/usr/bin/env python3
class Test:
    a = 10
    def __init__(self):
        Test.b = 20
    def m1(self):
        Test.c = 30
    @classmethod
    def m2(cls):
        cls.d = 40
        Test.e = 50
t = Test()
t.m1()
t.m2()
Test.g = 70
print(Test.__dict__)