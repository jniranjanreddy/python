class Student: 
    """This is a class for student.
       A Function within a Class is called Method.
    """
    # variables ---> Properties/attributors
    # methods --> Methods/Actions/Behavious
    def __init__(self): # __init__ is a special method that is called when an object is created.
        self.name = "Durga"
        self.age = 20
        self.section = "A1"

    def talk(self):
        print("Hello, my name is", self.name)
        print("I am", self.age, "years old")
        print("I am in section", self.section)
MyObject = Student() # Creating an object of the class Student

print(MyObject.name) # Accessing the properties of the object
print(MyObject.age) # Accessing the properties of the object
print(MyObject.section) # Accessing the properties of the object
MyObject.talk() # Calling the method talk() of the object


#print(Student.__doc__) # __doc__ is a special attribute that contains the docstring of the class
# help(Student) # This will print the docstring of the class