from abc import abstractmethod, ABC


class SomeClass(ABC):
    def operation(self, array: list[int]):
        # some logic
        print(self.sort(array))
        # some logic

    @abstractmethod
    def sort(self, array: list[int]) -> list[int]:
        pass


class ConcreteClass1(SomeClass):
    def sort(self, array: list[int]) -> list[int]:
        result = array.copy()
        result.sort()
        return result


class ConcreteClass2(SomeClass):
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
    some_object1 = ConcreteClass1()
    some_object2 = ConcreteClass2()

    lst = [5, 3, 4, 2, 7, 6, 8, 1, 9]

    some_object1.operation(lst)
    some_object2.operation(lst)
