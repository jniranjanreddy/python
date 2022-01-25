#!/usr/bin/env python3
class Student:
    schoolname="Durgasoft" #Static Variable

    # variables
    # Methods
    def __init__(self,name,rollno,marks):
        self.name = "Rama" # Instance Variables
        self.rollno = 101 # Instance Variables
        self.marks = 90 # Instance Variables

    def info(self):
        x = 10 # This is Local Variable
        for i in x: # local Variable
            print(i)
    