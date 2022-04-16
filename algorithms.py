from point import *

def slope(a, b):
    return (a.y - b.y) / (a.x - b.x)

def cross(a, b):
    return a.x*b.y - a.y*b.x

def intersects_old(segment_1, segment_2):
    a = segment_1[0]
    b = segment_1[1]
    c = segment_2[0]
    d = segment_2[1]

    ab = b - a
    cd = d - c

    ab_cross_cd = cross(ab, cd)

    if ab_cross_cd == 0:
        return false
    else:
        ac = c - a
        t1 = cross(ac, cd) / ab_cross_cd
        t2 = (cross(ab, ac) * -1) / ab_cross_cd

        return t1 >= 0 and t1 <= 1 and t2 >= 0 and t2 <= 1


def intersec2d(k: Point, l: Point, m: Point, n: Point) -> (int, float, float):
    det = (n.x - m.x) * (l.y - k.y)  -  (n.y - m.y) * (l.x - k.x)

    if (det == 0.0):
        return 0, None, None # não há intersecção

    s = ((n.x - m.x) * (m.y - k.y) - (n.y - m.y) * (m.x - k.x))/ det
    t = ((l.x - k.x) * (m.y - k.y) - (l.y - k.y) * (m.x - k.x))/ det

    return 1, s, t # há intersecção

def intersects(k: Point, l: Point, m: Point, n: Point) -> bool:
    ret, s, t = intersec2d( k,  l,  m,  n)

    if not ret: return False

    return s>=0.0 and s <=1.0 and t>=0.0 and t<=1.0

