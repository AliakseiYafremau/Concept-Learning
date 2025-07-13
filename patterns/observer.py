from abc import abstractmethod, ABC


class Subject(ABC):
    @abstractmethod
    def update(self):
        pass


class Observer:
    def __init__(self):
        self.subjects: list[Subject] = []

    def attach(self, subject: Subject):
        self.subjects.append(subject)

    def detach(self, subject: Subject):
        self.subjects.remove(subject)

    def notify(self):
        for sub in self.subjects:
            sub.update()

    def operation(self):
        # some logic
        self.notify()


class ConcreteSubject1(Subject):
    def update(self):
        print("ConcreteSubject1 was updated")


class ConcreteSubject2(Subject):
    def update(self):
        print("ConcreteSubject2 was updated")


class ConcreteSubject3(Subject):
    def update(self):
        print("ConcreteSubject3 was updated")


if __name__ == "__main__":
    obs = Observer()
    sub1 = ConcreteSubject1()
    sub2 = ConcreteSubject2()
    sub3 = ConcreteSubject3()

    obs.attach(sub1)
    obs.attach(sub2)
    obs.attach(sub3)

    obs.operation()
    obs.detach(sub3)
    obs.operation()
