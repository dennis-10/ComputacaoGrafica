from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import numpy as np

x0 = -1
xn = 1

y0 = -1
yn = 1

n = 50
dx = (xn - x0)/n
dy = (yn - y0)/n

def f2(x,y):
    # Paraboloide Circular
    return x**2+y**2 # para cima

def f(x,y):
    # Paraboloide Circular
    return x**2-y**2 # para baixo

# cores de verde para azul
def cor (t, c1 = np.array([0,1,0]), c2 = np.array([0,0,1])):
    return c1 + t*(c2 - c1)

def desenhaSuperficie():
    
    y = y0 # posicao inicial de y, que vai andar conforme dy na vertical
    
    for i in range(n):
        x = x0 # posicao inicial de x, anda conforme dx
        glBegin(GL_TRIANGLE_STRIP) # tipo primitivo
        for j in range(n):    
            # indica a cor para o ponto
            glColor3fv(cor(j/(n-1)))

            z = f(x, y)
            z2 = f(x,y + dy)

            glVertex3f(x, y, z) # desenha primeiro vertice
            glVertex3f(x, y + dy, z2) # desenha segundo vertice
            x += dx
        y += dy

        glEnd()

a = 0

def desenhaSuperficie2():
    
    y = y0
    
    for i in range(n):
        glBegin(GL_TRIANGLE_STRIP)
        x = x0
        for j in range(n):
            z = f2(x, y)
            z2 = f2(x,y + dy)
            glColor3fv(cor(j/(n-1)))

            glVertex3f(x, y, z)
            glVertex3f(x, y + dy, z2)
            x += dx
        y += dy

        glEnd()

def desenha():
    global a
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glPushMatrix()

    glTranslate(-3, 3, 0)
    glRotatef(-a,1,0,0)
    desenhaSuperficie()
    
    glPopMatrix()
    glPushMatrix()
    
    glTranslate(3, -3, 0)
    glRotatef(-a,1,0,0)
    desenhaSuperficie2()
    
    glPopMatrix()
    glutSwapBuffers()
    a += 1
 
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)

# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("Superficie")
glutDisplayFunc(desenha)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(45,800.0/600.0,0.1,100.0)
glTranslatef(0.0,0.0,-15)
glutTimerFunc(50,timer,1)
glutMainLoop()


