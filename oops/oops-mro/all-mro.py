class A: 
    def m1(self):
        print("A Class Method")
class B(): pass
    # def m1(self):
    #     print("B Class Method")
    # def m2(self):
    #     print("M2 Class")
class C(A):
    def m1(self):
        print("C Class Method")
class D(B,C): 
    pass
        
d = D()
d.m1()
