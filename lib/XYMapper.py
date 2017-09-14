class XYMapper:
	"""A mechanism to map X,Y coordinates against a known rectangle to a linear string of WS21x LEDs"""
	
	def __init__(self, strip, rect_width, rect_height, is_serpentine):
		self.strip  = strip
		self.width  = rect_width
		self.height = rect_height
		self.serpentine = is_serpentine
	
	def XY(self, x, y):
		i = False
		
		if (self.serpentine == False):
			i = (self.width * y) + x
		else:
		  if (y % 2):
		  	# odd rows run backward
		  	reverse_x = (self.width - 1) - x
		  	i = (self.width * y) + reverse_x
		  else:
		    i = (self.width * y) + x
		
		return i
			
	def XYwrap(self, x, y):
		if (x >= self.width):
			x = x % self.width
		
		if (y >= self.height):
			y = y % self.height
		
		return self.XY(x, y)
	