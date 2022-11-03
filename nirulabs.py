"""
This is the main file for calling functions
"""
import os
# For findin IPaddress
def MyIP():
    coM = ('hostname -i')
    os.system(coM)
MyIP()