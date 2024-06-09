# class Test:
#     def __init__(self):
#         self.__x = 10 # Private variable

#     def __m1(self): # Private Method
#         print("Private Method")

#     def m2(self):
#         print(self.__x)
#         self.__m1()

# t = Test()
# t.m2()
# print(t._Test__x) ## __x --> _Test__x # Its called name mangling

## Protected variables or Methods.
 # x = 10 # public 
 # __x = 10 # Private
 # _x = Protected

class Pro_Test:
    def __init__(self):
        self._x = 10
    def m1(self):
        print(self._x)

class Subtest(Pro_Test):
    def m2(self):
        print(self._x)

ts = Subtest()
ts.m1()
ts.m2()
