from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math

cores = ( (1,0,0),(1,1,0),(0,1,0),(0,1,1),(0,0,1),(1,0,1),(0.5,1,1),(1,0,0.5) )
quadro = 0

def desenha():
    global quadro
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    # glTranslatef(1, 0, 0)
    # glRotatef(1,0,0,0)
    glBegin(GL_TRIANGLE_FAN)
    glColor3fv(cores[0])
    glVertex3d(0.02,0.51,0) # primeiro vertice
    raio = 0.7
    for i in range(0,6+7):
        a = (i/6) * 2 * math.pi
        x = raio * math.cos(a)
        y = raio * math.sin(a)
        glColor3fv(cores[(i+1)%len(cores)])
        glVertex2f(x,y)
    glEnd()
    glPopMatrix()
    glutSwapBuffers()
    quadro += 1

# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("PIRAMIDE")
glPushMatrix()
# glRotatef(45,1,0,0)
glutDisplayFunc(desenha)
glPopMatrix()
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
glutMainLoop()