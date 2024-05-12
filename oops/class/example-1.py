class Dog:
    def __init__(self, name, age): # __init__ is a special method that is called when an object is created.
        self.name = name
        self.age = age
        print(self.name)

    def bark(self): # A function within a class is called a method.
        self.name = "USA"
        self.state = "California"
        print(f"{self.name} says woof!")
        print(f"{self.state} says woof!")
        
# Creating an instance of the Dog class
my_dog = Dog("Buddy", 3)

# Accessing attributes and methods of the Dog class
# print(my_dog.name)  # Output: Buddy
# print(my_dog.age)   # Output: 3
my_dog.bark()       # Output: Buddy says woof!
# print(my_dog.bark.state) # Output: California
# print(my_dog.name)  # Output: USA
