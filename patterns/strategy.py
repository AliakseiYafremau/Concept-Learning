from abc import abstractmethod, ABC


class Strategy(ABC):
    @abstractmethod
    def sort(self, array: list[int]) -> list[int]:
        pass


class Context:
    def __init__(self, stategy: Strategy):
        self.strategy = stategy

    def operation(self, lst: list[int]):
        # some logic
        result = self.strategy.sort(lst)
        # some logic
        return result


class BuiltInStrategy(Strategy):
    def sort(self, array: list[int]) -> list[int]:
        result = array.copy()
        result.sort()
        return result


class CustomStrategy(Strategy):
    def sort(self, array: list[int]) -> list[int]:
        result = []
        while array:
            minimal = 0
            for i in range(len(array)):
                if array[minimal] > array[i]:
                    minimal = i
            result.append(array.pop(minimal))

        return result


if __name__ == "__main__":
    built_in = BuiltInStrategy()
    custom = CustomStrategy()
    context1 = Context(built_in)
    context2 = Context(custom)

    lst = [5, 3, 4, 2, 7, 6, 8, 1, 9]

    print(context1.operation(lst))
    print(context2.operation(lst))
