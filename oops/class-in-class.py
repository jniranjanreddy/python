class Employee:
    def __init__(self,emname,emID,emsal):
        self.name = emname     # Instance Variables
        self.emID = emID      # Instance Variables
        self.emsal = emsal        # Instance Variables
    def display(self):
        print("Employee: Name: ", self.name)
        print("Employee ID: ", self.emID)
        print("Employee Salary: ", self.emsal)
   
class Manager:
    def updateEmpSal(emp):
        emp.emsal = emp.emsal+10000
        emp.display()

emp = Employee("Rama",101,90)
Manager.updateEmpSal(emp)
print(Manager.__dict__)
# m = Manager("Rama",100,10000)
# t.display()
# print(t.name)
# print(t.emID)
# print(t.emsal)
# print(m.name)