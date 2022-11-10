"""
To Generate a random object from List,Tuple,String...etc...
It will not work for set and Dictionary
"""
from random import *
# fruits = ['apple','banana','orange','mango','lemon']
# for i in range(10):
#     print(choice(fruits))

# alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# for i in range(10):
#     print(choice(alphabets))

digits = '0123456789'
for i in range(10):
    print(choice(digits), sep='-')