#!/usr/bin/env python3
import logging

class TooYoungException(Exception):
    def __init__(self, msg):
        self.msg=msg
        
age = int(input("Enter your age: "))

if age > 60:
    raise TooYoungException("Please wait somemore time: ")
elif age < 18:
    raise TooYoungException("You are already crossed age")
else:
    print("Thanks for Registration")
