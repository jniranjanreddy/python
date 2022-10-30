#!/usr/bin/env python3
import re
"""
search   re.researh(pattern,text)
match    re.match(pattern,text)
finditer re.finditer(pattern,text)
findall  re.findall(pattern,text)
split
sub ..etc
"""
my_str = "This is simple and it is easy"
# my_pattern = "i[st]"
my_pattern = "ab"
print(re.findall(my_pattern,my_str))
print(len(re.findall(my_pattern,my_str)))
