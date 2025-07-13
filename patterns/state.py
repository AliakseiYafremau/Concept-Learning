from abc import abstractmethod, ABC


class State(ABC):
    @abstractmethod
    def handle(self):
        pass


class Context:
    def request(self, state: State):  # state можно засунуть в __init__()
        print("Here is my logic")  # логика, которая не зависит от состояния
        state.handle()  # логика, которая ЗАВИСИТ от состояния


class ConcreteState1(State):
    def handle(self):
        print("State 1")


class ConcreteState2(State):
    def handle(self):
        print("State 2")


if __name__ == "__main__":
    state1 = ConcreteState1()
    state2 = ConcreteState2()
    context = Context()

    context.request(state1)
    context.request(state2)
