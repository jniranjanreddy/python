#!/usr/bin/env python3
class Test:
    def __init__(self):
        self.a = "Rama"
        self.b = "Sita"

    def m1(self):
        self.c = 30


t1 = Test()  # Oblect creation a,b will be added to Object
t1.m1()  # c will be added to Object
t1.d = 40  # d will be added to object
del t1.c,t1.d

# t2 = Test()
print("t1 Dict: ", t1.__dict__)
# print("t2 Dict: ", t2.__dict__)
print(t1.a)


# conList = t.__dict__
# print(conList)
# for s in conList.keys():
#     print("This is key: ", s)
# for s in conList.values():
#     print("This is Value: ", s)
