import re
str = "Is Python is it easy learn for learning is it hot now learn"
# my_pat = "^I[st]" 
my_pat = "\w$" # The dollar symbal is used to fetch a lase string.
b = re.findall(my_pat,str)
# print(re.findall(my_pat,str))
print(len(b)) # To check the count of the string.
