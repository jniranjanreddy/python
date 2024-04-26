class Student:
   def __init__(self, fname, lname, age, section):
       self.firstname = fname
       self.lastname = lname
       self.age = age
       self.section = section
# creating a new object
stu1 = Student("Sara", "Ansh", 22, "A2")
print(stu1.firstname)
print(stu1.lastname)
print(stu1.age)
print(stu1.section)
