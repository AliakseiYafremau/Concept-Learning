from abc import abstractmethod, ABC


class Widget(ABC):
    pass


class Mediator(ABC):
    @abstractmethod
    def notify(self, widget: Widget):
        pass


class ClickButton(Widget):
    def __init__(self, mediator: Mediator):
        self.mediator = mediator

    def click(self):
        # ...
        self.mediator.notify(self)
        # ...


class ToggleButton(Widget):
    def __init__(self, mediator: Mediator):
        self.mediator = mediator

    def toggle(self):
        # ...
        self.mediator.notify(self)
        # ...


class ConcreteMediator(Mediator):
    def notify(self, widget: Widget):
        print(f"{widget} was changed")


if __name__ == "__main__":
    mediator = ConcreteMediator()
    click_button = ClickButton(mediator)
    toggle_button = ToggleButton(mediator)

    click_button.click()
    toggle_button.toggle()
