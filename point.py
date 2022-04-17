class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Point(x, y)

    def __mul__(self, other: int):
        x = self.x * other
        y = self.y * other
        return Point(x, y)

    def __truediv__(self, other: int):
        x = self.x / other
        y = self.y / other
        return Point(x, y)

    def __str__(self):
        return f'(x: {self.x} , y: {self.y})'
