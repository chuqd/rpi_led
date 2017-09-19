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
	stretch_factor = 255 / max
	print stretch_factor

print width

pix_val = list(im.getdata())

stretched_pix = list(map(lambda x: int(x * stretch_factor), pix_val))

print stretched_pix

