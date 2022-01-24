#!/usr/bin/env python3
class Test:
    def __init__(self):
        print("The Object pointed: ", id(self))

t = Test()
print("The add of Object of t:", id(t))