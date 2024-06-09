
## Abstract Method
from abc import abstractmethod
class Vehicle:
    @abstractmethod
    def getNoOfWheels(self):
        pass


# Abstract Class
from abc import abstractmethod, ABC
class Vehicle(ABC):
    @abstractmethod
    def getNoOfWheels(self):
        pass

class Bus(Vehicle):
    def getNoOfWheels(self):
        return 6

class Auto(Vehicle):
    def getNoOfWheels(self):
        return 3

# Initiliasing Class
b = Bus()
print(b.getNoOfWheels())

a = Auto()
print(a.getNoOfWheels())
