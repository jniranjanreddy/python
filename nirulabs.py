#!/usr/bin/env python3
"""
This is the main file for calling functions
Add below two line in your pythin script to import modules. 
import sys
sys.path.insert(0, '/jnr/python') 
"""
import os
# For findin IPaddress
def myIP():
    coM = ('hostname -i')
    os.system(coM)
    return None

if __name__=="__main__":
    myIP()