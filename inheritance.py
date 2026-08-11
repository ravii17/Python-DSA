class Car:
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("Car stopped")


class ToyotaCar(Car):
    def __init__(self, name, type):
        self.name = name
        super().__init__(type)


car1 = ToyotaCar("Primus", "Electric")

print(car1.type)
print(car1.name)