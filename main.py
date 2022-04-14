from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
from point import Point

RANDOM_POINTS_COUNT = 10
POINT_SIZE = 3.0

RED = (1.0, 0.0, 0.0)
GREEN = (0.0, 1.0, 0.0)
WHITE = (1.0, 1.0, 1.0)
BLACK = (0.0, 0.0, 0.0)

polygon_vertexes = []
random_points = []
viewport = {}


def init():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA)

    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)

    read_polygon('PoligonoDeTeste.txt')
    create_viewport()
    create_random_points(RANDOM_POINTS_COUNT)

    window = glutCreateWindow("T1 - Lucas Antunes & Henrique Xavier")
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)

    glClearColor(*BLACK, 0)

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
    
    draw_polygon(polygon_vertexes)
    draw_points(random_points)

    glutSwapBuffers()


def read_polygon(path):
    file = open(path)
    
    # skip first line
    file.readline()

    for line in file:
        words = line.split()
        x = float(words[0])
        y = float(words[1])
        polygon_vertexes.append(Point(x, y))


def draw_polygon(vertexes):
    glColor3f(*WHITE)
    glBegin(GL_LINE_LOOP)
    
    for vertex in vertexes:
        glVertex3f(vertex.x, vertex.y, 0)

    glEnd()


def create_viewport():
    viewport[min], viewport[max] = get_polygon_limits(polygon_vertexes)

    margin_x = abs(viewport[max].x - viewport[min].x)*0.1
    margin_y = abs(viewport[max].y - viewport[min].y)*0.1

    viewport[min].x -= margin_x 
    viewport[min].y -= margin_y
    viewport[max].x += margin_x 
    viewport[max].y += margin_y


def get_polygon_limits(vertexes):
    x_points = [vertex.x for vertex in vertexes]
    y_points = [vertex.y for vertex in vertexes]

    min_point = Point(min(x_points), min(y_points))
    max_point = Point(max(x_points), max(y_points))

    return min_point, max_point


def create_random_points(count):
    for _ in range(count):
        x = random.uniform(viewport[min].x, viewport[max].x)
        y = random.uniform(viewport[min].y, viewport[max].y)
        random_points.append(Point(x, y))


def draw_points(points):
    glColor3f(*GREEN)
    glPointSize(POINT_SIZE)
    glBegin(GL_POINTS)

    for point in points:
        glVertex3f(point.x, point.y, 0)

    glEnd()

init()
