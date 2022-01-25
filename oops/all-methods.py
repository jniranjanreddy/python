#!/usr/bin/env python3
class Student:
    schoolname = "Durgasoft"  # Static Variable

    def __init__(self, name, rollno, marks):
        self.name = "Rama"  # Instance Variables
        self.rollno = 101  # Instance Variables
        self.marks = 90  # Instance Variables

    def getStudentinfo(self):  # Instance Method
        print("Student Name: ", self.name)
        print("Student RollNo: ", self.rollno)

    @classmethod  # Class Method
    def getSchoolName(cls):
        print("School Name: ", cls.schoolname)

    @staticmethod  # Static Method
    def getSum(a, b):
        sum = a + b
        return sum
