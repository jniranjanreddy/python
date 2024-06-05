class MMethods:
    def m1(self, *args):
        # print("variable length Arguments", len(args))
        print("variable length Arguments", sum(args))

t = MMethods()
t.m1()         
t.m1(10)       
t.m1(10,10)    
t.m1(10,10,10)