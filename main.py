#!/usr/bin/python3

import sys
from random import *

# import OpenGL
import OpenGL.GL as GL
import OpenGL.GLUT as GLUT
import OpenGL.GLU as GLU
import glfw
from vec3 import *
from scene_objs import *
import config

# width = 1400
# height = 1000

shapes = []

lasttime = 0

def get_last_elapsed_time():
	global lasttime
	# lasttime = glfwget_time()
	actualtime = glfw.get_time()
	difference = actualtime - lasttime
	lasttime = actualtime
	return difference	

def update(frametime):
	global shapes
	for i in range(0, len(shapes)):
		shapes[i].update(frametime)

def render():
	frametime = get_last_elapsed_time()
	update(frametime)

	print("framerate: " + str(round(1 / frametime)) + "      ", end = "\r")

	GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT) # Remove everything from screen (i.e. displays all white)
	GL.glLoadIdentity() # Reset all graphic/shape's position

	GL.glViewport(0, 0, config.width, config.height)
	# GL.glMatrixMode(GL.GL_PROJECTION) # no matrices necessary right now
	# GL.glLoadIdentity()
	GL.glOrtho(0.0, config.width, 0.0, config.height, 0.0, 1.0)
	# GL.glMatrixMode (GL.GL_MODELVIEW) # no matrices necessary right now
	# GL.glLoadIdentity()

	for i in range(0, len(shapes)):
		shapes[i].draw()

	GLUT.glutSwapBuffers()

def init():
	global lasttime
	global shapes
	# glfw.init()
	if not glfw.init():
		return
	lasttime = glfw.get_time()

	config.width = 1400
	config.height = 1000

	if (config.mode == 1):
		shapes = make_squares(50)

	GLUT.glutInit() # Initialize a glut instance which will allow us to customize our window
	GLUT.glutInitDisplayMode(GLUT.GLUT_RGBA) # Set the display mode to be colored
	GLUT.glutInitWindowSize(config.width, config.height)   # Set the width and height of your window
	GLUT.glutInitWindowPosition(0, 0)   # Set the position at which this windows should appear
	

def main():
	# default setup
	scene_name = "squares demo"
	config.mode = 1

	if (len(sys.argv) == 2):
		if (sys.argv[1] == "0"):
			scene_name = "hello triangle"
			config.mode = 0
			print("not yet implemented")
			return
		elif (sys.argv[1] == "1"):
			scene_name = "squares demo"
			config.mode = 1
		elif (sys.argv[1] == "2"):
			scene_name = "galaxy demo"
			config.mode = 2
			print("not yet implemented")
			return
		else:
			print("scene does not exist")
			return

	init()

	wind = GLUT.glutCreateWindow(scene_name) # Give your window a title
	GLUT.glutDisplayFunc(render)  # Tell OpenGL to call the render method continuously
	GLUT.glutIdleFunc(render)   # Draw any graphics or shapes in the render function at all times
	GLUT.glutMainLoop()  # Keeps the window created above displaying/running in a loop

main()

# add spin?
# go 3d
# add shaders
