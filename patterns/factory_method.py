from abc import ABC, abstractmethod

class Car(ABC):
    @abstractmethod
    def get_brand(self) -> str:
        ...

class BMW(Car):
    def get_brand(self) -> str:
        return "BMW"

class Audi(Car):
    def get_brand(self) -> str:
        return "Audi"

class Creator(ABC):
    @abstractmethod
    def create_car(cls) -> Car:
        ...

    def travel(self):
        car = self.create_car()
        print(f"Amazing trip on {car.get_brand()}!")
    

class BMWCreator(Creator):
    def create_car(self):
        return BMW()

class AudiCreator(Creator):
    def create_car(self):
        return Audi()

if __name__ == "__main__":
    bmw_creator = BMWCreator()
    audi_creator = AudiCreator()

    bmw_creator.travel()
    audi_creator.travel()
