from nirulabs import myIP

def decor(func):
    def inner(a,b):
        print(f"Total of {a} + {b} is: ", a+b)
        print("Send person with Full Decoration")
        func(a,b)
        myIP()
    return inner

@decor      # This decor will take display() as input and outputs inner..
def display(a,b):
    print(f"Multiply of {a} and {b} is:", a*b)

display(2,4)
