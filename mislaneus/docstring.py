#!/usr/bin/env python3
import os
import test
'''This is example for doc_string'''
#print(__doc__)
#print("This file name is:", __file__)
#print("This is the Absolute path", os.path.abspath(__file__))
#a = __file__
#print(a)
DEV = 'dev'
ENV_NAME = os.environ.get('M2_HOME') or DEV
print(ENV_NAME)
print(test.a)