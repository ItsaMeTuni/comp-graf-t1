from math import sqrt

from point import *

intersects_called = 0
dot_product_called = 0

def reset_profiling():
    global intersects_called
    global dot_product_called

    intersects_called = 0
    dot_product_called = 0

def profiling_result():
    return f'intersects_called {intersects_called} dot_product_called {dot_product_called}'

def intersec2d(k: Point, l: Point, m: Point, n: Point) -> (int, float, float):
    det = (n.x - m.x) * (l.y - k.y) - (n.y - m.y) * (l.x - k.x)

    if (det == 0.0):
        return 0, None, None  # não há intersecção

    s = ((n.x - m.x) * (m.y - k.y) - (n.y - m.y) * (m.x - k.x)) / det
    t = ((l.x - k.x) * (m.y - k.y) - (l.y - k.y) * (m.x - k.x)) / det

    return 1, s, t  # há intersecção


def intersects(k: Point, l: Point, m: Point, n: Point) -> bool:
    global intersects_called
    intersects_called += 1

    ret, s, t = intersec2d(k, l, m, n)

    if not ret: return False

    return 0.0 <= s <= 1.0 and 0.0 <= t <= 1.0


def dot_product(vec_a, vec_b):
    global dot_product_called
    dot_product_called += 1

    return vec_a.x * vec_b.x + vec_a.y * vec_b.y
