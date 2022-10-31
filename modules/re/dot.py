import re
"""Matches any single character except newline character"""
my_str = """eth0 eth1 eth2 eth3 eth44"""
my_pattern = "." # It will find for a two digits
print(re.findall(my_pattern,my_str))