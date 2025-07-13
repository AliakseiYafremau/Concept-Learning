from abc import abstractmethod, ABC


class Handler(ABC):
    def __init__(self, next_handler=None):
        self.next = next_handler

    def set_handler(self, next_handler):
        self.next = next_handler
        return self.next

    def handle(self, parameter: str):
        if self.next:
            return self.next.handle(parameter)

        return None


class HasDigitHandler(Handler):
    def handle(self, parameter: str):
        if not any(char.isdigit() for char in parameter):
            raise ValueError("Doesn't contain any digit")
        else:
            super().handle(parameter)


class HasAlphaHandler(Handler):
    def handle(self, parameter: str):
        if not any(char.isalpha() for char in parameter):
            raise ValueError("Doesn't contain any alpha")
        else:
            super().handle(parameter)


class ContainMoreThanFiveCharHandler(Handler):
    def handle(self, parameter: str):
        if len(parameter) <= 5:
            raise ValueError("Doesn't contain more than five symbols")
        else:
            super().handle(parameter)


text = "123abc"

digit = HasDigitHandler()
alpha = HasAlphaHandler()
more = ContainMoreThanFiveCharHandler()

digit.set_handler(alpha).set_handler(more)

print(digit.handle(text))
