class Test:
    a = []  # Static Variable
    @classmethod  # Class Method
    def m1(cls):
        del cls.a
        # print("Class Method: ", cls.a)

# Test.m1()    
# print(Test.__dict__)
# print(object.__dict__)

a = int(input("Enter the number of elements: "))
for i in range(a):
    Test.a.append(i)
t = Test()
# del t.a
print(Test.a)
# print(Test.__dict__)