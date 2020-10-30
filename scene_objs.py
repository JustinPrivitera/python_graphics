# import sys
from random import *

# import OpenGL
import OpenGL.GL as GL
from vec3 import *
import config

class geom_obj:
	def __init__(self, color):
		self.color = color

	def update(self, frametime):
		pass

class point(geom_obj):
	def __init__(self, pos, velocity, acceleration, color):
		geom_obj.__init__(self, color)
		self.pos = pos
		self.velocity = velocity
		self.acceleration = acceleration

	def draw(self):
		GL.glColor3f(self.color.x, self.color.y, self.color.z)
		GL.glBegin(GL.GL_POINTS)
		GL.glVertex3f(self.pos.x, self.pos.y, self.pos.z)
		GL.glEnd()

	def update(self, frametime):
		# need a method to update acceleration OUTSIDE this object
		self.velocity = self.acceleration * frametime + self.velocity
		self.pos = self.pos + self.velocity * frametime

# class physical_point(geom_obj):
	

class triangle(geom_obj):
	def __init__(self, a, b, c, velocity, color):
		geom_obj.__init__(self, color)
		self.a = a
		self.b = b
		self.c = c
		self.velocity = velocity

	def draw(self):
		GL.glColor3f(self.color.x, self.color.y, self.color.z)
		GL.glBegin(GL.GL_TRIANGLES)
		GL.glVertex3f(self.a.x, self.a.y, self.a.z)
		GL.glVertex3f(self.b.x, self.b.y, self.b.z)
		GL.glVertex3f(self.c.x, self.c.y, self.c.z)
		GL.glEnd()

	def update(self, frametime):
		self.a = self.a + self.velocity * frametime
		self.b = self.b + self.velocity * frametime
		self.c = self.c + self.velocity * frametime

# supports wall collisions
class square(geom_obj):
	def __init__(self, pos, side_length, velocity, color):
		geom_obj.__init__(self, color)
		self.pos = pos # lower left corner
		self.side_length = side_length
		# self.center = vec3(self.pos.x + self.side_length / 2, self.pos.y + self.side_length / 2, self.pos.z)
		self.velocity = velocity
		# self.color = color

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

	def collide(self): # collisions with wall
		if self.pos.x + self.side_length > config.width:
			self.velocity.x = -1 * abs(self.velocity.x)
		if self.pos.x < 0:
			self.velocity.x = abs(self.velocity.x)
		if self.pos.y + self.side_length > config.height:
			self.velocity.y = -1 * abs(self.velocity.y)
		if self.pos.y < 0:
			self.velocity.y = abs(self.velocity.y)

def make_squares(how_many):
	squares = []
	max_speed = 700
	for i in range(0, how_many):
		side_length = 100
		position = vec3(random() * (config.width - side_length), random() * (config.height - side_length), 0)
		velocity = vec3(((2 * random()) - 1) * max_speed, ((2 * random()) - 1) * max_speed, 0)
		color = vec3(random(), random(), random())
		squares.append(square(position, side_length, velocity, color))
	return squares

def make_points(how_many):
	points = []
	max_speed = 300
	for i in range(0, how_many):
		pos = vec3(random() * config.width, random() * config.height, 0)
		velocity = vec3(((2 * random()) - 1) * max_speed, ((2 * random()) - 1) * max_speed, 0)
		acceleration = vec3()
		color = vec3(random(), random(), random())
		points.append(point(pos, velocity, acceleration, color))
	return points
