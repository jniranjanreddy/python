#!/usr/bin/env python3
try: 
    print(10/0)
except ZeroDivisionError as msg:
    print("Exception Type:", type(msg))
    print("Exception Type:", msg.__class__)
    print("Exception Type:", msg.__class__.__name__)
    print("The Description of Message:", msg)