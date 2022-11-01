import re

# text = """
# This is for python2 
# there ate two major version python2
# and python3 in future for python4
# """
# This block is for search
'''
pat = r"\bpython[23]?\b"
match_ob = re.search(pat,text)
# my_search = re.findall(pat,text)
if match_ob:
    print("Match from your pattern:", match_ob.group())
    print("Starting Index: ", match_ob.start())
    print("Ending Index: ", match_ob.end()-1)
    print("length: ", match_ob.end()-match_ob.start())
else:
    print("No Match Found..")
'''

#This block is for match
text = """python 
there ate two major version python1
hey this and python2 
in future for python3
"""
pat = r"\bpython[23]?\b"
# print(re.findall(pat,text))
# print(re.match(pat,text))
match_ob = re.search(pat,text)
# my_search = re.findall(pat,text)
if match_ob:
    print("Match from your pattern:", match_ob.group())
    print("Starting Index: ", match_ob.start())
    print("Ending Index: ", match_ob.end()-1)
    print("length: ", match_ob.end()-match_ob.start())
else:
    print("No Match Found..")
