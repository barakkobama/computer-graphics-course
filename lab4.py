#!/usr/bin/env python3
import sys
from math import cos,pi,sin

from glfw.GLFW import *

from OpenGL.GL import *
from OpenGL.GLU import *


viewer = [0.0, 0.0, 10.0]

theta = 0.0
phi = 0.0
pix2angle = 1.0

left_mouse_button_pressed = 0
mouse_x_pos_old = 0
mouse_y_pos_old = 0
delta_x = 0
delta_y = 0

mat_ambient = [1.0, 1.0, 1.0, 1.0]
mat_diffuse = [1.0, 1.0, 1.0, 1.0]
mat_specular = [1.0, 1.0, 1.0, 1.0]
mat_shininess = 20.0

light_ambient = [0.1, 0.1, 0.0, 1.0]
light_diffuse = [0.8, 0.8, 0.0, 1.0]
light_specular = [1.0, 1.0, 1.0, 1.0]
light_position = [0.0, 0.0, 10.0, 1.0]

light_ambient1 = [0.5, 0.5, 0.3, 1.0]
light_diffuse1 = [0.1, 0.1, 0.8, 1.0]
light_specular1 = [1.0, 1.0, 1.0, 1.0]
light_position1 = [0.0, 10.0, 0.0, 1.0]

att_constant = 1.0
att_linear = 0.05
att_quadratic = 0.001

material = 0
light = 0
ambient = 0
diffuse = 0
specular = 0
down = 0
up = 0


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

    glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, att_constant)
    glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, att_linear)
    glLightf(GL_LIGHT0, GL_QUADRATIC_ATTENUATION, att_quadratic)


    glLightfv(GL_LIGHT1, GL_AMBIENT, light_ambient1)
    glLightfv(GL_LIGHT1, GL_DIFFUSE, light_diffuse1)
    glLightfv(GL_LIGHT1, GL_SPECULAR, light_specular1)
    glLightfv(GL_LIGHT1, GL_POSITION, light_position1)

    glLightf(GL_LIGHT1, GL_CONSTANT_ATTENUATION, att_constant)
    glLightf(GL_LIGHT1, GL_LINEAR_ATTENUATION, att_linear)
    glLightf(GL_LIGHT1, GL_QUADRATIC_ATTENUATION, att_quadratic)

    glShadeModel(GL_SMOOTH)
    glEnable(GL_LIGHTING)
    #glEnable(GL_LIGHT1)
    glEnable(GL_LIGHT0)


def shutdown():
    pass


