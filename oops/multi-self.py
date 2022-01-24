#!/usr/bin/env python3
class Student:

    def __init__(self,name,rollno,marks):
        self.name = name
        self.rollno = rollno
        self.marks = marks
        

    def talk(self):
        print("Hello My Name is: ", self.name)
        print("Hello My Role Number is: ", self.rollno)
        print("Hello My My Marks are: ", self.marks)

s1 = Student("Sunny", 101, 50)
s1.talk()