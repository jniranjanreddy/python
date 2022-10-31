import re
#\b Empty string at the begining or end of word.
#\B Not empty string at the begining or end of word

#\b
# text = "isa python and learn itlearn pis easy tolearn" 
# my_pat = r"\blearn\b"

#\B
# text = "isa python and learn itlearnis pis easy tolearn" 
# my_pat = r"\Blearn\B"
# print(re.findall(my_pat,text))

#\t Matches tab
# text = 'isa python  and  learn \n itlearnis pis easy tolearn' 
# my_pat = r"\t"
# print(re.findall(my_pat,text))

#{2}
# text = 'This is a pythonnn and aaa python' 
# my_pat = r"\ba{3}\b"
# print(re.findall(my_pat,text))

#{2,4}
# text = 'This is a pythonnn and aaaaaa  python aa aaa aaaa aaaaaaaaa' 
# my_pat = r"a{2,6}\b"
# print(re.findall(my_pat,text))

# #{2,} Minimum 2 and maximum  may be any...
# text = 'This is a pythonnn and aaaaaa  python aa aaa aaaa aaaaaaaaa' 
# my_pat = r"a{2,6}\b"
# print(re.findall(my_pat,text))

# # + one or more 
# text = 'This is a pythonnn and aaaaaa  python aa aaa aaaa aaaaaaaaa' 
# my_pat = r"a{1,6}\b"
# print(re.findall(my_pat,text))

# # * Zero or n=more times 
# text = 'xaz xaaz xxaaz is a pythonnn and az  aaaaaaaz python aa aaa aaaa aaaaaaaaa' 
# my_pat = r"x+a"
# print(re.findall(my_pat,text))

# ? Once or none 
# text = 'xz xaz xaaz xoaz rat rot xaaaaaaaaaaaz is a pythonnn'
# my_pat = r"ro?a?t"
# print(re.findall(my_pat,text))

# #  re.I Ignore case senstive
# text = 'this is a string, THIS is a string' 
# my_pat = r"THIS"
# print(re.findall(my_pat,text,re.I))

# #  re.M Multiline String..
# text = """this is a first line, 
# THIS is second line
# this is third line
# This is forth Line"""
# my_pat = r"^this"
# print(re.findall(my_pat,text,re.M|re.I))

#  re.M Multiline String..
text = """this is a first line, 
THIS is second line
this is third line
This is forth Line"""
my_pat = r"^this"
print(re.findall(my_pat,text,re.M|re.I))