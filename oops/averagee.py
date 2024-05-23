# class Test:
#     @staticmethod  # Static Method
#     def average(List1):
#         result = sum(List1) / len(List1)
#         print("Average of List: ", result)

# t = Test()

# List1 = [ f for f in range(4)]
# t.average(List1)  # Static Method

class Test:
    def m1(self, number) -> None:
        self.number = number 
        print("local variable", self.number)

    # def m2(self):
    #     # a = 20
    #     print("local variable", self.number)

t = Test()
t.m1(10)
# t.m1()
# t.m2()