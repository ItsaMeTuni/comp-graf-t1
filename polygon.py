from algorithms import *
from OpenGL.GL import *
from quickhull import *
from colors import *


class Polygon:
    def __init__(self, vertexes):
        self.vertexes = vertexes
        self.limit_min, self.limit_max = get_limits(vertexes)

    def contains_point(self, point):
        max_x = self.limit_max.x

        a = point
        b = Point(max_x, point.y)

        intersection_count = 0

        for i in range(len(self.vertexes)):
            c = self.vertexes[i - 1]
            d = self.vertexes[i]

            if intersects(a, b, c, d):
                intersection_count += 1

        return intersection_count % 2 != 0

    def draw(self, color=White):
        glColor3f(*color)
        glBegin(GL_LINE_LOOP)

        for vertex in self.vertexes:
            glVertex3f(vertex.x, vertex.y, 0)

        glEnd()

    def get_convex_hull(self):
        return Polygon(quickhull(self.vertexes))


def get_limits(vertexes):
    x_points = [vertex.x for vertex in vertexes]
    y_points = [vertex.y for vertex in vertexes]

    min_point = Point(min(x_points), min(y_points))
    max_point = Point(max(x_points), max(y_points))

    return min_point, max_point
