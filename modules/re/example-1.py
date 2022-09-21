#!/usr/bin/env python3
import re
str = "Abcd 4 computer  765 python 687 \computer ?"
#pattern = 'computer'
# pattern = r'[a-zA-Z]+'
# pattern = r'[0-9]+'
# pattern = r'[a-zA-Z0-9]+'
pattern = r'[computer]+' 
match=re.findall(pattern, str)
print(match)