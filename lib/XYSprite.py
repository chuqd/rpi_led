from neopixel import *
from ColorMap import *

class XYSprite:
	"""X/Y bookkeeping data for a pixellated 2D image"""
	white = Color(255, 255, 255)
	
	pixels = false  # If only levels are set, all x,y will return default pixel color
	
	def __init__(self, sprite_width, sprite_height):
		self.width  = sprite_width
		self.height = sprite_height
	
	def setPixels(self, pixel_set):
		self.pixels = pixel_set
		
	def pixelAt(self, x, y):
		pixel = '*'
	  
		if self.pixels:
			this_row = self.pixels[y]
	  
	  		if (len(this_row) > x):
	  			pixel = this_row[x]
	  	
		return pixel 

	def levelAt(self, x, y):
		level = 1.0
	 
		if not hasattr(self, 'levels'):
			return level
 
		this_row = self.levels[y]
	  
		if (len(this_row) > x):
			level = this_row[x]
	  	
		return level 

	def setLevels(self, level_set):
		self.levels = level_set

	def colorAt(self, x, y, default_color = white):
		level = self.levelAt(x, y)
		pixel_color = self.pixelAt(x, y)
		if pixel_color == '*':
			color = default_color
		else:
			color = ColorMap[pixel_color]

		if (hasattr(self, 'levels')):
			shade_factor = self.levelAt(x, y)
			red   = (color >> 16) & 255
			green = (color >> 8)  & 255
			blue  = color & 255
			color = Color(int(red * shade_factor), int(green * shade_factor), int(blue * shade_factor))

		print 'color:', color
		return color
