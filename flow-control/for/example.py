#!/usr/bin/env python3
s = 'Sri Rama'
# ind = 0
# for i in s:

#     print(f"An indes is : {ind}, The charater is: {i}")
#     ind = ind + 1
# for x in range(5):
#     print('Welcome to python for loooooop')

# for x in range(21):
#     if x%2 == 0:
#         print(x)\
# list = [ 1, 2, 3, 4, 5]
# sum = 0
# for x in list:
#     sum = sum+x
# print(f"The sum is: {sum}") 
# print("The is sum of:", sum(list))
#======================================
# for each_list in ["Om", "Namah", "Shivah"]:
#     if "Om" in each_list or "Namah" in each_list:
#         print("Oh My God")
#     print(each_list)
index = 0
myInput = input("Enter a String: ")
for each_list in myInput:
    print(f"{each_list} --> {index}" )
    index=index-1
    