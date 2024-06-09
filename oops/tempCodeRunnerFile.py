class Pro_Test:
    def __init__(self):
        self._x = 10
    def m1(self):
        print(self.__x)

class Subtest(Pro_Test):
    def m2(self):
        print(self._x)

ts = Subtest()
ts.m1()
ts.m2()