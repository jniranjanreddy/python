class outer: # outer class
    def __init__(self) -> None:
        print("Outer Class")

    class inner:  # Inner class
        def __init__(self) -> None:
            print("I am inner class Object Creation")

        def m1(self):
            print("Inner method")

        class nested:  # Inner class
            def __init__(self) -> None:
                print("I am nested class Object Creation")
            @staticmethod    
            def m2():
                print("Its a Static method method")
            


outer().inner().nested().m2() # calling with Object refference
outer().inner().nested.m2()   # calling with Statis refference