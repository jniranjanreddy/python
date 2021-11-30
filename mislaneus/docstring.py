#!/usr/bin/env python3
import os
'''This is example for doc_string'''
print(__doc__)
print("This file name is:", __file__)
print("This is the Absolute path", os.path.abspath(__file__))
a = __file__
print(a)