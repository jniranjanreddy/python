#!/usr/bin/env python3
import re
str='''
apple
banana
orange 
peach
avocado
cherries
chennai
'''
# pattern = r'.[^ ]+'
# pattern = r'.*i'
# pattern = r'.*ie'
pattern = r'.*ies'
match=re.findall(pattern, str)

# print(match)
for m in match:
    print(m)