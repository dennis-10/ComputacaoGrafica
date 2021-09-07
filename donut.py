from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math

r = 1
n = 50
halfpi = math.pi/2
R = 2

# a partir de uma esfera faço os circulos
def f(u, v):
    # angulo theta cresce a cada valor de n
    theta = (u*2*math.pi)/(n-1) # u é o meu x

    # angulo phi move a cada valor de n
    phi = (v*2*math.pi)/(n-1)

    # posicao de x,y,z no circulo com raio phi é calculado a partir do com raio tetha
    # a partir do raio do circulo 1, 
    x = (R + r*math.cos(theta))*math.cos(phi)
    y = (R + r*math.cos(theta))*math.sin(phi)
    z = r*math.sin(theta)
    return x, y, z

def desenhaEsfera():
    for i in range(n):
        glBegin(GL_TRIANGLE_STRIP)
        for j in range(n):
            glVertex3fv(f(i,j))
            glVertex3fv(f(i+1,j))
        glEnd()

a = 0

def desenha():
    global a
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    glRotatef(a,0,1,0)
    desenhaEsfera()    
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
glutCreateWindow("Esfera")
glutDisplayFunc(desenha)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(45,800.0/600.0,0.1,100.0)
glTranslatef(0.0,0.0,-8)
glutTimerFunc(50,timer,1)
glutMainLoop()


