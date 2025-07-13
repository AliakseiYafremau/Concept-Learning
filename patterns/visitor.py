from __future__ import annotations
from abc import abstractmethod, ABC


class Shape(ABC):
    @abstractmethod
    def accept(self, visitor: Visitor):
        pass


class Dot(Shape):
    def __init__(self, x, y):
        self.coords = [x, y]

    def accept(self, visitor: Visitor):
        return visitor.visit_dot(self)

    def get_coords(self):
        return [0, 0]


class Rectangle(Shape):
    def __init__(self, x1, y1, x2, y2):
        self.coords = [x1, y1, x2, y2]

    def accept(self, visitor: Visitor):
        return visitor.visit_rect(self)

    def get_coords(self):
        return self.coords


class Visitor(ABC):
    @abstractmethod
    def visit_dot(self, element: Dot):
        pass

    @abstractmethod
    def visit_rect(self, element: Rectangle):
        pass


class ExtractXVisitor(Visitor):
    def visit_dot(self, element: Dot):
        return element.coords[0]

    def visit_rect(self, element: Rectangle):
        return (element.coords[0], element.coords[2])


class ExtractYVisitor(Visitor):
    def visit_dot(self, element: Dot):
        return element.coords[1]

    def visit_rect(self, element: Rectangle):
        return (element.coords[1], element.coords[3])


if __name__ == "__main__":
    d = Dot(1, 2)
    r = Rectangle(1, 2, 3, 4)
    get_x_visitor = ExtractXVisitor()
    get_y_visitor = ExtractYVisitor()

    shapes = [d, r]
    for shape in shapes:
        print(shape.accept(get_x_visitor))
        print(shape.accept(get_y_visitor))
