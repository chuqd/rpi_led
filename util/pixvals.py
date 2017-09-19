from __future__ import division  # floating-point division
comment = '''
im.getdata() => sequence

Returns the contents of an image as a sequence object containing pixel values. 
The sequence object is flattened, so that values for line one follow directly after 
the values of line zero, and so on.

Note that the sequence object returned by this method is an internal PIL data type, 
which only supports certain sequence operations, including iteration and basic sequence 
access. To convert it to an ordinary sequence (e.g. for printing), use list(im.getdata()).

http://effbot.org/imagingbook/image.htm

Usage: python pixvals.py image_file_name
'''

from PIL import Image
import sys

MAX_8BIT_VAL = 255

im = Image.open(sys.argv[1], 'r')

(width, height) = im.size

# modes: 
#  1 - 1-bit, black/white
#  L, P - 8-bit
#  RGB, YCbCr - 3x8bit
#  RGBA, CMYK - 4x8bit
#  I - 32bit signed
#  F - 32bit float
print im.mode

stretch_factor = 1
if im.mode in ['1', 'L', 'P']:
	(min, max) = im.getextrema()
	stretch_factor = MAX_8BIT_VAL / max
	print stretch_factor

print width

pix_val = list(im.getdata())

print 'Integer:'
stretched_pix = list(map(lambda x: int(x * stretch_factor), pix_val))
print stretched_pix

inverted_pix = list(map(lambda x: MAX_8BIT_VAL - int(x * stretch_factor), pix_val))
print 'Inverted:'
print inverted_pix

print 'Percentage:'
stretched_pix = list(map(lambda x: round((x * stretch_factor / MAX_8BIT_VAL), 3), pix_val))
print stretched_pix

inverted_pix = list(map(lambda x: round(1.0 - (x * stretch_factor / MAX_8BIT_VAL), 3), pix_val))
print 'Inverted:'
print inverted_pix

