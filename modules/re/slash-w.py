#!/usr/bin/env python3
import re
"""
\w - matches any single letter, digit or underscore.
\W - Matches any character not part of \w
search   re.researh(pattern,text)
match    re.match(pattern,text)
finditer re.finditer(pattern,text)
findall  re.findall(pattern,text)
split
sub ..etc
"""
# my_str = "This is simple and b it is python"
# my_pattern = "i[st]"    # It will find for is and it
# my_pattern = "[abcd]"    #  It will print all characters between a to d
# my_pattern = "[a-d]"    # It will print all characters between a to d.
# print(len(re.findall(my_pattern,my_str)))
# my_pattern = "\w"
# my_pattern = "\w\w"
# my_pattern = "\w\w\w"  Prints all characters belons to \w, a to z and _
# my_pattern = "\W"      #Matches all characters with doesnt belons to small w (\w) _ space
my_str = "This is simple and b it is python _ # - ?"
my_pattern = "\W"
print(re.findall(my_pattern,my_str))








