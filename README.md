## What is python?
```
Python is an interpreted, object-oriented, high-level programming language, developed by Guido van Rossum. 
It was originally released in 1991. Designed to be easy as well as fun, the name "Python" is a nod to the British comedy group Monty Python.
```
![alt text](https://github.com/jniranjanreddy/python/blob/master/Guido-Van-Rossum.JPG)

```
List - Mutable
tuple - Immutable
set = Mutable
frozenset - Immutable
dict - Mutable
range - Immutable
bytes - Immutable
bytesarray - Mutable
```
## Python extras
```
flake8 - linter - flake8 usecase - flake8 --max-line-length=90 ${my-path}
mypy - Static type checker against python modules
pytest - pytest --cov-report=html
black  - formatter
iosort - imported modues sorted by order
```


```
Python Identifiers.. are CaseSensitive.

1. below are the valid identifiers.
   a to z
   A to Z
   0-9
   _(underscore)
   
2. should not start with digit
   123rama=10
   
3. Its CaseSensitive
   rama=10
   Rama=20
   RAMA=30

4. no length limit

x - simple x variable
_x - Protected Variable
__x - Strict Private variable
__x__ - Magic Variable

5. Reserved keywords..
   Reserved words in Python:33         Reserved words in Java 53
   True False None
   and or not is
   if elif else
   While For Break Continue return in yield
   Try Except Finally, Raise Assert
   Import From as Class Def Pass
   Global nonlocal lambda del with
   
[root@minikube01 ~]# python3
Python 3.6.8 (default, Nov 16 2020, 16:55:22)
[GCC 4.8.5 20150623 (Red Hat 4.8.5-44)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import keyword

>>> print(keyword.kwlist)
['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

>>> import shutil
>>> help(shutil)
>>> dir(shutil)
['COPY_BUFSIZE', 'Error', 'ExecError', 'ReadError', 'RegistryError', 'SameFileError', 'SpecialFileError', '_ARCHIVE_FORMATS', '_BZ2_SUPPORTED', '_GiveupOnFastCopy', '_HAS_FCOPYFILE', '_LZMA_SUPPORTED', '_UNPACK_FORMATS', '_USE_CP_SENDFILE', '_WINDOWS', '_WIN_DEFAULT_PATHEXT', '_ZLIB_SUPPORTED', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_access_check', '_basename', '_check_unpack_options', '_copyfileobj_readinto', '_copytree', '_copyxattr', '_destinsrc', '_ensure_directory', '_fastcopy_fcopyfile', '_fastcopy_sendfile', '_find_unpack_format', '_get_gid', '_get_uid', '_is_immutable', '_islink', '_make_tarball', '_make_zipfile', '_ntuple_diskusage', '_rmtree_isdir', '_rmtree_islink', '_rmtree_safe_fd', '_rmtree_unsafe', '_samefile', '_stat', '_unpack_tarfile', '_unpack_zipfile', '_use_fd_functions', 'chown', 'collections', 'copy', 'copy2', 'copyfile', 'copyfileobj', 'copymode', 'copystat', 'copytree', 'disk_usage', 'errno', 'fnmatch', 'get_archive_formats', 'get_terminal_size', 'get_unpack_formats', 'getgrnam', 'getpwnam', 'ignore_patterns', 'make_archive', 'move', 'nt', 'os', 'posix', 'register_archive_format', 'register_unpack_format', 'rmtree', 'stat', 'sys', 'unpack_archive', 'unregister_archive_format', 'unregister_unpack_format', 'which']
>>>
    
 Switch and do-while is not present Python
   
   
   Data Types:--

   1. int
   2. float
   3. complex
   4. bool
   5. str
   6. Tuple
   7. set
   8. frozen set
   9. dict
   10. byte
   11. bytearray
   12. range
   13. none
 
 
 1. int
      int can be configured below ways..
      a = 10
        |__> decimal form - base10
        |__> binary form  - base2
        |__> Octal form   - base8
        |__> Hexa Decimal - base16
   
   
Base Conversion Functions:-

   1. bin()
   2. oct()
   3. hex()

   >>> bin(15)
   '0b1111'

   >>> oct(100)
   '0o144'
   >>>

   >>> hex(100)
   '0x64'
   >>>

2. Float
   >>> a = 1.5
   >>> a
   1.5
   >>> type(a)
   <class 'float'>
   >>>
   
3. Complex
   >>> a = 10 + 20j
   >>> type(a)
   <class 'complex'>
   >>>
   
   >>> a.real
   10.0
   >>> a.imag
   20.0
   
4. bool
   True - T should be in uppercase
   fallse - F should be in uppercase
   
   
5. str
   #!/usr/bin/env python3
# a="python"
# output=a[0].upper()+a[1:]
# print(output)

# b="python"
# # bout=b[:len(b)-1]+b[-1].upper()
# boutput=b[:len(b)-1]+b[-1].upper()
# print(boutput)

# c = "python"
# coutput = c[0].upper()+c[1:len(c)-1]+c[-1].upper()
# print(coutput)

# d = c.upper()
# d_lower = d[0].lower()+d[1:len(d)-1]+d[-1].lower()
# print(d_lower)
# print(d)

a="python" * 3
print(a)
b = 3 * "python"
print(b)
   
   
Type Casting Data types
   1. int()
   2. float()
   3. complex()
   4. bool()
   5. str()
   
 
 
 >>> bool(10)
True
>>> bool(0)
False
>>> bool(-0)
False
>>> bool(-1)
True
>>>

>>> bool(0.0)
False
>>> bool(0.1)
True
>>>

>>> bool("True")
True
>>> bool('True')
True
>>> bool('False')
True
>>> bool('Yes')
True
>>> bool('No')
True
>>> bool('')
False
>>> bool("")
False
>>>
==============
str()

   
   
   
Datatypes:
    list - []
    tuple - ()
    set - {}
    frozenset
    dict { name:'nirulabs'}
    range
    bytes
    bytearray
    

List : []
      1. Order Preserved
      2. Duplicate objects are allowed
      3. [] represent square brackets
      4. Heterogenious objects can be appended
      5. Indexing and Slicing
      6. Growable in nature
      7. Mutable
      
Tuple: ()
     1. All same as List, only difference is, Tuple is immutable.
     2. readonly version of List.

Set : {}
    1. duplicated are not allowed
    2. Order not require
    3. Indexing|Slicing not allowed
    4. set is mutable and growable
    5. heteregenous elements are allowed
    

Operators:-
    Operator is a symbol that performs certain operations. 
    Python provides the following set of operators
         1) Arithmetic Operators 
         2) Relational Operators OR Comparison Operators 
         3) Logical operators 
         4) Bitwise oeprators 
         5) Assignment operators 
         6) Special operators
1) Arithmetic Operators:
         1) +
         2) –
         3) *
         4) /
         5) %
         6) // Floor Division Operator
         7) ** Exponential operator
Eg: test.py 1) a=10 2) b=2 3) print('a+b=',a+b) 4) print('a-b=',a-b) 5) print('a*b=',a*b) 6) print('a/b=',a/b) 7) print('a//b=',a//b) 8) print('a%b=',a%b) 9) print('a**b=',a**b) Output:
Python test.py OR py test.py
a+b = 12
a-b= 8
a*b= 20
```
What is the difference between "==" and is operator.
```
== operator is used to compere the content of the given two objects.
is operator is used to compare the address of the two objects.
```
Logical Operators..
```
and or not are logical Operators..
It Returns True, both arguments are True.
True and True   - True
True and false  - False
False and True  - False
False and False - False

True or True   - True
True or false  - False
False or True  - False
False or False - False
```
Logical Operators with non-boolean valures.
```
x and y
0 and 20 
if x evaluate to False, result is false either 0

10 and 20
if x evaluate to True, the result is y, eiter 20.
```


Ternary Operator

```
Special Operator:
  1. Identity Operator - address comparision operator- 
        >>> a = 10
        >>> b = 10
        >>> print(a is b)
  2. membership operator - 
     >>> a = "hello"
     >>> print('h' in a)
         True
     >>> print('a' in a)
         False
```
Operator Precedence
 >>> print(10+10*3)
     40
>>> print((10+10)*3)
     60

Seperator
```
print("Durga"+"Soft")
print("Durga \t Soft")
print(10 * "Durga")
print("Durga \n Soft")
a,b,c, = 10,20,30
print("valures are:", a, b, c)
print(f"valures are:", {a}, {b}, {c} )
#using seperator
print(a,b,c, sep='@')
print('Hello',end='')
print('Durga',end='')
print('Soft')
# Using End
print('Hello',end='::')
print('Durga',end='**')
print('Soft')
# Combination of sep and end
print(10,20,30,sep=':',end='###')
print(40,50,60,sep='::')
print(70,80,sep='**',end='@@')
print(90,100)

# print with Replacement operator
name = 'Durga'
sl = 10000
company = 'dsoft'
print('Hello {}, your Salary is {}, and your company is: {}'.format(name,sl,company))
print('Hello {0}, your Salary is {1}, and your company is: {2}'.format(name,sl,company))
# Keyword Arguments
print('Hello {n}, your Salary is {s}, and your company is: {c}'.format(n=name,s=sl,c=company))
print(f'Hello {name}, your Salary is {sl}, and your company is: {company}')

#print with formatted string
# %i - signed decimal value
# %d - signed Decimal value
# %f - float value
# %s - string value - including object list set 
a = 10
b = 20
c = 30
print('a value is: %i' %a)
print('a=%d,b=%d,c=%d' %(a,b,c))

price = 70.1234
print("The price is {}".format(price))
print("The price is %f" %price)
print("The price is %.2f" %price)
```

Flow Control

## Transfer Statements


## Important Modules.
```
os, sys, shutil, datetime, socket, random, io, re, urllib, logging, shlex, json, traceback, signal, syslog, multiprocessing, sqlite3, functools, imp,
zipfile, base64, tempfile, __main__, typing, pathlib, enum, collections, __future__, itertools, warnings, error no, codecs, tarfile, argparse, abc,
inspect, pathlib, importlib, uuid, time, traceback, optparse, copy, pickle, tkinter, email, venv, glob, locale, builtins, smtplib, zlib.
```

![image](https://github.com/jniranjanreddy/python/assets/83489863/a7b05f0e-63d8-42d4-92ff-d3129cfd8591)


```
__dict__ = it displays the workspace.
__base__
__bases__
__annotations__
__call__
__class__
__delattr__
__dictoffset__
__doc__
__dir__
__eg__
__flags__
__format__
__getattribute__
__getstate__
__hash__
__init__
__init_subclass__
__instancecheck__
__itemsize__
__module__
__mro__
__name__
__ne__
__new__
__or__
__prepare__
__qualname__
__reduce__
__reduce_ex__
__repr__
__ror__
__setattr__
__sizeof__
__str__
__subclasscheck__
__subclasses__
__subclasshook__
__text_signature__
__weakrefobject__

__base__ - Only applicable to new-style classes (derived from object), it refers to the immediate base class.
__bases__ - A tuple containing base classes of a class.
__annotations__ - A dictionary holding annotations for class attributes or method parameters and return types.
__call__ - Allows an instance of a class to be called as a function. Defined using def __call__(self, *args, **kwargs):.
__class__ - References the class of an instance.
__delattr__ - Called when delattr is used to delete an attribute. Defined using def __delattr__(self, name):.
__dictoffset__ - The offset in bytes of the object’s __dict__ within the object’s memory layout. Mainly used internally by the interpreter.
__doc__ - The docstring of a class, function, or module.
__dir__ - Called by dir() to get a list of attributes and methods. Defined using def __dir__(self):.
__eg__ - This seems like a typo or non-standard attribute; there’s no built-in Python attribute __eg__.
__flags__ - Used internally by the interpreter, especially in classes created with the type() function.
__format__ - Called by the format() function and formatted string literals. Defined using def __format__(self, format_spec):.
__getattribute__ - Called unconditionally to access an attribute. Defined using def __getattribute__(self, name):.
__getstate__ - Called by pickle to get the state of an object for pickling. Defined using def __getstate__(self):.
__hash__ - Called by hash() and when adding an object to a hash-based collection like set or dict. Defined using def __hash__(self):.

__init__ - The initializer method for a class. Called when a class instance is created. Defined using def __init__(self, *args, **kwargs):.

__init_subclass__ - Called when a class is subclassed. Defined using def __init_subclass__(cls):.
__instancecheck__ - Used by isinstance(). Defined using def __instancecheck__(self, instance):.
__itemsize__ - For variable-sized objects, it gives the size in bytes of a single item. Used internally by the interpreter.
__module__ - The name of the module in which a class was defined.
__mro__ - A tuple showing the method resolution order used to look up methods.
__name__ - The name of a class, function, method, etc.
__ne__ - Called by the != operator. Defined using def __ne__(self, other):.
__new__ - Responsible for creating a new instance of a class. Defined using def __new__(cls, *args, **kwargs):.
__or__ - Called by the | operator. Defined using def __or__(self, other):.
__prepare__ - Used to create the namespace for a class. Defined in a metaclass using def __prepare__(metacls, name, bases):.
__qualname__ - The qualified name of a class, function, method, etc., providing a dotted path to the name.
__reduce__ - Used by pickle to define how an object should be reduced to a serializable form. Defined using def __reduce__(self):.
__reduce_ex__ - An extended version of __reduce__ for pickle. Defined using def __reduce_ex__(self, protocol):.
__repr__ - Called by repr(), and should return a string that ideally can be used to recreate the object. Defined using def __repr__(self):.
__ror__ - Called by the | operator when the left operand does not support it. Defined using def __ror__(self, other):.
__setattr__ - Called when an attribute assignment is attempted. Defined using def __setattr__(self, name, value):.
__sizeof__ - Called by sys.getsizeof() to get the size of an object in bytes. Defined using def __sizeof__(self):.
__str__ - Called by str() and print(), and should return a readable string representation of an object. Defined using def __str__(self):.
__subclasscheck__ - Used by issubclass(). Defined using def __subclasscheck__(self, subclass):.
__subclasses__ - Returns a list of known subclasses of a class.
__subclasshook__ - Provides a customizable check for issubclass(). Defined in an ABC (Abstract Base Class) using @classmethod def __subclasshook__(cls, C):.
__text_signature__ - Holds the function signature string. Used by the inspect module and documentation tools.
__weakrefobject__ - The attribute used internally to store weak references. May refer to __weakref__, which is used for weak references support in Python objects.

Each of these attributes and methods plays a specific role in Python's object model, allowing for rich and flexible behavior customization. They are primarily used for implementing custom classes, enabling special behaviors, and providing hooks for various operations and interactions.









```
