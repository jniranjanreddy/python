#!/usr/bin/env python3
import re
str = '''
dfshj@gmail.com
3ytgdy.56
aniranjan@yahoo.com
hfg123h@com
hello@gmail.com user@gmail.com
'''
pattern = r'[a-z]+[0-9]*[a-z]*@[a-z]+\.com'
match=re.findall(pattern, str)
for m in match:
    print(m)