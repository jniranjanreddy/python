
def my_decorator(f):
    print("This is the decorator")  


@my_decorator
def mainFunc():
    print("This is the main function")