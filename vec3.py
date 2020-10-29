# contains vec3 class for vector math

class vec3:
	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z

	def __add__(self, other): # vector addition
		return vec3(self.x + other.x, self.y + other.y, self.z + other.z)

	def __radd__(self, other): # vector addition
		return self._add__(other)

	def __mul__(self, sc): # scalar multiplication
		return vec3(self.x * sc, self.y * sc, self.z * sc)

	def __rmul__(self, sc): # scalar multiplication
		return self.__mul__(sc)

	# make plus equals
