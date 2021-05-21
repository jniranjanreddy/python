#!/usr/bin/env python3
import os
from os import path
#my_file = open("dirlist.txt", "r")
#content = my_file.read()
#print(content)

my_file = open("dirlist.txt", "r")
content_list = my_file.readlines()
for i in content_list:
    print(i)

