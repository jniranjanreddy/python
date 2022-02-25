#!/usr/bin/env python3
import string
a = "Rama"
print("+".join(a))
print(a.upper())
print(a.lower())
# for i in range(1, 10):
#     if(i % 2 == 0):
#         # print("{}".format(number))
#         print(i)    
# for i in range(1,10):
#     print(i, end=' ')

print("Alphabet from a-z:")
for letter in string.ascii_uppercase:
   print(letter, end =" " )