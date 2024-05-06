#!/usr/bin/env python3
import os
import platform
if platform.system()=="Windows":
    print("Windows OS detected")
    # os.system("clear")
else:
    print("Linux OS detected")
    os.system("sleep 2")