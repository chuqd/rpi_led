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
LED_BRIGHTNESS = 055     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
LED_STRIP      = ws.WS2811_STRIP_GRB   # Strip type and colour ordering

def bright_line(mapper, y):
  for x in range (0, MTX_WIDTH):
    mapper.setPixel(x, y, white)
  mapper.show()

def flicker_block(min_y, max_y, count):
  for i in range (0, count):
    for y in range(min_y, max_y+1):
      for x in range(0, MTX_WIDTH):
        grayval = int(random() * 255)
        grayval = int((math.exp(random() * 10) / 22027) * 255)
        color = Color(grayval, grayval, grayval)
        mapper.setPixel(x, y, color);
    mapper.show()

def invader(mapper):
  mapper.allOff()

  mtx_orig = {'x': 0, 'y': 0}
  sprite_orig = {'x': 3, 'y': 2}
  mapper.drawSprite(mtx_orig, sprite_orig, invader1a)
  sleep(2)
	
  invader_sleep = 0.3
  t = 1
  while t < 14:
    mapper.allOff()
    sprite_orig = {'x': 3 + t, 'y': 2}
    mapper.drawSprite(mtx_orig, sprite_orig, invader1b, {'no_wrap': True})
    sleep(invader_sleep)
    t = t + 1
    mapper.allOff()
    sprite_orig = {'x': 3 + t, 'y': 2}
    mapper.drawSprite(mtx_orig, sprite_orig, invader1a, {'no_wrap': True})
    sleep(invader_sleep)
    t = t + 1

def do_goodyear(mapper):
  sleep_sec = 0.008
  sprite_orig = {'x': 0, 'y': 0}
  sprite = goodyear
  for x in range(-MTX_WIDTH, sprite.width):# + 10): #MTX_WIDTH):
    mtx_orig = {'x': x, 'y': 0}
    mapper.drawSprite(mtx_orig, sprite_orig, sprite, {'no_wrap': True})
    sleep(sleep_sec)

def do_blimp(mapper):
  sleep_sec = 0.008
  sprite_orig = {'x': 0, 'y': 0}
  sprite = blimp16
  for x in range(-MTX_WIDTH, sprite.width + MTX_WIDTH):
    mtx_orig = {'x': x, 'y': 0}
    mapper.drawSprite(mtx_orig, sprite_orig, sprite, {'no_wrap': True})
    sleep(sleep_sec)

def running_man(mapper):
  sleep_sec = 0.05
  sprite_orig = {'x': 0, 'y': 0}
  mtx_orig = {'x': 0, 'y': 0}
  
  runners = [intel1, intel2, intel3, intel4, intel5, intel6, intel7, intel8]
  
  i = 0
  while (i < 5):
    for s in runners:
      mapper.drawSprite(mtx_orig, sprite_orig, s)
      sleep(sleep_sec)
    i = i + 1
    
  for i in range (0,5):
    mapper.drawSprite(mtx_orig, sprite_orig, runners[i])
    sleep(sleep_sec)

  trippers = [trip1, trip2, trip3]
  for t in trippers:    
   mapper.drawSprite(mtx_orig, sprite_orig, t)
   sleep(sleep_sec * 2.5)

  sleep(1)
  mapper.allOff()

def do_ghost(mapper):
  sleep_sec = 0.12
  sprite_orig = {'x': 0, 'y': 0}
  mtx_orig = {'x': 0, 'y': 0}

  for i in range(0, 5):
    mapper.drawSprite(mtx_orig, sprite_orig, bw_ghost1a, {'no_wrap': True})
    sleep(sleep_sec)
    mapper.drawSprite(mtx_orig, sprite_orig, bw_ghost1b, {'no_wrap': True})
    sleep(sleep_sec)

  mapper.allOff()
   

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
          flicker_block(7-i, 8+i, 1)

        flicker_block(0, MTX_HEIGHT, 155) 

        sprite_orig = {'x': 0, 'y': 0}
        mtx_orig = {'x': 0, 'y': 0}

        mapper.drawSprite(mtx_orig, sprite_orig, jacko16)
	sleep(3)

        flicker_block(0, MTX_HEIGHT, 10) 
        mapper.drawSprite(mtx_orig, sprite_orig, face1)
	sleep(3)

        flicker_block(0, MTX_HEIGHT, 6) 
	invader(mapper)
#        sleep(0.5)

        do_ghost(mapper)
        sleep(0.25)


        flicker_block(0, MTX_HEIGHT, 7) 
        running_man(mapper)
        sleep(1.5)

        flicker_block(0, MTX_HEIGHT, 10) 
        do_goodyear(mapper)
        do_blimp(mapper)

	mapper.allOff()

