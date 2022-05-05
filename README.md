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

