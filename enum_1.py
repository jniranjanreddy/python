from enum import Enum


class Car(Enum):
    TOYOTA = 1
    HONDA = 2
    BMW = 3
    FORD = 4
    FORD1 = 5

# def main():
#     print(Car.TOYOTA)
#     print(type(Car.HONDA))
#     print(Car.BMW)
#     print(Car.FORD)

# for car in Car:
#     print(car)
print(Car.TOYOTA.value)
print(Car.__dict__)

# if Car.TOYOTA == Car.HONDA:
#     print("TOYOTA and HONDA are same")
# else:
#     print("TOYOTA and HONDA are different")
# if __name__ == '__main__':
#     main()
