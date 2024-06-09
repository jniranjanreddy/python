# class Test:
#     def m1(self, x):
#         print("{} - argument method" .format(x.__class__.__name__))

# t = Test()
# t.m1(10)      # int - argument method
# t.m1("Hello") # str - argument method
# t.m1(10.0)    # float - argument metho
# t.m1(True)    # bool - argument method


class parent:
    def Property(self):
        print("land + Gold Cash Power")

    def Marry(self):
        print("marry Appalamma")

class Child(parent):
    def Marry(self):
        super().Marry()
        print("Anupama")

t = Child()
t.Marry()