def render(time):
    global theta
    global ambient
    global diffuse
    global specular
    global up
    global down
    global light
    global material
    global phi
    global light_position

    if material:
        if ambient:
            if up:
                if mat_ambient[0] < 1.0:
                    mat_ambient[0] += 0.01
                    mat_ambient[1] += 0.01
                    mat_ambient[2] += 0.01
                    mat_ambient[3] += 0.01
            if down:
                if mat_ambient[0] > 0.0:
                    mat_ambient[0] -= 0.01
                    mat_ambient[1] -= 0.01
                    mat_ambient[2] -= 0.01
                    mat_ambient[3] -= 0.01
        if diffuse:
            if up:
                if mat_diffuse[0] < 1.0:
                    mat_diffuse[0] += 0.01
                    mat_diffuse[1] += 0.01
                    mat_diffuse[2] += 0.01
                    mat_diffuse[3] += 0.01
            if down:
                if mat_diffuse[0] > 0.0:
                    mat_diffuse[0] -= 0.01
                    mat_diffuse[1] -= 0.01
                    mat_diffuse[2] -= 0.01
                    mat_diffuse[3] -= 0.01

        if specular:
            if up:
                if mat_specular[0] < 1.0:
                    mat_specular[0] += 0.01
                    mat_specular[1] += 0.01
                    mat_specular[2] += 0.01
                    mat_specular[3] += 0.01
            if down:
                if mat_specular[0] > 0.0:
                    mat_specular[0] -= 0.01
                    mat_specular[1] -= 0.01
                    mat_specular[2] -= 0.01
                    mat_specular[3] -= 0.01

    if light:
        if ambient:
            if up:
                if light_ambient[0] < 1.0:
                    light_ambient[0] += 0.01
                    light_ambient[1] += 0.01
                    light_ambient[2] += 0.01
                    light_ambient[3] += 0.01
            if down:
                if light_ambient[0] > 0.0:
                    light_ambient[0] -= 0.01
                    light_ambient[1] -= 0.01
                    light_ambient[2] -= 0.01
                    light_ambient[3] -= 0.01
        if diffuse:
            if up:
                if light_diffuse[0] < 1.0:
                    light_diffuse[0] += 0.01
                    light_diffuse[1] += 0.01
                    light_diffuse[2] += 0.01
                    light_diffuse[3] += 0.01
            if down:
                if light_diffuse[0] > 0.0:
                    light_diffuse[0] -= 0.01
                    light_diffuse[1] -= 0.01
                    light_diffuse[2] -= 0.01
                    light_diffuse[3] -= 0.01

        if specular:
            if up:
                if light_specular[0] < 1.0:
                    light_specular[0] += 0.01
                    light_specular[1] += 0.01
                    light_specular[2] += 0.01
                    light_specular[3] += 0.01
            if down:
                if light_specular[0] > 0.0:
                    light_specular[0] -= 0.01
                    light_specular[1] -= 0.01
                    light_specular[2] -= 0.01
                    light_specular[3] -= 0.01


    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    gluLookAt(viewer[0], viewer[1], viewer[2],
              0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

    if left_mouse_button_pressed:
        theta += delta_x * pix2angle
        phi += delta_y * pix2angle

    glRotatef(theta, 0.0, 1.0, 0.0)


    glMaterialfv(GL_FRONT, GL_AMBIENT, mat_ambient)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse)
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
    glMaterialf(GL_FRONT, GL_SHININESS, mat_shininess)
    
    glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)
    glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular)
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)

    quadric = gluNewQuadric()
    gluQuadricDrawStyle(quadric, GLU_FILL)
    gluSphere(quadric, 3.0, 10, 10)
    gluDeleteQuadric(quadric)

    '''quadric = gluNewQuadric()
    gluQuadricDrawStyle(quadric, GLU_LINE)
    gluSphere(quadric, 3.0, 6, 5)
    gluDeleteQuadric(quadric)
'''
    x_s = cos(phi * pi/180) * cos(theta * pi/180)
    y_s = sin(phi * pi/180)
    z_s = sin(theta * pi/180) * cos(phi * pi/180)

    glTranslate(x_s.real, y_s.real, z_s.real)

    light_position = (-x_s.real, -y_s.real, -z_s.real)

    glLightfv(GL_LIGHT0, GL_POSITION, light_position)

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


def keyboard_key_callback(window, key, scancode, action, mods):
    global ambient
    global diffuse
    global specular
    global up
    global down
    global light
    global material

    if key == GLFW_KEY_ESCAPE and action == GLFW_PRESS:
        glfwSetWindowShouldClose(window, GLFW_TRUE)

    if key == GLFW_KEY_M and action == GLFW_PRESS:
        material = 1
        light = 0

    if key == GLFW_KEY_L and action == GLFW_PRESS:
        material = 0
        light  = 1

    if key == GLFW_KEY_A and action == GLFW_PRESS:
        ambient = 1
        diffuse = 0
        specular = 0
    if key == GLFW_KEY_D and action == GLFW_PRESS:
        ambient = 0
        diffuse = 1
        specular = 0
    if key == GLFW_KEY_S and action == GLFW_PRESS:
        ambient = 0
        diffuse = 0
        specular = 1

    if key == GLFW_KEY_UP and action == GLFW_PRESS:
        up = 1
        down = 0

    if key == GLFW_KEY_DOWN and action == GLFW_PRESS:
        up = 0
        down = 1

def mouse_motion_callback(window, x_pos, y_pos):
    global delta_x
    global mouse_x_pos_old
    global delta_y
    global mouse_y_pos_old


    delta_x = x_pos - mouse_x_pos_old
    mouse_x_pos_old = x_pos
    delta_y = y_pos - mouse_y_pos_old
    mouse_y_pos_old = y_pos 

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