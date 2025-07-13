from abc import abstractmethod


class Flywieght:
    @abstractmethod
    def operation(self):
        pass


class ConcreteFlyweight(Flywieght):
    def __init__(self, intrinsic):
        self.intrinsic = intrinsic

    def operation(self):
        """Какая-то логика"""


class FlywieghtFactory:
    def get_flyweight(self, key):
        """
        если flyweight с ключом 'key' не существует:
            создать flyweight с key
        вернуть flyweight
        """
