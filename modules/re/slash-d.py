import re
# matches decimal digit 0-9
# my_str = "1This22 is 1 simple and b it 11 is python _ # 192.168.9.1 - ?"
my_str = """
eth0 eth1 eth2 eth3 eth44 """
# my_pattern = "\d" # It will find for a single digit
# my_pattern = "\d\d" # It will find for a two digits
my_pattern = "eth[\d]" # It will find for a two digits
print(re.findall(my_pattern,my_str))