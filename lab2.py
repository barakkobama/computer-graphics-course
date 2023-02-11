import sys
from math import cos,sin,pi

import numpy
from glfw.GLFW import *
from random import random

from OpenGL.GL import *
from OpenGL.GLU import *



def startup():
    glClearColor(0.0,0.0,0.0,1.0)           # Kolor tła po wywołaniu funckji glClear()
    glEnable(GL_DEPTH_TEST)                 # Potrzebne do modelowania w 3d
    update_viewport(None,800,800,-7.5,7.5)  # Zmiana zakresu rysowania 

def shutdown():
    pass

def render(time):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    axes()
    spin(time*180/3.1415)
    #show_egg_points(egg_tab)
    #show_egg_lines(egg_tab)
    
    #show_egg_triangles(egg_tab)
    show_egg_trianglestrip(egg_tab)
    glFlush()


def update_viewport(window,width,height,start,end): #Zmienia zakres rysowania ze [-1.0:1.0] do [start:end]
    if height == 0:
        height = 1
    if width == 0:
        width = 1
    aspectRatio = width/height

    glMatrixMode(GL_PROJECTION)
    glViewport(0,0,width,height)
    glLoadIdentity()

    if width <= height:
        glOrtho(start,end,start/aspectRatio,end/aspectRatio,start,end)
    else:
        glOrtho(start * aspectRatio,end * aspectRatio,start,end,start,end)
    
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def axes():
    glBegin(GL_LINES)

    glColor3f(1.0,0.0,0.0)
    glVertex3f(-5.0,0.0,0.0)
    glVertex3f(5.0,0.0,0.0)
    
    glColor3f(0.0,1.0,0.0)
    glVertex3f(0.0,-5.0,0.0)
    glVertex3f(0.0,5.0,0.0)

    glColor3f(0.0,0.0,1.0)
    glVertex3f(0.0,0.0,-5.0)
    glVertex3f(0.0,0.0,5.0)
    glEnd()


def make_egg(N):
    tab = numpy.zeros((N+1,N+1,3))
    u = []
    v = []
    for i in range(N+1):
        u.append(i/N)
        v.append(i/N)
    for i in range(N+1):
        for j in range(N+1):
            tab[i][j] = [( -90 * u[i]**5 + 225 * u[i]**4 - 270 * u[i]**3 + 180 * u[i]**2 - 45*u[i]) * cos(pi*v[j]),
                            160 * u[i]**4 - 320 * u[i]**3 + 160 * u[i]**2 - 5,
                        ( -90 * u[i]**5 + 225 * u[i]**4 - 270 * u[i]**3 + 180 * u[i]**2 - 45*u[i]) * sin(pi*v[j])]
    return tab

def show_egg_points(tab):
    glBegin(GL_POINTS)
    for i in range(len(tab)):
        for j in range(len(tab)):
            glVertex(tab[i][j])
            
    glEnd()

def show_egg_lines(tab):
    for i in range(len(tab)-1):
        for j in range(len(tab)-1):
            glBegin(GL_LINES)
            glVertex(tab[i][j])
            glVertex(tab[i+1][j])
            glEnd()

            glBegin(GL_LINES)
            glVertex(tab[i][j])
            glVertex(tab[i][j+1])
            glEnd()

def show_egg_triangles(tab):
    for i in range(len(tab)-1):
        for j in range(len(tab)-1):
            glBegin(GL_TRIANGLES)
            glColor3f(0.44, 0.12, 0.0)
            glVertex(tab[i][j])
            glColor3f(0.0, 0.65, 0.3)
            glVertex(tab[i+1][j])
            glColor3f(0.23, 0.0, 0.26)
            glVertex(tab[i][j+1])
            glEnd()

            glBegin(GL_TRIANGLES)
            glVertex(tab[i+1][j])
            glVertex(tab[i][j+1])
            glColor3f(0.91, 0.4, 0.7)
            glVertex(tab[i+1][j+1])
            glEnd()

def show_egg_trianglestrip(tab): 
    N = len(tab)
    for i in range (N):
        if(i+1 < N):
            glBegin(GL_TRIANGLE_STRIP)
            if(i < N/2): glColor3f(0.5, 0.3, 0.0)
            else: glColor3f(0.7, 0.0, 1.0)
            glVertex(tab[i][0])
            for j in range (N-1):
                if(i < N/2): glColor3f(0.7, 0.0, 1.0)
                else: glColor3f(0.5, 0.3, 0.0)
                glVertex(tab[i+1][j])
                if(i < N/2): glColor3f(0.5, 0.3, 0.0)
                else: glColor3f(0.7, 0.0, 1.0)
                glVertex(tab[i][j+1])

            if(i < N/2): glColor3f(0.7, 0.0, 1.0)
            else: glColor3f(0.5, 0.3, 0.0)
            glVertex(tab[i+1][N-1])
            glEnd()


egg_tab = make_egg(60)

def spin(angle):
    glRotatef(angle,1.0,0.0,0.0)
    glRotatef(angle,0.0,1.0,0.0)
    glRotatef(angle,0.0,0.0,1.0)

def main():
    if not glfwInit():
        sys.exit(-1)
    
    window = glfwCreateWindow(800,800,__file__,None, None)
    if not window:
        glfwTerminate()
        sys.exit(-1)
    glfwMakeContextCurrent(window)
    glfwSetFramebufferSizeCallback(window,update_viewport)
    glfwSwapInterval(1)

    startup()
    while not glfwWindowShouldClose(window):
        render(glfwGetTime())
        glfwSwapBuffers(window)
        glfwWaitEvents()
    shutdown()

    glfwTerminate()

if __name__ == '__main__':
    main()