# NeoPixel library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.


import sys
sys.path.append("../lib")

import time
from time import sleep
from random import *

import math

from neopixel import *
from ColorMap import *
from XYMapper import *
from XYSprite import *
from Sprites  import *

# LED strip configuration:
LED_COUNT      = 256      # Number of LED pixels.
MTX_WIDTH      = 16
MTX_HEIGHT     = 16
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
LED_STRIP      = ws.WS2811_STRIP_GRB   # Strip type and colour ordering

def bright_line(mapper, y):
  for x in range (0, MTX_WIDTH):
    mapper.setPixel(x, y, white)
  mapper.show()

def flicker_block(min_y, max_y):
  for y in range(min_y, max_y+1):
    for x in range(0, MTX_WIDTH):
      grayval = int(random() * 255)
      grayval = int((math.exp(random() * 10) / 22027) * 255)
      color = Color(grayval, grayval, grayval)
      mapper.setPixel(x, y, color);
  mapper.show()


# Main program logic follows:
if __name__ == '__main__':
	sleep_sec = 0.001
        # Create NeoPixel object with appropriate configuration.
        strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
        # Intialize the library (must be called once before other functions).
        strip.begin()

        mapper = XYMapper(strip, 16, 16, True)


        for i in range (0, 8):
          bright_line(mapper, 7 - i)
          bright_line(mapper, 8 + i)
          flicker_block(7-i, 8+i)

        #for x in range(-MTX_WIDTH, sprite.width - MTX_WIDTH):
	t = 0
        while (t < 5000):
          flicker_block(0, MTX_HEIGHT) 
 	  #sleep(sleep_sec)
	  t += 1

	sleep(5)
	mapper.allOff()

