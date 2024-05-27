class Engine:
    def __init__(self):
        self.power = "1000cc"
    def useEngine(self):
        print("Engine specific functionality")


class Car:
    def __init__(self):
        self.engine = Engine()
        print("Car object created")
        self.model = "BMW"

    def m2(self):
        print("Car required Engine functionality")
        self.engine.useEngine()
        print(self.model)
        print(self.engine.power)

c = Car()
c.m2()