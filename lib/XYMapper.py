from ColorMap import *

black = ColorMap[' '];
white = ColorMap['w'];

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

	# mtx_orig: location of the matrix origin on the sprite
	# sprite_orig: location of the sprite origin on the matrix
	def drawSprite(self, mtx_orig, sprite_orig, sprite, default_color = white):
		max_y = min (sprite.height, self.height)
		for y in range(0, max_y):
			max_x = min (sprite.width, self.width)
			for x in range(0, max_x):
				pixel_idx = self.XY(x + sprite_orig['x'], y + sprite_orig['y'])

				color = sprite.colorAt(x + mtx_orig['x'], y + mtx_orig['y'], default_color)
				#print color, pixel_idx
				self.strip.setPixelColor(pixel_idx, color)
		self.strip.show()

	def allOff(self):
		for y in range(0, self.height):
			for x in range(0, self.width):
				pixel_idx = self.XY(x, y)
				self.strip.setPixelColor(pixel_idx, black)
	
		self.strip.show()

