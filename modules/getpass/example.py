#!/usr/bin/env python3
import getpass
"""
Two important Functions
getpass()
getuser()
getuser will fetch LOGNAME, USER, LNAME USERNAME by sequence
"""
# db_pass = getpass.getpass(prompt="Enter your Password: ")
# print(f"Entered password is: {db_pass}")
print(getpass.getuser())