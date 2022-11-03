import os
import time
import platform
# import jnr.python.functions.nirulabs
from jnr.python.functions import *
nirulabs.MyIP()
def mycode(cmd1,cmd2):
    print("Please wait, Clearining the screen.")
    time.sleep(2)
    os.system(cmd1)
    print("Please wait, Listin Files and dirs")
    time.sleep(2)
    os.system(cmd2)

if platform.system() == "Windows":
    mycode("cls","dir")
else:
    mycode("clear", "ls -ltr")
