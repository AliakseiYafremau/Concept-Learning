class Target:
    def some_operation(self):
        return "Target operation"


class Adaptee:
    def specific_operation(self):
        return "Adaptee operation"


class Adapter(Target, Adaptee):
    def some_operation(self):
        return self.specific_operation()


print(Adapter().some_operation())
