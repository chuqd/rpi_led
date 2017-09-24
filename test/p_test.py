# NeoPixel library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.


import sys
sys.path.append("../lib")
sys.path.append("../../rpi_ws281x/python")

import time

from neopixel import *
from ColorMap import *
from XYMapper import *
from XYSprite import *


# LED strip configuration:
LED_COUNT      = 256      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 64      # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
LED_STRIP      = ws.WS2811_STRIP_GRB   # Strip type and colour ordering



white = ColorMap['w'];

def shadeColor(color, shade_factor):
	red   = (color >> 16) & 255
	green = (color >> 8)  & 255
	blue  = color & 255
	shaded_color = Color(int(red * shade_factor), int(green * shade_factor), int(blue * shade_factor))
	print shade_factor, red, green, blue
	return shaded_color

def drawSprite(mapper, x_orig, y_orig, sprite, default_color = white):
	for y in range(0, sprite.height):
		for x in range(0, sprite.width):
#			code  = sprite.pixelAt(x, y)
#			color = ColorMap[code]
#			if (hasattr(sprite, 'levels')):
#				level = sprite.levelAt(x, y)
#				color = shadeColor(color, level)
			pixel_idx = mapper.XY(x + x_orig, y + y_orig)

			color = sprite.colorAt(x, y)
			print color, pixel_idx
			mapper.strip.setPixelColor(pixel_idx, color)
	mapper.strip.show()

# Main program logic follows:
if __name__ == '__main__':
	# Create NeoPixel object with appropriate configuration.
	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
	# Intialize the library (must be called once before other functions).
	strip.begin()

	mapper = XYMapper(strip, 16, 16, True)

	pixels = [
		['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
		['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
		['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
		['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
		['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
		['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
		['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
		['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
		['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
		['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
		['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
		['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
		['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
		['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
		['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
		['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
		['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*']
		]
	levels = [
		[0.0,0.313,0.667,0.604,0.063,0.0,0.0,0.0,0.0,0.0,0.0,0.042,0.583,0.688,0.292],
		[0.5,0.979,1.0,1.0,0.667,0.0,0.0,0.0,0.0,0.0,0.0,0.667,1.0,1.0,0.979],
		[1.0,1.0,1.0,1.0,0.875,0.063,0.0,0.0,0.0,0.0,0.083,0.896,1.0,1.0,1.0],
		[1.0,1.0,1.0,1.0,0.792,0.021,0.0,0.021,0.042,0.0,0.042,0.771,1.0,0.979,1.0],
		[1.0,1.0,1.0,1.0,0.438,0.0,0.021,0.708,0.729,0.021,0.0,0.396,1.0,1.0,1.0],
		[0.75,1.0,0.979,0.563,0.0,0.0,0.5,1.0,1.0,0.583,0.0,0.0,0.542,0.938,1.0],
		[0.063,0.333,0.188,0.0,0.0,0.146,0.938,1.0,1.0,0.958,0.167,0.0,0.0,0.146,0.25],
		[0.0,0.0,0.0,0.0,0.0,0.25,0.958,1.0,1.0,0.938,0.333,0.0,0.0,0.0,0.0],
		[0.417,0.0,0.0,0.0,0.0,0.021,0.146,0.271,0.25,0.146,0.0,0.0,0.0,0.0,0.063],
		[1.0,0.792,0.458,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.021,0.146,0.354,0.646,0.833],
		[0.729,1.0,0.792,0.0,0.0,0.125,0.729,0.771,0.75,0.75,0.792,0.917,1.0,1.0,1.0],
		[0.146,0.938,1.0,0.375,0.146,0.563,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,0.938],
		[0.0,0.292,0.938,1.0,0.979,0.979,1.0,1.0,1.0,1.0,0.979,0.625,0.375,0.792,0.479],
		[0.0,0.0,0.25,0.854,1.0,1.0,1.0,1.0,1.0,1.0,0.521,0.0,0.0,0.104,0.0],
		[0.0,0.0,0.0,0.083,0.583,0.813,1.0,1.0,1.0,0.958,0.208,0.0,0.0,0.0,0.0],
		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
		]

	sprite = XYSprite(16, 16)
	sprite.setPixels(pixels)
	sprite.setLevels(levels)

	drawSprite(mapper, 0, 0, sprite)

