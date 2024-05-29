class p:
    def m1(self):
        print("Parent Class Method")
class c(p):
    def m2(self):
        print("Child Class Method")

c = c()
c.m1()
c.m2()

