from abc import abstractmethod


class Component:
    @abstractmethod
    def operate(self) -> str:
        pass


class ConcreteComponent(Component):
    def operate(self):
        return "I'm the ConcreteComponent"


class FirstDecorator(Component):
    def __init__(self, component: Component):
        self.decorated = component

    def operate(self):
        return (
            f'I\'m the FirstDecorator and here the result: "{self.decorated.operate()}"'
        )


class SecondDecorator(Component):
    def __init__(self, component: Component):
        self.decorated = component

    def operate(self):
        return f'I\'m the SecondDecorator and here the result: "{self.decorated.operate()}"'


concrete = ConcreteComponent()
first = FirstDecorator(concrete)
second = SecondDecorator(first)
print(second.operate())
