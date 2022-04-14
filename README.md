# Python-Scripts
List - Mutable
tuple - Immutable
set = Mutable
frozenset - Immutable
dict - Mutable
range - Immutable
bytes - Immutable
bytesarray - Mutable









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

List : 
      1. Order Preserved
      2. Duplicate objects are allowed
      3. [] represent square brackets
      4. Heterogenious objects can be appended
      5. Indexing and Slicing
      6. Growable in nature
      7. Mutable


Set datatype
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

