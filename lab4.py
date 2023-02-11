#!/usr/bin/env python3
import sys

from glfw.GLFW import *

from OpenGL.GL import *
from OpenGL.GLU import *



viewer = [0.0, 0.0, 10.0]

theta = 0.0
pix2angle = 1.0

left_mouse_button_pressed = 0
mouse_x_pos_old = 0
delta_x = 0

mat_ambient = [1.0, 1.0, 1.0, 1.0]
mat_diffuse = [1.0, 1.0, 1.0, 1.0]
mat_specular = [1.0, 1.0, 1.0, 1.0]
mat_shininess = 20.0

light_ambient = [0.1, 0.1, 0.0, 1.0]
light_diffuse = [0.8, 0.8, 0.0, 1.0]
light_specular = [1.0, 1.0, 1.0, 1.0]
light_position = [0.0, 0.0, 10.0, 1.0]

light1_ambient = [0.5, 0.2, 0.0, 8.0]
light1_diffuse = [0.1, 0.1, 0.3, 0.5]
light1_specular = [1.0, 1.0, 1.0, 1.0]
light1_postion = [0.0, 1.0, 5.0, 0.0]


att_constant = 1.0
att_linear = 0.05
att_quadratic = 0.001


plus_pressed = 0
minus_pressed = 0
space_pressed = 0


def startup():
    update_viewport(None, 400, 400)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glEnable(GL_DEPTH_TEST)

    glMaterialfv(GL_FRONT, GL_AMBIENT, mat_ambient)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse)
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
    glMaterialf(GL_FRONT, GL_SHININESS, mat_shininess)

    glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)
    glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular)
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)


    glLightfv(GL_LIGHT1, GL_AMBIENT, light1_ambient)
    glLightfv(GL_LIGHT1, GL_DIFFUSE, light1_diffuse)
    glLightfv(GL_LIGHT1, GL_SPECULAR, light1_specular)
    glLightfv(GL_LIGHT1, GL_POSITION, light1_postion)


    glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, att_constant)
    glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, att_linear)
    glLightf(GL_LIGHT0, GL_QUADRATIC_ATTENUATION, att_quadratic)


    glLightf(GL_LIGHT1, GL_CONSTANT_ATTENUATION, att_constant)
    glLightf(GL_LIGHT1, GL_LINEAR_ATTENUATION, att_linear)
    glLightf(GL_LIGHT1, GL_QUADRATIC_ATTENUATION, att_quadratic)


    glShadeModel(GL_SMOOTH)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)

#    glEnable(GL_LIGHT1)


def shutdown():
    pass


def keyboard_key_callback(window, key, scancode, action, mods):
    global plus_pressed
    global minus_pressed
    global space_pressed

    if key == GLFW_KEY_ESCAPE and action == GLFW_PRESS:
        glfwSetWindowShouldClose(window, GLFW_TRUE)
    
    if key == GLFW_KEY_EQUAL and action == GLFW_PRESS:
        plus_pressed = 1
    else:
        plus_pressed = 0
    
    if key == GLFW_KEY_MINUS and action == GLFW_PRESS:
        minus_pressed = 1
    else:
        minus_pressed = 0

    if key == GLFW_KEY_SPACE and action == GLFW_PRESS:
        space_pressed +=1
        if space_pressed == 30:
            space_pressed = 0
def render(time):
    global theta
    change = 0 
    global plus_pressed
    global minus_pressed
    global space_pressed
    global mat_shininess

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    if plus_pressed:
         change = 0.1
    if minus_pressed:
        change = -0.1

    if space_pressed < 4:
        mat_ambient[space_pressed%4] += change
        print("mat_ambient",space_pressed%4,mat_ambient[space_pressed%4])
    elif space_pressed < 8:
        mat_diffuse[space_pressed%4] += change
        print("mat_diffuse",space_pressed%4,mat_diffuse[space_pressed%4])
    elif space_pressed < 12:
        mat_specular[space_pressed%4] += change
        print("mat_spectular",space_pressed%4,mat_specular[space_pressed%4])
    elif space_pressed < 13:
        mat_shininess +=change
        print("mat_shininess",space_pressed%4,mat_shininess)
    elif space_pressed < 17:
        if 0.0<light_ambient[space_pressed%4]<1.0:
            light_ambient[space_pressed%4] +=change
            print("light_ambient",space_pressed%4,light_ambient[space_pressed%4])
    elif space_pressed < 21:
        if 0.0<light_diffuse[space_pressed%4]<1.0:
            light_diffuse[space_pressed%4] +=change
            print("light_diffuse",space_pressed%4,light_diffuse[space_pressed%4])
    elif space_pressed < 25:
        light_specular[space_pressed%4] =(light_specular[space_pressed%4] + change
        print("light_specular",space_pressed%4,light_specular[space_pressed%4])
    elif space_pressed < 29:
        light_position[space_pressed%4] +=change
        print("light_position",space_pressed%4,light_position[space_pressed%4])
    
    
        


    gluLookAt(viewer[0], viewer[1], viewer[2],
              0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

    if left_mouse_button_pressed:
        theta += delta_x * pix2angle

    glRotatef(theta, 0.0, 1.0, 0.0)

    quadric = gluNewQuadric()
    gluQuadricDrawStyle(quadric, GLU_FILL)
    gluSphere(quadric, 3.0, 10, 10)
    gluDeleteQuadric(quadric)

    glFlush()


def update_viewport(window, width, height):
    global pix2angle
    pix2angle = 360.0 / width

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    gluPerspective(70, 1.0, 0.1, 300.0)

    if width <= height:
        glViewport(0, int((height - width) / 2), width, width)
    else:
        glViewport(int((width - height) / 2), 0, height, height)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def mouse_motion_callback(window, x_pos, y_pos):
    global delta_x
    global mouse_x_pos_old

    delta_x = x_pos - mouse_x_pos_old
    mouse_x_pos_old = x_pos


def mouse_button_callback(window, button, action, mods):
    global left_mouse_button_pressed

    if button == GLFW_MOUSE_BUTTON_LEFT and action == GLFW_PRESS:
        left_mouse_button_pressed = 1
    else:
        left_mouse_button_pressed = 0


def main():
    if not glfwInit():
        sys.exit(-1)

    window = glfwCreateWindow(400, 400, __file__, None, None)
    if not window:
        glfwTerminate()
        sys.exit(-1)

    glfwMakeContextCurrent(window)
    glfwSetFramebufferSizeCallback(window, update_viewport)
    glfwSetKeyCallback(window, keyboard_key_callback)
    glfwSetCursorPosCallback(window, mouse_motion_callback)
    glfwSetMouseButtonCallback(window, mouse_button_callback)
    glfwSwapInterval(1)

    startup()
    while not glfwWindowShouldClose(window):
        render(glfwGetTime())
        glfwSwapBuffers(window)
        glfwPollEvents()
    shutdown()

    glfwTerminate()


if __name__ == '__main__':
    main()