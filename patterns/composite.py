from abc import abstractmethod


class Component:
    @abstractmethod
    def read(self) -> str:
        pass


class Composite(Component):
    @abstractmethod
    def add(self, component: Component) -> None:
        pass

    @abstractmethod
    def remove(self, component: Component) -> None:
        pass

    @abstractmethod
    def get_child(self, index: int) -> Component:
        pass


class Text(Component):
    def __init__(self, text: str):
        self.text = text

    def read(self) -> str:
        return self.text


class Summary(Composite):
    def __init__(self):
        self.children = []

    def read(self) -> str:
        result = ""
        for child_index in range(len(self.children)):
            if child_index == 0:
                result = self.get_child(child_index).read()
            else:
                result += " and "
                result += self.get_child(child_index).read()
        return result

    def add(self, component: Component) -> None:
        self.children.append(component)

    def remove(self, component: Component) -> None:
        self.children.remove(component)

    def get_child(self, index: int) -> Component:
        return self.children[index]


text1 = Text("The first text")
text2 = Text("The second text")
text3 = Text("The third Text")

summary1 = Summary()
summary2 = Summary()

summary1.add(text1)
summary1.add(summary2)
summary2.add(text2)
summary2.add(text3)

print(summary1.read())
