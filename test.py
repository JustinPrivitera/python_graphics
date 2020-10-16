#!/usr/bin/python3

import sys

# import OpenGL
import OpenGL.GL as GL
import OpenGL.GLUT as GLUT
import OpenGL.GLU as GLU

width = 500
height = 500

def iterate():
	GL.glViewport(0, 0, width, height)
	GL.glMatrixMode(GL.GL_PROJECTION)
	GL.glLoadIdentity()
	GL.glOrtho(0.0, width, 0.0, height, 0.0, 1.0)
	GL.glMatrixMode (GL.GL_MODELVIEW)
	GL.glLoadIdentity()

def showScreen():
	GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT) # Remove everything from screen (i.e. displays all white)
	GL.glLoadIdentity() # Reset all graphic/shape's position
	iterate()
	GL.glColor3f(1.0, 0.0, 3.0) # Set the color to pink
	square() # Draw a square using our function
	GLUT.glutSwapBuffers()

def square():
	# We have to declare the points in this sequence: bottom left, bottom right, top right, top left
	GL.glBegin(GL.GL_QUADS) # Begin the sketch
	GL.glVertex2f(100, 100) # Coordinates for the bottom left point
	GL.glVertex2f(200, 100) # Coordinates for the bottom right point
	GL.glVertex2f(200, 200) # Coordinates for the top right point
	GL.glVertex2f(100, 200) # Coordinates for the top left point
	GL.glEnd() # Mark the end of drawing

GLUT.glutInit() # Initialize a glut instance which will allow us to customize our window
GLUT.glutInitDisplayMode(GLUT.GLUT_RGBA) # Set the display mode to be colored
GLUT.glutInitWindowSize(width, height)   # Set the width and height of your window
GLUT.glutInitWindowPosition(0, 0)   # Set the position at which this windows should appear
wind = GLUT.glutCreateWindow("hello triangle") # Give your window a title
GLUT.glutDisplayFunc(showScreen)  # Tell OpenGL to call the showScreen method continuously
GLUT.glutIdleFunc(showScreen)   # Draw any graphics or shapes in the showScreen function at all times
GLUT.glutMainLoop()  # Keeps the window created above displaying/running in a loop
