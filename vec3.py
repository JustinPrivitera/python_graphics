# contains vec3 class for vector math

import math

class vec3:
	def __init__(self, x = 0, y = 0, z = 0):
		self.x = x
		self.y = y
		self.z = z

	def __add__(self, other): # vector addition
		return vec3(self.x + other.x, self.y + other.y, self.z + other.z)

	def __radd__(self, other): # vector addition
		return vec3(self.x + other.x, self.y + other.y, self.z + other.z)

	def __sub__(self, other): # vector subtraction
		return vec3(self.x - other.x, self.y - other.y, self.z - other.z)

	def __rsub__(self, other): # vector subtraction
		return vec3(other.x - self.x, other.y - self.y, other.z - self.z)

	def __iadd__(self, other):
		self.x += other.x
		self.y += other.y
		self.z += other.z

	def __mul__(self, sc): # scalar multiplication
		return vec3(self.x * sc, self.y * sc, self.z * sc)

	def __rmul__(self, sc): # scalar multiplication
		return self.__mul__(sc)

	def __str__(self):
		return str(self.x) + ", " + str(self.y) + ", " + str(self.z)

	def magnitude(self):
		return math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)

	def normalize(self):
		mag = self.magnitude()
		return self * (1/mag)


	# make plus equals
