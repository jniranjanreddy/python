class outer: # outer class
    def __init__(self) -> None:
        print("Outer Class")

    class inner:  # Inner class
        def __init__(self) -> None:
            print("I am inner class Object Creation")

        def m1(self):
            print("Inner method")

# # One way of calling..
# o = outer()    # creating outer Object
# i = o.inner()  # Creating Inner Object

# # Another way of calling..
# i = outer().inner() # Combining bith inner and outer
# i.m1()         # This will call inner Method

# print(i.m1())

outer().inner().m1() # commining all together.