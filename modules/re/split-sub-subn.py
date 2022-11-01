import re
# Split Block
# text = "This is about python and python is very easy to learn python2 and python3 Python4"
# my_pat = "python[23]?"
# print(re.split(my_pat,text,maxsplit=0,flags=re.I))

# # sub - Block is used to replace the the given string.
# text = "This is about python and python is very easy to learn python2 and python3 Python4"
# my_pat = "python[23]?"
# print(re.sub(my_pat, 'jython', text, count=2, flags=re.I))

# subn - It will give the count of number of relpaced items.
text = "This is about python and python is very easy to learn python2 and python3 Python4"
my_pat = "python[23]?"
print(re.subn(my_pat, 'jython', text, flags=re.I))