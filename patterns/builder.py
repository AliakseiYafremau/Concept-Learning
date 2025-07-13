class Wheel:
    def __init__(self, brand: str):
        self.brand = brand

    def __repr__(self):
        return f"{self.brand} wheel"

class Seat:
    def __init__(self, price: int):
        self.price = price

    def __repr__(self):
        return f"{self.price}$ seat"

class Car:
    def __init__(self, wheels: list[Wheel] = [], seats: list[Seat] = []):
        self.wheels = wheels
        self.seats = seats

    def __str__(self):
        return f"Wheels: {self.wheels}, Seats: {self.seats}"
        
class Builder:
    def __init__(self):
        self.car = Car()

    def build_wheel(self):
        self.car.wheels.append(Wheel("Asanti"))

    def build_seat(self):
        self.car.seats.append(Seat(0))

    def get_car(self):
        result = self.car
        self.car = Car()
        return result

class SpecificBuilder1(Builder):
    def build_wheel(self):
        self.car.wheels.append(Wheel("Cray"))

    def build_seat(self):
        self.car.seats.append(Seat(100))

class SpecificBuilder2(Builder):
    def build_seat(self):
        self.car.seats.append(Seat(200))

def create_car(builder: Builder):
    builder.build_wheel()
    builder.build_wheel()
    builder.build_wheel()
    builder.build_wheel()
    builder.build_seat()

    return builder.get_car()

if __name__ == "__main__":
    builder1 = SpecificBuilder1()
    car1 = create_car(builder1)
    print(car1)
