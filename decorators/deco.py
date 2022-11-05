from nirulabs import myIP

def decor(func):
    def inner():
        print("Send person to Beauty parlour")
        print("Send person with Full Decoration")
    return inner

@decor      # This decor will take display() as input and outputs inner..
def display():
    print("Show person as it is: ")

display()
myIP()