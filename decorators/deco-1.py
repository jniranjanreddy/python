
from nirulabs import myIP

def decor(func):
    print("Send person to Beauty parlour")
    print("Send person with Full Decoration")
    return inner

def inner():
    print("Hey This is Inner")

@decor      # This decor will take display() as input and outputs inner..
def display():
    print("Show person as it is: ")

display()
myIP()