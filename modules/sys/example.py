#!/usr/bin/env python3
import sys
import os
# sys.exit(2) # This will exit python script and Return code is 2.
# print("Shivah Namah")
# print(sys.argv)
if len(sys.argv) != 3:
    print("Usage:")
    print(f"{sys.argv[0]} <Your required string> <lower|upper|Title>")
    sys.exit()

user_str = sys.argv[1]
user_action = sys.argv[2]

if user_action == "lower":
    print(user_str.lower())
elif user_action == "upper":
    print(user_str.upper())
elif user_action == "title":
    print(user_str.title())
else:
    print("Your action is Invalid, please select valid options")



