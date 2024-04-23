import re

input_string = "The quick brown fox jumps over the lazy fox, fox, fox."
pattern = "fox"
replacement = "cat"

new_string = re.sub(pattern, replacement, input_string)
print(new_string)


import re
str = "Hello I a Python Programmer"
my_pat = "Python"
replacement = "Java"
new_str = re.sub(my_pat, replacement, str)
print(new_str) # Hello I a Java Programmer

