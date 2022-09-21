#!/usr/bin/env python3
import os

#os.remove("test001")

if os.path.exists("test001"):
   os.remove("test001")
else:
   print("File Doesn't exist")


