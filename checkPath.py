#!/usr/bin/env python3
import os
from os import path
import pathlib
import re
import shutil

#my_file = open("dirlist.txt", "r")
#content_list = my_file.readlines()

with open('dirlist.txt') as content_list:
    for i in content_list:
        if path.exists(i):
            print("File exist")
        else:
            #print(i)
            os.makedirs(i)
            print("File not exist")