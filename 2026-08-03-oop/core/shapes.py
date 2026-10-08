class Shape:
    def __init__(self):
        self.color = "Black"

    def get_area(self):
        return -1


class Rectangle(Shape):
    def __init__(self):
        super().__init__()
        self.length = 0
        self.width = 0

    def get_area(self):
        return self.length * self.width


class Circle(Shape):
    def __init__(self):
        super().__init__()
        self.radius = 0.0

    def get_area(self):
        return 3.14 * self.radius * self.radius


def get_shape_area(shape: Shape):
    return shape.get_area()
