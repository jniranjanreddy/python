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
text = 'This is a pythonnn and aaaaaa python aa aaa aaaa' 
my_pat = r"\ba{2,6}\b"
print(re.findall(my_pat,text))


