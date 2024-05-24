# # Reverse
# a = [1,2,3,4]
# print(a[::-1])

# number = 123
# string_number = str(number)
# print(type(string_number))

################
def myPolindrome(x):
    string_number = str(x)
    if string_number == string_number[::-1]:
        print("Its polindrome")
    else:
        print("Its not palindrome")

myPolindrome(20002)
