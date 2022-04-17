from math import sqrt

ABOVE = 'above'
BELOW = 'below'

def quickhull(vertexes):
    convex_hull = []

    vertexes = sort_x_axis(vertexes)

    # left most vertex
    v1 = vertexes[0]
    #right most vertex
    v2 = vertexes[-1]

    vertexes.pop(0)
    vertexes.pop(-1)

    above, below = create_segment(v1, v2, vertexes)

    top_hull = _quickhull(v1, v2, above, ABOVE)
    bottom_hull = _quickhull(v1, v2, below, BELOW)

    convex_hull += [
        v1,
        *sort_x_axis(top_hull),
        v2,
        *sort_x_axis(bottom_hull)[::-1]
    ]

    return convex_hull


def create_segment(v1, v2, vertexes):
    above = []
    below = []

    # vertical line
    if v1.x == v2.x:
        return above, below
    
    # y = mx + c
    m = (v2.y - v1.y) / (v2.x - v1.x)
    c =  - m * v1.x + v1.y

    for vertex in vertexes:
        # y > mx + c (above)
        if vertex.y > m * vertex.x + c:
            above.append(vertex)
        
        # y < mx + c (below)
        if vertex.y < m * vertex.x + c:
            below.append(vertex)

    return above, below


def _quickhull(v1, v2, segment, position):
    if segment == [] or v1 is None or v2 is None:
        return []

    convex_hull = []

    farthest_distance = -1
    farthest_vertex = None
    for vertex in segment:
        distance = calculate_distance(v1, v2, vertex)
        if distance > farthest_distance:
            farthest_distance = distance
            farthest_vertex = vertex

    convex_hull.append(farthest_vertex)

    segment.remove(farthest_vertex)

    above1, below1 = create_segment(v1, farthest_vertex, segment)
    above2, below2 = create_segment(v2, farthest_vertex, segment)

    if position == ABOVE:
        convex_hull += _quickhull(v1, farthest_vertex, above1, ABOVE)
        convex_hull += _quickhull(farthest_vertex, v2, above2, ABOVE)
    
    if position == BELOW:
        convex_hull += _quickhull(v1, farthest_vertex, below1, BELOW)
        convex_hull += _quickhull(farthest_vertex, v2, below2, BELOW)

    return convex_hull


def calculate_distance(v1, v2, v3):
    # ax + by + c = 0
    a = v1.y - v2.y
    b = v2.x - v1.x
    c = v1.x*v2.y - v2.x*v1.y


    return abs(a*v3.x + b*v3.y + c) / sqrt(a*a + b*b)

def sort_x_axis(vertexes):
    return sorted(vertexes, key=lambda point: point.x)
    

