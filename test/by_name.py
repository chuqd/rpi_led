# NeoPixel library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.


import sys
sys.path.append("../lib")

import time
from time import sleep


from neopixel import *
from ColorMap import *
from XYMapper import *
from XYSprite import *
from Sprites  import *

g_mapper = 0
import signal
import sys
def signal_handler(signal, frame):
	if (g_mapper != 0):
		g_mapper.allOff()
	exit(0)
signal.signal(signal.SIGINT, signal_handler)

if len(sys.argv) < 2:
	print "State your name"
	exit(0)
sprite_name = sys.argv[1]

if (sys.argv[2]):
	lux = int(sys.argv[2])
else:
	lux = 64

# LED strip configuration:
LED_COUNT      = 256      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = lux     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
LED_STRIP      = ws.WS2811_STRIP_GRB   # Strip type and colour ordering



white = ColorMap['w'];

# Main program logic follows:
if __name__ == '__main__':
	sleep_sec = 5
        # Create NeoPixel object with appropriate configuration.
        strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
        # Intialize the library (must be called once before other functions).
        strip.begin()

        mapper = XYMapper(strip, 16, 16, True)
        g_mapper = mapper


	sprite = globals()[sprite_name]

	sprite_orig = {'x': 0, 'y': 0}
	mtx_orig = {'x': 0, 'y': 0}

	mapper.drawSprite(mtx_orig, sprite_orig, sprite)
	while True:
		sleep(sleep_sec)
