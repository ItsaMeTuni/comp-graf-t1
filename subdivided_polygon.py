from polygon import *

STRIP_COUNT = 10


class SubdividedPolygon(Polygon):
    def __init__(self, vertexes):
        super().__init__(vertexes)
        self.strip_step = abs(self.limit_max.y - self.limit_min.y) / STRIP_COUNT
        self.edges_by_strip = self.get_edges_by_strip()

    def get_edges_by_strip(self):
        edges_by_strip = []

        for i in range(STRIP_COUNT):
            top_left, bottom_right = self.get_strip_bbox(i)

            edges = get_edges_overlapping_bbox(self.vertexes, top_left, bottom_right)
            edges_by_strip.append(edges)

        return edges_by_strip

    def get_strip_bbox(self, strip_idx):
        min_y = self.limit_min.y + self.strip_step * strip_idx
        max_y = min_y + self.strip_step

        top_left = Point(self.limit_min.x, max_y)
        bottom_right = Point(self.limit_max.x, min_y)

        return top_left, bottom_right

    def contains_point(self, point):
        ray_end = Point(self.limit_max.x, point.y)
        strip_idx = self.find_strip_idx_for_point(point)

        if strip_idx is None:
            return False

        intersection_count = 0
        for edge in self.edges_by_strip[strip_idx]:
            if intersects(edge[0], edge[1], point, ray_end):
                intersection_count += 1

        return intersection_count % 2 != 0

    def find_strip_idx_for_point(self, point):
        step = abs(self.limit_max.y - self.limit_min.y) / STRIP_COUNT

        for i in range(STRIP_COUNT):
            min_y = self.limit_min.y + step * i
            max_y = min_y + step

            if min_y <= point.y <= max_y:
                return i

        return None

    def draw_divisions(self, color=White):
        glColor3f(*color)
        glBegin(GL_LINES)

        _, first_top_right = self.get_strip_bbox(0)
        first_a = Point(self.limit_min.x, first_top_right.y)
        first_b = Point(self.limit_max.x, first_top_right.y)

        glVertex3f(first_a.x, first_a.y, 0)
        glVertex3f(first_b.x, first_b.y, 0)

        for i in range(STRIP_COUNT):
            top_left, _ = self.get_strip_bbox(i)

            a = top_left
            b = Point(self.limit_max.x, top_left.y)

            glVertex3f(a.x, a.y, 0)
            glVertex3f(b.x, b.y, 0)

        glEnd()

def get_edges_overlapping_bbox(vertexes, top_left: Point, bottom_right: Point):
    edges = []

    bbox_top_edge_a = top_left
    bbox_top_edge_a = Point(bottom_right.x, bbox_top_edge_a.y)

    bbox_bottom_edge_b = bottom_right
    bbox_bottom_edge_a = Point(top_left.x, bbox_bottom_edge_b.y)

    for i in range(len(vertexes)):
        c = vertexes[i - 1]
        d = vertexes[i]

        c_in_bbox = is_point_in_bbox(top_left, bottom_right, c)
        d_in_bbox = is_point_in_bbox(top_left, bottom_right, d)

        if c_in_bbox or d_in_bbox or intersects(bbox_top_edge_a, bbox_bottom_edge_b, c, d) or intersects(bbox_bottom_edge_a, bbox_bottom_edge_b, c, d):
            edges.append([c, d])

    return edges


def is_point_in_bbox(top_left, bottom_right, point):
    return top_left.x <= point.x <= bottom_right.x and top_left.y >= point.y >= bottom_right.y
