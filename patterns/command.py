from abc import abstractmethod, ABC


class Reciever:
    @staticmethod
    def some_operation():
        print("It is the operation from the Reciever")


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class SomeCommand(Command):
    def __init__(self, reciever: Reciever):
        self.reciever = Reciever

    def execute(self):
        self.reciever.some_operation()


class Invoker:
    def __init__(self, command: Command):
        self.command = command

    def click(self):
        self.command.execute()


if __name__ == "__main__":
    reciever = Reciever()
    some_command = SomeCommand(reciever)

    invoker = Invoker(some_command)

    invoker.click()
