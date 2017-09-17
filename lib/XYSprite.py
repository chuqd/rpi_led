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
	
