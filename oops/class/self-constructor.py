# class Test:
#     def __init__(self):
#         print('Constructor called')
        
#     def m1(self, x):
#         print('Method called', x)

# t = Test()
# t.m1(10)                       

class Test:
    a = 10
    def __init__(self):
        Test.a = 20

print(Test.a)