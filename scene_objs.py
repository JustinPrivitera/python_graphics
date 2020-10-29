# import sys
from random import *

# import OpenGL
import OpenGL.GL as GL
from vec3 import *

class square:
	def __init__(self, pos, side_length, velocity, color, width, height):
		self.pos = pos # lower left corner
		self.side_length = side_length
		# self.center = vec3(self.pos.x + self.side_length / 2, self.pos.y + self.side_length / 2, self.pos.z)
		self.velocity = velocity
		self.color = color
		self.width = width
		self.height = height

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
		if self.pos.x + self.side_length > self.width:
			self.velocity.x = -1 * abs(self.velocity.x)
		if self.pos.x < 0:
			self.velocity.x = abs(self.velocity.x)
		if self.pos.y + self.side_length > self.height:
			self.velocity.y = -1 * abs(self.velocity.y)
		if self.pos.y < 0:
			self.velocity.y = abs(self.velocity.y)

def make_squares(how_many, width, height):
	squares = []
	max_speed = 700
	for i in range(0, how_many):
		side_length = 100
		position = vec3(random() * (width - side_length), random() * (height - side_length), 0)
		velocity = vec3(((2 * random()) - 1) * max_speed, ((2 * random()) - 1) * max_speed, 0)
		color = vec3(random(), random(), random())
		squares.append(square(position, side_length, velocity, color, width, height))
	return squares
