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
	domath()
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

def domath():
	global shapes
	if config.mode == config.GALAXY_DEMO:
		for i in range(0, len(shapes)):
			acceleration = vec3()
			for j in range(0, len(shapes)):
				if i != j:
					vect = shapes[j].pos - shapes[i].pos
					dist = vect.magnitude()
					vect.normalize()
					mass = 1
					if dist > 1:
						acceleration = acceleration + vect * (config.G * mass / (dist * dist))
			shapes[i].acceleration = acceleration

def init_geom():
	global shapes
	if config.mode == config.HELLO_TRIANGLE:
		a = vec3(100, 100, 0)
		b = vec3(300, 100, 0)
		c = vec3(200, 300, 0)
		velocity = vec3(50,50,0)
		color = vec3(0.8, 0.8, 0.0)
		shapes.append(triangle(a, b, c, velocity, color))
	elif config.mode == config.SQUARES_DEMO:
		shapes = make_squares(50)
	elif config.mode == config.POINTS_DEMO:
		shapes = make_points(1000)
	elif config.mode == config.PHYSICAL_POINTS_DEMO:
		shapes = make_physical_points(1000)
	elif config.mode == config.GALAXY_DEMO:
		shapes = make_points(100, 0, 600, 800, 400, 600)

def init():
	global lasttime
	if not glfw.init():
		return False
	lasttime = glfw.get_time()

	config.width = 1400
	config.height = 1000

	# default setup
	config.scene_name = "squares demo"
	config.mode = config.SQUARES_DEMO

	if (len(sys.argv) == 2):
		if (sys.argv[1] == "0"):
			config.scene_name = "hello triangle"
			config.mode = config.HELLO_TRIANGLE
		elif (sys.argv[1] == "1"):
			config.scene_name = "squares demo"
			config.mode = config.SQUARES_DEMO
		elif (sys.argv[1] == "2"):
			config.scene_name = "points demo"
			config.mode = config.POINTS_DEMO
		elif (sys.argv[1] == "3"):
			config.scene_name = "physical points demo"
			config.mode = config.PHYSICAL_POINTS_DEMO
		elif (sys.argv[1] == "4"):
			config.scene_name = "galaxy demo"
			config.mode = config.GALAXY_DEMO
		else:
			print("scene does not exist")
			return

	init_geom()

	if not GLUT.glutInit(): # Initialize a glut instance which will allow us to customize our window
		return False
	GLUT.glutInitDisplayMode(GLUT.GLUT_RGBA) # Set the display mode to be colored
	GLUT.glutInitWindowSize(config.width, config.height)   # Set the width and height of your window
	GLUT.glutInitWindowPosition(0, 0)   # Set the position at which this windows should appear

	return True

def main():
	if not init():
		print("initialization failed")
		return

	window = GLUT.glutCreateWindow(config.scene_name) # Give your window a title
	GLUT.glutDisplayFunc(render)  # Tell OpenGL to call the render method continuously
	GLUT.glutIdleFunc(render)   # Draw any graphics or shapes in the render function at all times
	GLUT.glutMainLoop()  # Keeps the window created above displaying/running in a loop

main()

# add spin?
# go 3d
# add shaders
