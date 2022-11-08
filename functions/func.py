import os
import sys
import time
import platform
# sys.path.insert(0, r'/jnr/python')

# nirulabs.MyIP()
def mycode(cmd1,cmd2):
    print("Please wait, Clearining the screen.")
    time.sleep(2)
    os.system(cmd1)
    print("Please wait, Listing Files and dirs")
    time.sleep(2)
    os.system(cmd2)
    return None

if platform.system() == "Windows":
    mycode("cls","dir")
else:
    mycode("clear", "uname -a")

mycode("uname", "date")