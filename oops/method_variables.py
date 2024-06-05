class myMethod:
    def m1(self, a = None, b = None, c = None):
        if a is not None and b is not None and c is not None:
            print("Three arguments methos")
        elif a is not None and b is not None:
            print("Two argument method")
        elif a is not None:
            print("One argument Methos")
        else:
            print("No Argument methods")

t = myMethod() # 
t.m1()         # No Argument methods
t.m1(10)       # One argument Methos
t.m1(10,10)    # Two argument Methos
t.m1(10,10,10) # Three argument Methos
