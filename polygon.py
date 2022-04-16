from point import *

class Polygon:
    def __init__(self, vertexes):
        self.vertexes = vertexes
        self.limit_min, self.limit_max = get_polygon_limits(vertexes)


    def contains_point(self, point):
        y = point.y
        min_x = self.limit_min.x
        max_x = self.limit_max.x

        a = Point(min_x, y)
        b = Point(max_x, y)

        for i in range(1, len(self.vertexes)):
            c = self.vertexes[i - 1]
            d = self.vertexes[i]

            if intersects(a, b, c, d):
                return true

        return false

def get_polygon_limits(vertexes):
    x_points = [vertex.x for vertex in vertexes]
    y_points = [vertex.y for vertex in vertexes]

    min_point = Point(min(x_points), min(y_points))
    max_point = Point(max(x_points), max(y_points))

    return min_point, max_point

