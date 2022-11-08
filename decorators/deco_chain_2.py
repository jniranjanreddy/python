def decor2(func):  #func is replaced with main() function
    def inner2():  # Nested function 
        x = func() # calling main function
        return 2*x 
    return inner2

def decor1(func): # func is replaced with main() function
    def inner1():
        x = func()
        return x*x
    return inner1

@decor2 # input is @decor1  
@decor1 # input is mail(), 
def main():
    return 20

print(main())