import os
import sys
sys.path.insert(0, '/jnr/python')
from nirulabs import myIP
def readFile():
    path = input("Enter file name to read: ")
    try:
        with open(path) as f:
            print(f.read())
            f.close()
    except:
        print("Some Problem Reading files")
if __name__=="__main__":
    readFile()
    myIP()