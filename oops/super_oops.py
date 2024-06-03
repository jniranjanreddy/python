class p:
    a = 10
def __init__(self):
    print("parrent Constructor")
    def m1(self):
        print("parent Instance Method")
    @classmethod()
    def m2(cls):
        print("Parent Class method")
    @staticmethod()
    def m3():
        print("Parent STatic method")
        

class c(p):
    def __init__(self):
        print("Child Constructor")
    def method1(self):
        print(super().a)
        super().m1()
        super().m2()
        super().m3()
        super().__init__()

c = c()
# c.m1()
c.method1()