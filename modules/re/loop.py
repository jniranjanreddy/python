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
ant
'''
# pattern = r'.[^ ]+'
# pattern = r'.*i'
# pattern = r'.*ie'
#pattern = 'ch'
pattern = r'\b[aeiou].+\b'
match=re.findall(pattern, str)

# print(match)
for m in match:
    print(m)