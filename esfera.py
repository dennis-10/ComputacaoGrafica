from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math

r = 1
n = 50
halfpi = math.pi/2

def f(i, j):
    # angulo theta cresce a cada valor de n
    # a cada iteracao o meu pi que esta quebrando em 49 partes cresce
    # assim o angulo vai aumentando
    # como quero que cresca de -pi/2 ate pi/2 e nao de 0 ate pi, diminuo pela metade de pi
    theta = (i*math.pi/(n-1))-halfpi # se remover halfpi fica o circulo pela metade
    
    # anggulo phi que gira no eixo y
    phi = (j*2*math.pi)/(n-1) # de fato quero comecar de 0, e dessa vez terminar em 2pi para fazer 1 circulo
    
    # calculos de x,y,z conforme mostrado na aula
    x = r*math.cos(theta)*math.cos(phi)
    y = r*math.sin(theta)
    z = r*math.cos(theta)*math.sin(phi)
    return x, y, z

def desenhaEsfera():
    for i in range(n): # i anda no angulo theta
        glBegin(GL_TRIANGLE_STRIP)
        for j in range(n): # j anda no angulo phi e faz o circulo horizontal c 360º
            glVertex3fv(f(i,j)) # recebe de volta x,y,z
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


