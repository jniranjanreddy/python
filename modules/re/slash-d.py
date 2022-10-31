import re
# my_str = "1This22 is 1 simple and b it 11 is python _ # 192.168.9.1 - ?"
my_str = "python0 python1 python2 3python4"
# my_pattern = "\d" # It will find for a single digit
# my_pattern = "\d\d" # It will find for a two digits
my_pattern = "python" # It will find for a two digits
print(re.findall(my_pattern,my_str))