import re

text = "This is for python there ate two major version python2 and python3, in future for python4"
pat = r"\bpython[\d]?\b"
match_ob = re.search(pat,text)
# my_search = re.findall(pat,text)
print(match_ob)