"""
This is the main file for calling functions
"""

# For findin IPaddress
def MyIP():
    coM = ('hostname -i')
    os.system(coM)
MyIP()