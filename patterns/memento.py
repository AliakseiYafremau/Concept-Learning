class Memento:
    def __init__(self, counter):
        self.__counter = counter

    def get_state(self):
        return self.__counter

    def set_state(self, counter):
        self.__counter = counter


class Originator:
    def __init__(self, counter=0):
        self.__counter = counter
        self._mementos = []

    def remember(self):
        self._mementos.append(self.create_memento())

    def go_back(self):
        self.set_memento(self._mementos.pop())

    def increase(self, value=1):
        self.__counter += value

    def get_counter(self):
        return self.__counter

    def create_memento(self):
        return Memento(self.__counter)

    def set_memento(self, memento: Memento):
        self.__counter = memento.get_state()


def wait_day(originator: Originator):
    originator.increase(24)


def wait_week(originator: Originator):
    originator.increase(168)


if __name__ == "__main__":
    clock = Originator()

    clock.remember()
    print("First:", clock.get_counter())

    wait_day(clock)

    clock.remember()
    print("Second:", clock.get_counter())

    wait_week(clock)

    clock.remember()
    print("Third:", clock.get_counter())

    clock.go_back()
    print("Go back once:", clock.get_counter())

    clock.go_back()
    print("Go back twice:", clock.get_counter())

    clock.go_back()
    print("Go back three times:", clock.get_counter())
