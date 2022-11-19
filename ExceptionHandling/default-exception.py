#!/usr/bin/env python3
import os
try: 
    #Risky Code
    MKDIR = "mkdir test01"
    os.system(MKDI)
    
    x = int(input("Enter First Number: "))
    y = int(input("Enter Second Number: "))
    print("The result is: ", x/y)
except ZeroDivisionError as msg:
    print("ZeroDivisionError")
except:
    #Exception Handling Code
    print("Default")
finally:
    # Cleanup Code
    print("hey reached finally")
    
