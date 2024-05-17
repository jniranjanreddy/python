# class Test:
#     def m1(self):
#         print('Method called', id(self))

# t = Test()
# t.m1()
# print(id(t))


class Test:
    def __init__(self):
        print('no-Constructor')

    def __init__(self, x):
        print('single Constructor')
# t = Test()
t = Test()
t1 = Test(10)

