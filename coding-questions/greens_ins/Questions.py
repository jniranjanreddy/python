# 1. Print hello world
a = "hello world"
print(a)


# 2. Write a program on Addition(sub)(mul)(div) of two Numbers
b = 10
c = 20
print("Addition", b + c)
print("Substraction", b - c)
print("Multiplication", b * c)
print("division", b / c)

# 3. Write a program Average on three numbers . 
b = 90
c = 20
d = 10
myAvg = (b + c + d) / 3
print("Average of three numbers", myAvg)

# Kinetic Energy
def calculate_kinetic_energy(mass, velocity):
    # Kinetic energy formula: KE = 0.5 * mass * velocity^2
    kinetic_energy = 0.5 * mass * velocity ** 2
    return kinetic_energy

print(calculate_kinetic_energy(20,30))

# Conditional Statement: 
# 1. Write a program Which one is big given two values using if else condition
a = 10
b = 5
if a > b:
    print("a is big")
else:
    print("b is big")    

# 2. Write a program Eligible for voting for given age by using scanner class

class EligibleForVoting:
    def check_eligibility(self, age):
        if age >= 18:
            print("Eligible for voting")
        else:
            print("Not eligible for voting")

obj = EligibleForVoting()
obj.check_eligibility(25)

# 
class even_odd:
    def check_eligibility(self, number):
        if number % 2 == 0:
            print("Even number")
        else:
            print("Odd Number")
Even_odd = even_odd()
Even_odd.check_eligibility(20)

# Write a program calculate the total marks and if it is less than 35 marks  on single subject  Consider as fail .

class TotalMarks:
    def check_marks(self, marks):
        if marks < 35:
            print("Fail")
        else:
            print("Pass") 

obj = TotalMarks()
obj.check_marks(30)

# 

myMarks = [40,50,60,70,80]
minMarks = min(myMarks)
if minMarks < 35:
    print("Fail")
else: 
    print("Pass")

if min(myMarks) < 35:
    print("Fail")
else: 
    print("Pass")



