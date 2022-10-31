import re
"""Matches any single character except newline character"""
my_str = """This is DB IP 192.168.100.100  192.168.100.101  192. 1000 0000000 """
# my_pattern = "\d\d\d.\d\d\d.\d\d\d.\d\d\d" # It will find for a two digits
my_pattern = "\d\d\d\.\d\d\d\.\d\d\d\.\d\d\d"
print(re.findall(my_pattern,my_str))