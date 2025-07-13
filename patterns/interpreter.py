from abc import abstractmethod, ABC


class Expression(ABC):
    @abstractmethod
    def interpret(self):
        pass


class Number(Expression):
    def __init__(self, value):
        self.value = value

    def interpret(self):
        return str(self.value)


class Add(Expression):
    def __init__(self, left: Expression, right: Expression):
        self.left = left
        self.right = right
