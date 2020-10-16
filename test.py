#!/usr/bin/python3

# import sys
from random import *

# import OpenGL
import OpenGL.GL as GL
import OpenGL.GLUT as GLUT
import OpenGL.GLU as GLU
import glfw

width = 1400
height = 1000
x = 0
flag = True;

squares = []

lastime = 0

def get_last_elapsed_time():
	global lasttime
	# lasttime = glfwget_time()
	actualtime = glfw.get_time()
	difference = actualtime - lasttime
	lasttime = actualtime
	return difference

class vec3:
	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z

	def __add__(self, other):
		return vec3(self.x + other.x, self.y + other.y, self.z + other.z)

	def __mul__(self, sc):
		return vec3(self.x * sc, self.y * sc, self.z * sc)

class square:
	def __init__(self, pos, side_length, velocity, color):
		self.pos = pos # lower left corner
		self.side_length = side_length
		# self.center = vec3(self.pos.x + self.side_length / 2, self.pos.y + self.side_length / 2, self.pos.z)
		self.velocity = velocity
		self.color = color

	def draw(self):
		GL.glColor3f(self.color.x, self.color.y, self.color.z) # Set the color
		# We have to declare the points in this sequence: bottom left, bottom right, top right, top left
		GL.glBegin(GL.GL_QUADS) # Begin the sketch
		GL.glVertex3f(self.pos.x, self.pos.y, self.pos.z) # Coordinates for the bottom left point
		GL.glVertex3f(self.pos.x + self.side_length, self.pos.y, self.pos.z) # Coordinates for the bottom right point
		GL.glVertex3f(self.pos.x + self.side_length, self.pos.y + self.side_length, self.pos.z) # Coordinates for the top right point
		GL.glVertex3f(self.pos.x, self.pos.y + self.side_length, self.pos.z) # Coordinates for the top left point
		GL.glEnd() # Mark the end of drawing

	def update(self, frametime):
		self.collide()
		self.pos = self.pos + self.velocity * frametime

	def collide(self):
		xbig = self.pos.x + self.side_length
		xsmall = self.pos.x
		ybig = self.pos.y + self.side_length
		ysmall = self.pos.y
		if xbig > width:
			self.velocity.x = -1 * abs(self.velocity.x)
		if xsmall < 0:
			self.velocity.x = abs(self.velocity.x)
		if ybig > height:
			self.velocity.y = -1 * abs(self.velocity.y)
		if ysmall < 0:
			self.velocity.y = abs(self.velocity.y)

def make_squares(how_many):
	global squares
	max_speed = 700
	for i in range(0, how_many):
		side_length = 100
		position = vec3(random() * (width - side_length), random() * (height - side_length), 0)
		velocity = vec3(((2 * random()) - 1) * max_speed, ((2 * random()) - 1) * max_speed, 0)
		color = vec3(random(), random(), random())
		squares.append(square(position, side_length, velocity, color))

def iterate():
	GL.glViewport(0, 0, width, height)
	GL.glMatrixMode(GL.GL_PROJECTION)
	GL.glLoadIdentity()
	GL.glOrtho(0.0, width, 0.0, height, 0.0, 1.0)
	GL.glMatrixMode (GL.GL_MODELVIEW)
	GL.glLoadIdentity()

def update(frametime):
	global squares
	for i in range(0, len(squares)):
		squares[i].update(frametime)

def render():
	global x, s1

	frametime = get_last_elapsed_time()
	update(frametime)

	print("framerate: " + str(round(1 / frametime)) + "      ", end = "\r")

	GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT) # Remove everything from screen (i.e. displays all white)
	GL.glLoadIdentity() # Reset all graphic/shape's position

	iterate()

	for i in range(0, len(squares)):
		squares[i].draw()

	GLUT.glutSwapBuffers()

def init():
	global lasttime
	# glfw.init()
	if not glfw.init():
		return
	lasttime = lastime = glfw.get_time()

	make_squares(50)

	GLUT.glutInit() # Initialize a glut instance which will allow us to customize our window
	GLUT.glutInitDisplayMode(GLUT.GLUT_RGBA) # Set the display mode to be colored
	GLUT.glutInitWindowSize(width, height)   # Set the width and height of your window
	GLUT.glutInitWindowPosition(0, 0)   # Set the position at which this windows should appear
	

def main():
	init()
	wind = GLUT.glutCreateWindow("hello triangle") # Give your window a title
	GLUT.glutDisplayFunc(render)  # Tell OpenGL to call the render method continuously
	GLUT.glutIdleFunc(render)   # Draw any graphics or shapes in the render function at all times
	GLUT.glutMainLoop()  # Keeps the window created above displaying/running in a loop

main()

# gimme framerate, frametime to make things move consistently
