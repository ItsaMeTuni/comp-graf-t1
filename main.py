from OpenGL.GLUT import *
import random
from polygon import *
from colors import *

RANDOM_POINTS_COUNT = 1000
POINT_SIZE = 7.0

polygon = None
random_points = []
viewport = {}
convex_hull = None


def init():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA)

    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)

    global polygon
    polygon = read_polygon('EstadoRS.txt')

    create_viewport(polygon.limit_min, polygon.limit_max)
    generate_random_points(RANDOM_POINTS_COUNT)

    global convex_hull
    convex_hull = polygon.get_convex_hull()

    window = glutCreateWindow("T1 - Lucas Antunes & Henrique Xavier")
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)

    glClearColor(*Black, 1)
    glutMainLoop()


def reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(viewport[min].x, viewport[max].x, viewport[min].y, viewport[max].y, 0.0, 1.0)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    polygon.draw(White)
    convex_hull.draw(Blue)
    draw_points(random_points)

    glutSwapBuffers()


def read_polygon(path):
    vertexes = []

    file = open(path)

    # skip first line
    file.readline()

    for line in file:
        words = line.split()
        x = float(words[0])
        y = float(words[1])
        vertexes.append(Point(x, y))

    return Polygon(vertexes)


def create_viewport(limit_min, limit_max):
    viewport[min] = limit_min
    viewport[max] = limit_max

    margin_x = abs(viewport[max].x - viewport[min].x) * 0.1
    margin_y = abs(viewport[max].y - viewport[min].y) * 0.1

    viewport[min].x -= margin_x
    viewport[min].y -= margin_y
    viewport[max].x += margin_x
    viewport[max].y += margin_y


def generate_random_points(count):
    for _ in range(count):
        x = random.uniform(viewport[min].x, viewport[max].x)
        y = random.uniform(viewport[min].y, viewport[max].y)
        random_points.append(Point(x, y))


def draw_points(points):
    glPointSize(POINT_SIZE)
    glColor3f(*Green)
    glBegin(GL_POINTS)

    for point in points:
        if convex_hull.contains_point(point):
            if polygon.contains_point(point):
                glColor3f(*Green)
            else:
                glColor3f(*Yellow)
        else:
            glColor3f(*Red)

        glVertex3f(point.x, point.y, 0)

    glEnd()


init()
