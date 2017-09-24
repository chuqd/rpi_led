class XYSprite:
	"""X/Y bookkeeping data for a pixellated 2D image"""
	
	def __init__(self, sprite_width, sprite_height):
		self.width  = sprite_width
		self.height = sprite_height
	
	def setPixels(self, pixel_set):
		self.pixels = pixel_set
		
	def pixelAt(self, x, y):
		pixel = False
	  
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
	
