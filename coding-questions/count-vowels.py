# use in
def volFunc(t): 
    myVowel = ["a", "e", "i", "o", "u"]
    # myText = "hello"
    count = 0
    for char in t:
        if char in myVowel:
            count += 1
    print(count)
volFunc("Hello")


# # not in 
# def volFunc(t): 
#     myVowel = ["a", "e", "i", "o", "u"]
#     # myText = "hello"
#     count = 0
#     for char in t:
#         if char not in myVowel:
#             count += 1
#     print(count)
# volFunc("Hello")

class volCount:
    # def __init__(self) -> None:
    # def __init__(self,t):
    #     self.t = t
    #     myVowel = ["a", "e", "i", "o", "u"]
    #     count = 0
    #     for char in t:
    #         if char in myVowel:
    #             count += 1
    #     print(count)
    def myFunc1(self,t):
        self.t = t
        # myVowel = ["a", "e", "i", "o", "u"]
        myVowel = "H"
        count = 0
        for char in t:
            if char in myVowel:
                count += 1
        print(count)        

obj = volCount()
obj.myFunc1("Hello")