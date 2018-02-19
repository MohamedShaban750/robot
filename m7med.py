from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
from math import *

def draw():
    glClearColor(1,1,1,1)
    glClear(GL_COLOR_BUFFER_BIT)

    glColor(1,0,0)
    glBegin(GL_POLYGON)
    glVertex2d(0.3,0.3)
    glVertex2d(-0.3,0.3)
    glVertex2d(-0.3,-0.3)
    glVertex2d(0.3,-0.3)
    glEnd()

    glColor(1,1,0)
    glBegin(GL_POLYGON)
    glVertex2d(0.38,0.25)
    glVertex2d(0.3,0.25)
    glVertex2d(0.3,-0.2)
    glVertex2d(0.38,-0.2)
    glEnd()

    glColor(1,1,0)
    glBegin(GL_POLYGON)
    glVertex2d(-0.38,0.25)
    glVertex2d(-0.3,0.25)
    glVertex2d(-0.3,-0.2)
    glVertex2d(-0.38,-0.2)
    glEnd()

    glColor(1,1,0)
    glBegin(GL_POLYGON)
    glVertex2d(-0.05,0.4)
    glVertex2d(0.05,0.4)
    glVertex2d(0.05,0.3)
    glVertex2d(-0.05,0.3)
    glEnd()

    glColor(1,0,1)
    glBegin(GL_POLYGON)
    glVertex2d(-0.15,0.65)
    glVertex2d(0.15,0.65)
    glVertex2d(0.15,0.4)
    glVertex2d(-0.15,0.4)
    glEnd()

    glColor(0,0,1)
    glBegin(GL_POLYGON)
    glVertex2d(0.1,-0.3)
    glVertex2d(0.19,-0.3)
    glVertex2d(0.19,-0.6)
    glVertex2d(0.1,-0.6)
    glEnd()

    glColor(0,0,1)
    glBegin(GL_POLYGON)
    glVertex2d(-0.19,-0.3)
    glVertex2d(-0.1,-0.3)
    glVertex2d(-0.1,-0.6)
    glVertex2d(-0.19,-0.6)
    glEnd()

    glColor(1,1,1)
    glBegin(GL_POLYGON)
    glVertex2d(-0.1,0.47)
    glVertex2d(0.1,0.47)
    glVertex2d(0.1,0.42)
    glVertex2d(-0.1,0.42)
    glEnd()

    glColor(1,0,0)
    glBegin(GL_POLYGON)
    glVertex2d(-0.09,0.46)
    glVertex2d(0.09,0.46)
    glVertex2d(0.09,0.43)
    glVertex2d(-0.09,0.43)
    glEnd()

    glColor(1,1,1)
    glBegin(GL_POLYGON)
    r=.038
    for theta in np.arange(0, 2 * pi ,.01) :
        x= r * cos(theta)+.09
        y= r * sin(theta)+.58
        glVertex2d(x,y)
    glEnd()

    glColor(1,1,1)
    glBegin(GL_POLYGON)
    r=.038
    for theta in np.arange(0, 2 * pi ,.01) :
        x= r * cos(theta)-.09
        y= r * sin(theta)+.58
        glVertex2d(x,y)
    glEnd()

    glColor(0,0,0)
    glBegin(GL_POLYGON)
    r=.02
    for theta in np.arange(0, 2 * pi ,.01) :
        x= r * cos(theta)+.09
        y= r * sin(theta)+.58
        glVertex2d(x,y)
    glEnd()

    glColor(0,0,0)
    glBegin(GL_POLYGON)
    r=.02
    for theta in np.arange(0, 2 * pi ,.01) :
        x= r * cos(theta)-.09
        y= r * sin(theta)+.58
        glVertex2d(x,y)
    glEnd()

    glColor(1,1,1)
    glBegin(GL_POLYGON)
    glVertex2d(0.0,0.58)
    glVertex2d(0.03,0.49)
    glVertex2d(-0.03,0.49)
    glEnd()




    glFlush()

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(600,600)
glutCreateWindow(b"First OpenGL Program")
glutDisplayFunc(draw)
glutMainLoop()
