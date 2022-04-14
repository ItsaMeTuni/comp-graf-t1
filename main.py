from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from point import Point

viewport_min = Point(0, 0)
viewport_max = Point(15, 8)

polygon_vertexes = []
viewport = {}

def init():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA)

    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)

    read_polygon('PoligonoDeTeste.txt')
    create_viewport()

    window = glutCreateWindow("T1 - Lucas Antunes & Henrique Xavier")
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)

    glClearColor(0, 0, 1, 1)

    glutMainLoop()


def reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    margin_x = abs(viewport[max].x - viewport[min].x)*0.1
    margin_y = abs(viewport[max].y - viewport[min].y)*0.1
    glOrtho(viewport[min].x-margin_x, viewport[max].x+margin_x, viewport[min].y-margin_y, viewport[max].y+margin_y, 0.0, 1.0)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    # glClearColor(0, 0, 1, 1)
    
    draw_polygon(polygon_vertexes)

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
    glColor3f(1,0,0)
    glBegin(GL_LINE_LOOP)
    
    for vertex in vertexes:
        glVertex3f(vertex.x, vertex.y, 0)

    glEnd()

def create_viewport():
    viewport[min], viewport[max] = get_polygon_limits(polygon_vertexes)

def get_polygon_limits(vertexes):
    x_points = [vertex.x for vertex in vertexes]
    y_points = [vertex.y for vertex in vertexes]

    min_point = Point(min(x_points), min(y_points))
    max_point = Point(max(x_points), max(y_points))

    return min_point, max_point



init()
