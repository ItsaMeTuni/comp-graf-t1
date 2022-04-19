from polygon import *
from algorithms import *
from quickhull import *


class ConvexPolygon(Polygon):
    def __init__(self, vertexes):
        super().__init__(quickhull(vertexes))

    def contains_point(self, point):
        for i in range(len(self.vertexes)):
            a = self.vertexes[i - 1]
            b = self.vertexes[i]

            ab = b - a
            ab_median = a + ab/2
            median_to_point_vec = point - ab_median
            normal = Point(ab.y, -ab.x)

            if dot_product(normal, median_to_point_vec) < 0:
                return False

        return True
