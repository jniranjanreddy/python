class A: 
    def m1(self):
        print("A Class Method")
class B():
    def m1(self):
        print("B Class Method")
class C(A):
    def m1(self):
        print("C Class Method")
class D(B,C): 
    pass
        
d = D()
d.m1()