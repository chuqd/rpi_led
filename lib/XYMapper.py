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

	def setPixel(self, x, y, color):
		pixel_idx = self.XY(x, y)
		self.strip.setPixelColor(pixel_idx, color)


	# mtx_orig: location of the matrix origin on the sprite
	# sprite_orig: location of the sprite origin on the matrix
	def drawSprite(self, mtx_orig, sprite_orig, sprite, attrs = {}):
		if ('color' in attrs):
			default_color = attrs['color']
		else:
			default_color = white

		if ('no_wrap' in attrs):
			no_wrap = attrs['no_wrap']
		else:
			no_wrap = False

		if('no_show' in attrs):
			show_strip = False
		else:
			show_strip = True

		if('blank' in attrs):
			blank_it = attrs['blank']
		else:
			blank_it = False

		if('on_curve' in attrs):
			curve_it = attrs['on_curve']
		else:
			curve_it = True

		max_y = min (sprite.height, self.height)
		for y in range(0, max_y):
			max_x = min (sprite.width, self.width, (self.width - sprite_orig['x']))
			for x in range(0, max_x):
				if (x + sprite_orig['x'] < 0 or y + sprite_orig['y'] < 0):
					continue;
				pixel_idx = self.XY(x + sprite_orig['x'], y + sprite_orig['y'])

				pix_x = x + mtx_orig['x']
				pix_y = y + mtx_orig['y']

				if (no_wrap and (pix_x < 0 or pix_y < 0 or pix_x > sprite.width or pix_y > sprite.height)):
					color = black
				elif (blank_it): 
					color = black
				#elif (x + sprite_orig['x'] < 0 or y + sprite_orig['y'] < 0):
				#	color = black
				else:
					color = sprite.colorAt(pix_x, pix_y, default_color, {'on_curve': curve_it})
				#print color, pixel_idx
				self.strip.setPixelColor(pixel_idx, color)
		if show_strip:
			self.strip.show()

	def drawSpriteSet(self, sprites, attrs = {}):
		for sprite_info in sprites:
			attrs['no_show'] = True
			self.drawSprite(sprite_info['mo'], sprite_info['so'], sprite_info['sprite'], attrs)
		self.strip.show()

	def allOff(self):
		for y in range(0, self.height):
			for x in range(0, self.width):
				pixel_idx = self.XY(x, y)
				self.strip.setPixelColor(pixel_idx, black)
	
		self.strip.show()

        def allOn(self):
                for y in range(0, self.height):
                        for x in range(0, self.width):
                                pixel_idx = self.XY(x, y)
                                self.strip.setPixelColor(pixel_idx, white)

                self.strip.show()


	def show(self):
	  self.strip.show()
