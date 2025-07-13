from abc import abstractmethod, ABC


class Iterator(ABC):
    @abstractmethod
    def first(self):
        pass

    @abstractmethod
    def next(self):
        pass

    @abstractmethod
    def is_done(self) -> bool:
        pass

    @abstractmethod
    def current(self):
        pass


class CustomList(ABC):
    def __init__(self):
        self.lst = []

    @abstractmethod
    def create_iterator(self) -> Iterator:
        pass

    def count(self):
        return len(self.lst)

    def add(self, value):
        self.lst.append(value)

    def remove(self, value):
        self.lst.remove(value)

    def __getitem__(self, index):
        return self.lst[index]


class SpecificIterator(Iterator):
    def __init__(self, lst: CustomList):
        self.cursor = 0
        self.lst = lst

    def first(self):
        self.cursor = 0

    def next(self):
        self.cursor += 1

    def is_done(self):
        if self.cursor >= self.lst.count():
            return True
        return False

    def current(self):
        if self.is_done():
            raise StopIteration
        return self.lst[self.cursor]


class SpecificList(CustomList):
    def create_iterator(self):
        return SpecificIterator(self)


if __name__ == "__main__":
    lst = SpecificList()
    lst.add("First element")
    lst.add("Second element")
    lst.add("Third element")

    itrtr = lst.create_iterator()
    print(itrtr.current())
    itrtr.next()
    print(itrtr.current())
    itrtr.next()
    print(itrtr.current())
    itrtr.next()
