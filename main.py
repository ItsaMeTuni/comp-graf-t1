from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

viewport_min = Point(0, 0)
viewport_max = Point(100, 100)

polygon_vertexes = []

def init():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)

    read_polygon('EstadoRS.txt')

    window = glutCreateWindow("T1 - Lucas Antunes & Henrique Xavier")
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)

    glutMainLoop()


def reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    glOrtho(viewport_min.x, viewport_max.x, viewport_min.y, viewport_max.y, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    draw_polygon(polygon_vertexes)

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
    glColor3f(1,0,0)
    glBegin(GL_LINE_LOOP)
    
    for vertex in vertexes:
        glVertex3f(vertex.x, vertex.y, 0)

    glEnd()



init()
