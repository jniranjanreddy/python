class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        self.name = "USA"
        self.state = "California"
        print(f"{self.name} says woof!")
        
# Creating an instance of the Dog class
my_dog = Dog("Buddy", 3)

# Accessing attributes and methods of the Dog class
print(my_dog.name)  # Output: Buddy
print(my_dog.age)   # Output: 3
# my_dog.bark()       # Output: Buddy says woof!
print(my_dog.state) # Output: California
print(my_dog.name)  # Output: USA
