# Interview Questions.

## What is Python? Describe some of its key features.
Python is a high-level, interpreted programming language known for its simplicity and readability. Key features include dynamic typing, automatic memory management (garbage collection),
extensive standard libraries, and support for multiple programming paradigms (procedural, object-oriented, and functional).

## What are the differences between Python 2 and Python 3?
Python 2 is legacy and no longer maintained since January 1, 2020. Python 3 is the current version. Major differences include print statement (Python 2) vs. print function (Python 3),
integer division behavior, Unicode support, and syntax changes like xrange() being replaced by range().

## How do you comment out multiple lines of code in Python?
You can use triple quotes (''' or """) to comment out multiple lines of code.

## What is PEP 8? Why is it important?
PEP 8 is the official style guide for Python code. It provides guidelines and best practices to enhance code readability and maintainability. Following PEP 8 improves code consistency across projects and makes it easier for developers to understand each other's code.

## Explain the differences between lists, tuples, and dictionaries in Python.
Lists are mutable sequences, tuples are immutable sequences, and dictionaries are key-value pairs. Lists and tuples can store heterogeneous data types,
while dictionaries store data as key-value pairs for fast retrieval.

## What is a generator in Python? How is it different from a list?
A generator in Python is a special type of iterator that generates values on-the-fly using the yield keyword. Generators save memory by producing values lazily, 
while lists store all elements in memory at once.

## What is the purpose of the __init__ method in Python classes?
The __init__ method is a constructor in Python classes. It initializes instance variables when an object of the class is created.

## How do you handle exceptions in Python?
Exceptions in Python are handled using try-except blocks. Code that might raise an exception is placed inside the try block, and the handling code is placed inside the except block.

## Explain the difference between == and is in Python.
The == operator checks for equality of values, while the is operator checks for identity (whether two variables refer to the same object in memory).

## What is a lambda function? When would you use one?
A lambda function is an anonymous function defined using the lambda keyword. It is used for short, simple functions where defining a full function using def would be overkill.
Lambda functions are often used in conjunction with functions like map(), filter(), and reduce().

## How do you open and read a file in Python?
You can open and read a file in Python using the open() function with the appropriate mode ('r' for reading). For example:

with open('filename.txt', 'r') as file:
    data = file.read()

## What is the difference between append() and extend() methods in Python lists?
The append() method adds a single element to the end of a list, while the extend() method adds all elements of an iterable (such as another list) to the end of the list.

## How do you remove duplicates from a list in Python?
You can remove duplicates from a list in Python using several methods. One common way is to convert the list to a set, which automatically removes duplicates due to its property of containing only unique elements.
Then, you can convert it back to a list if necessary.

## Explain the concept of list comprehension in Python.
List comprehension is a concise way to create lists in Python. It allows you to generate lists by applying an expression to each item in an iterable, optionally including a conditional to filter items.
It has the syntax [expression for item in iterable if condition].

## What are decorators in Python? How do you use them?
Decorators are functions that modify the behavior of other functions or methods. They allow you to add functionality to existing functions without modifying their code directly.
Decorators are commonly used to add logging, authentication, or caching to functions. They are implemented using the @decorator_name syntax before the function definition.

## What is the purpose of __name__ == "__main__" in Python scripts?
This conditional statement is used to determine whether a Python script is being run as the main program or being imported as a module into another script. It allows you to write code that will only be executed if the script is run directly, not when it's imported as a module.

## Explain the difference between global and local variables in Python.
Global variables are declared outside of any function and can be accessed from any part of the program. Local variables are declared within a function and can only be accessed within that function's scope.

## What is the purpose of the super() function in Python?
The super() function is used to call methods of a superclass from a subclass. It is commonly used to invoke the superclass's constructor (__init__ method) within the subclass's constructor to initialize inherited attributes.

## How do you create a virtual environment in Python?
You can create a virtual environment in Python using the venv module. First, navigate to the desired directory in your terminal, then run python -m venv env_name to create a virtual environment named env_name.
Finally, activate the virtual environment using source env_name/bin/activate on Unix-like systems or env_name\Scripts\activate.bat on Windows.

## Explain the difference between iter() and next() functions in Python.
The iter() function is used to create an iterator object from an iterable (such as a list or tuple). The next() function is used to retrieve the next item from an iterator.
When there are no more items, it raises the StopIteration exception.

## What are Python decorators used for?
Python decorators are used to modify the behavior of functions or methods. They allow you to add functionality to existing functions without modifying their code directly.
Decorators are commonly used for tasks such as logging, caching, and authentication.

## How do you convert a string to lowercase in Python?
You can convert a string to lowercase in Python using the lower() method. For example:

python
Copy code
string = "Hello World"
lowercase_string = string.lower()
print(lowercase_string)  # Output: hello world

## What is the purpose of the os module in Python?
The os module in Python provides functions for interacting with the operating system. It allows you to perform tasks such as file and directory operations,
process management, and environment variable manipulation.

## Explain the purpose of the __doc__ attribute in Python.
The __doc__ attribute in Python is used to access the documentation string (docstring) of a function, method, class, or module. It is a string literal that is the first statement in the body of the function,
method, class, or module, and it provides documentation about its purpose and usage.

## Explain the difference between static, class, and instance methods in Python.
Static methods are defined using the @staticmethod decorator and can be called on the class itself or an instance of the class. They do not have access to the instance or class variables.
Class methods are defined using the @classmethod decorator and take the class (cls) as the first parameter. They can access and modify class-level variables.
Instance methods are regular methods defined within a class and take the instance (self) as the first parameter. They can access and modify instance variables.

## How do you sort a dictionary by value in Python?
You can sort a dictionary by value in Python using the sorted() function with a custom key function that sorts based on the dictionary values. For example:

python
Copy code
my_dict = {'a': 3, 'b': 1, 'c': 2}
sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print(sorted_dict)  # Output: {'b': 1, 'c': 2, 'a': 3}

## What is the purpose of the __slots__ attribute in Python classes?
The __slots__ attribute in Python is used to limit the attributes that can be created on instances of a class. It can improve memory usage and performance by preventing the dynamic
creation of attributes at runtime.

## Explain the concept of duck typing in Python.
Duck typing is a programming concept in Python where the type or class of an object is determined by its behavior (methods and properties) rather than its explicit type or inheritance hierarchy.
It emphasizes the importance of what an object can do (its interface) rather than what it is (its type).

## What is the purpose of the collections module in Python?
The collections module in Python provides specialized container datatypes that are alternatives to the built-in container types (dict, list, set, and tuple). For example, Counter is used for counting hashable objects, defaultdict is a subclass of dict that provides default values for missing keys, and namedtuple is used to create tuple subclasses with named fields.

## What is the difference between a shallow copy and a deep copy in Python?
A shallow copy creates a new object, but does not recursively copy the objects contained within the original object. As a result, changes to mutable objects inside the original object will affect the copied object. A deep copy, on the other hand, creates a completely new object with its own copies of the objects contained within the original object, recursively.

## How do you handle multi-threading in Python?
Multi-threading in Python can be achieved using the threading module. You can create a new thread by subclassing the Thread class and overriding the run() method, or by passing a target function to the Thread constructor. However, due to the Global Interpreter Lock (GIL), multi-threading in Python is not suitable for CPU-bound tasks, but can be useful for I/O-bound tasks.

## What is the purpose of the enumerate() function in Python?
The enumerate() function in Python is used to iterate over a sequence (such as a list or tuple) while keeping track of the index of each item. It returns an iterator that yields tuples containing the index and value of each item in the sequence.

## Explain the use of the with statement in Python.
The with statement in Python is used to wrap the execution of a block of code with methods defined by a context manager. It ensures that certain operations are properly performed, such as opening and closing files, acquiring and releasing locks, and connecting and disconnecting from databases. It is commonly used with file I/O operations to automatically close files when done.

## What is the purpose of the zip() function in Python?
The zip() function in Python is used to combine multiple iterables (such as lists, tuples, or strings) into a single iterator of tuples. Each tuple contains elements from each of the input iterables, aligned by their position.

## Explain the concept of list comprehension in Python.
List comprehension is a concise way to create lists in Python. It allows you to generate lists by applying an expression to each item in an iterable, optionally including a conditional to filter items. It has the syntax [expression for item in iterable if condition].

## How do you reverse a list in Python?
You can reverse a list in Python using either the reverse() method, which reverses the list in place, or by using slicing with a step of -1. For example:

python
Copy code
my_list = [1, 2, 3, 4, 5]
reversed_list = my_list[::-1]
print(reversed_list)  # Output: [5, 4, 3, 2, 1]

## What is Scope in Python?
Every object in Python functions within a scope. A scope is a block of code where an object in Python remains relevant. Namespaces uniquely identify all the objects inside a program. However, these namespaces also have a scope defined for them where you could use their objects without any prefix. A few examples of scope created during code execution in Python are as follows:

A local scope refers to the local objects available in the current function.
A global scope refers to the objects available throughout the code execution since their inception.
A module-level scope refers to the global objects of the current module accessible in the program.
An outermost scope refers to all the built-in names callable in the program. The objects in this scope are searched last to find the name referenced.
Note: Local scope objects can be synced with global scope objects using keywords such as global.





