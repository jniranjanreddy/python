import os
"""

# sys.path.insert(0, '/jnr/python/') # or export PYTHONPATH=’path/to/directory’
# Windows - SET PYTHONPATH=”path/to/directory”
"""


from nirulabs import myIP
def readFile():
    path = input("Enter file name to read: ")
    try:
        with open(path) as f:
            print(f.read())
            f.close()
    except Exception as e:
        print("Some Problem Reading files:", e)
    finally: 
        print("Hey, try and except block executed.")
if __name__=="__main__":
    readFile()
    myIP()