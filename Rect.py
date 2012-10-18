class Rect:
	def __init__(self, x, y, width, height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height

	def __repr__(self):
		return repr("x:" + str(self.x) + ", y:" + str(self.y) + ", width:" + str(self.width) + ", height:" + str(self.height))

	def right(self):
		return self.x + self.width - 1

	def bottom(self):
		return self.y + self.height - 1
