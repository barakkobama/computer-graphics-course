import sys

from glfw.GLFW import *
from random import random

from OpenGL.GL import *
from OpenGL.GLU import *


def triangle():
    glColor3f(0.0, 1.0, 0.0)
    glBegin(GL_TRIANGLES)
    glVertex2f(-100.0, -100.0)
    glColor3f(1.0,0.0,0.0)
    glVertex2f(100.0, -100.0)
    glColor3f(0.0,0.0,1.0)
    glVertex2f(0.0, 100.0)
    glEnd()

def rectangle(x,y,a,b):
    glColor3f(0.54,0.12,0.23)
    glBegin(GL_TRIANGLES)
    glVertex2f(x,y)
    glVertex2f(x+a,y)
    glVertex2f(x,y+b)
    glEnd()
    glBegin(GL_TRIANGLES)
    glVertex2f(x+a,y)
    glVertex2f(x+a,y+b)
    glVertex2f(x,y+b)
    glEnd()

def rectangle_w(x,y,a,b):
    glColor3f(0.0,0.0,0.0)
    glBegin(GL_TRIANGLES)
    glVertex2f(x,y)
    glVertex2f(x+a,y)
    glVertex2f(x,y+b)
    glEnd()
    glBegin(GL_TRIANGLES)
    glVertex2f(x+a,y)
    glVertex2f(x+a,y+b)
    glVertex2f(x,y+b)
    glEnd()




def dis_rec(x,y,a,b,d = 0.0):

    
    if(d):
        a *= d
        b *= d
        x *= d
        y *= d

    glBegin(GL_TRIANGLES)
    glColor3f(random(),random(),random())
    glVertex2f(x,y)
    glColor3f(random(),random(),random())
    glVertex2f(x+a,y)
    glColor3f(random(),random(),random())
    glVertex2f(x,y+b)
    glEnd()
    glBegin(GL_TRIANGLES)
    glVertex2f(x+a,y)
    glColor3f(random(),random(),random())
    glVertex2f(x+a,y+b)
    glVertex2f(x,y+b)
    glEnd()

def carpet(x, y, a, b, depth):
    if depth == 0:
        rectangle_w(x, y, a, b)
    else:
        depth-=1 
        new_a = a/3
        new_b = b/3

        for m in range(3):
            for n in range(3):
                if m!=1 or n!=1:
                    newY = y - new_b + n * new_b
                    newX = x - new_a + m * new_a
                    carpet(newX, newY, new_a, new_b, depth)
        

def startup():
    glClearColor(0.5,0.5,0.5,1.0)  #Kolor tła po wywołaniu funckji glClear()
    update_viewport(None,400,400)

def shutdown():
    pass

def render(time):
    glClear(GL_COLOR_BUFFER_BIT)
    #triangle()
    #rectangle(-50,-50,100,120)
   #dis_rec(-50,-50,100,120,0.4)

    carpet(0,0,150,150,4)
    

    glFlush()

def update_viewport(window,width,height): #zmienia zakres rysowania ze [-1.0:1.0] do [-100.0:100.0]
    if height == 0:
        height = 1
    if width == 0:
        width = 1
    aspectRatio = width/height

    glMatrixMode(GL_PROJECTION)
    glViewport(0,0,width,height)
    glLoadIdentity()

    if width <= height:
        glOrtho(-100.0,100.0,-100.0/aspectRatio,100.0/aspectRatio,1.0,-1.0)
    else:
        glOrtho(-100.0 * aspectRatio,100.0 * aspectRatio,-100.0,100.0,1.0,-1.0)
    
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def main():
    if not glfwInit():
        sys.exit(-1)
    
    window = glfwCreateWindow(400,400,__file__,None, None)
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