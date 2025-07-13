class Target:
    def some_operation(self):
        return "Target operation"

class Adaptee:
    def specific_operation(self):
        return "Adaptee operation"

class Adapter(Target):
    def __init__(self, adaptee):
        self._adaptee = adaptee

    def some_operation(self):
        return self._adaptee.specific_operation()

print(Adapter(Adaptee()).some_operation())
