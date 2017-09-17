# NeoPixel library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.


import sys
sys.path.append("../lib")

import time

from neopixel import *
from ColorMap import *
from XYMapper import *
from XYSprite import *
from Sprites  import *

# LED strip configuration:
LED_COUNT      = 256      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 64     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
LED_STRIP      = ws.WS2811_STRIP_GRB   # Strip type and colour ordering



white = ColorMap['w'];

def drawSprite(mapper, x_orig, y_orig, sprite, default_color = white):
        for y in range(0, sprite.height):
                for x in range(0, sprite.width):
                        code  = sprite.pixelAt(x, y)
                       	if ('*' == code):
				color = default_color 
			else:
				color = ColorMap[code]
                        pixel_idx = mapper.XY(x + x_orig, y + y_orig)

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

#        pixels = ["r r", "g g", "b b"]
#        sprite = XYSprite(3, 3)
#        sprite.setPixels(pixels)

        drawSprite(mapper, 0, 0, intel1)

