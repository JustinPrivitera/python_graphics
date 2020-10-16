#!/usr/bin/python3

# import sys

# import OpenGL
import OpenGL.GL as GL
import OpenGL.GLUT as GLUT
import OpenGL.GLU as GLU

width = 500
height = 500
x = 0
flag = True;

def iterate():
	GL.glViewport(0, 0, width, height)
	GL.glMatrixMode(GL.GL_PROJECTION)
	GL.glLoadIdentity()
	GL.glOrtho(0.0, width, 0.0, height, 0.0, 1.0)
	GL.glMatrixMode (GL.GL_MODELVIEW)
	GL.glLoadIdentity()

def motion():
	global x, flag
	if x > 100:
		flag = False
	if x < -100:
		flag = True
	if not flag:
		x -= 0.01
	else:
		x += 0.01

def render():
	global x
	GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT) # Remove everything from screen (i.e. displays all white)
	GL.glLoadIdentity() # Reset all graphic/shape's position
	iterate()
	GL.glColor3f(3.0, 0.5, 0.0) # Set the color
	motion()
	square(x) # Draw a square using our function
	GLUT.glutSwapBuffers()

def square(x):
	# We have to declare the points in this sequence: bottom left, bottom right, top right, top left
	GL.glBegin(GL.GL_QUADS) # Begin the sketch
	GL.glVertex3f(100 + x, 100 + x, 0) # Coordinates for the bottom left point
	GL.glVertex3f(200 + x, 100 + x, 0) # Coordinates for the bottom right point
	GL.glVertex3f(200 + x, 200 + x, 0) # Coordinates for the top right point
	GL.glVertex3f(100 + x, 200 + x, 0) # Coordinates for the top left point
	GL.glEnd() # Mark the end of drawing

GLUT.glutInit() # Initialize a glut instance which will allow us to customize our window
GLUT.glutInitDisplayMode(GLUT.GLUT_RGBA) # Set the display mode to be colored
GLUT.glutInitWindowSize(width, height)   # Set the width and height of your window
GLUT.glutInitWindowPosition(0, 0)   # Set the position at which this windows should appear
wind = GLUT.glutCreateWindow("hello triangle") # Give your window a title
GLUT.glutDisplayFunc(render)  # Tell OpenGL to call the render method continuously
GLUT.glutIdleFunc(render)   # Draw any graphics or shapes in the render function at all times
GLUT.glutMainLoop()  # Keeps the window created above displaying/running in a loop
