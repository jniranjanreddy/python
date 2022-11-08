import nirulabs,os
def decor1(func):
    def inner1():
        print("Decorator1 Execution")
    return inner1

def decor2(func):
    def inner2():
        print("Decorator2 Execution")
    return inner2

def decor3(func):
    def inner3():
        print("Decorator3 Execution")
        
    return inner3

@decor3
@decor2
@decor1 
def f():
    print(f"Original Function")

if __name__=="__main__":
    f()

