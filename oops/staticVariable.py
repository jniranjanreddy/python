#!/usr/bin/env python3
class StaticVar:
    a = 10
    def __init__(self):
        StaticVar.b = 20
    def m1(self):
        StaticVar.c = 30
# print(StatiVar.__dict__)
t = StaticVar()
t.m1()
print(t.a,t.b,t.c)
