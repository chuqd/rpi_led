class XYSprite:
	"""X/Y bookkeeping data for a pixellated 2D image"""
	
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

	def setLevels(self, level_set):
		self.levels = level_set
	
