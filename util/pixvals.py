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

filename = sys.argv[1]

im = Image.open(filename, 'r')

(width, height) = im.size

# modes: 
#  1 - 1-bit, black/white
#  L, P - 8-bit
#  RGB, YCbCr - 3x8bit
#  RGBA, CMYK - 4x8bit
#  I - 32bit signed
#  F - 32bit float
print im.mode

def print_em(pixels, height, width):
	print "["
	for y in range (0, height-1):
		line = '  ['
		for x in range (0, width-1):
			line += str(pixels[(y * width) + x])
			if (x < width - 2):
				line += ','
		line += ']'
		if (y < height - 2):
			line += ','
		print line
	print "],"

stretch_factor = 1
if im.mode in ['1', 'L', 'P']:
	(min, max) = im.getextrema()
	stretch_factor = MAX_8BIT_VAL / max
	print stretch_factor

print width, height, im.mode

if im.mode in ['RGB', 'RGBA']:
	pix_val = list(map(lambda p: int((0.21 * p[0]) + (0.72 * p[1]) + (0.07 * p[2])), im.getdata()))
else:
	pix_val = list(im.getdata())

#print pix_val

print 'Integer:'
stretched_pix = list(map(lambda x: int(x * stretch_factor), pix_val))
print stretched_pix

inverted_pix = list(map(lambda x: MAX_8BIT_VAL - int(x * stretch_factor), pix_val))
print 'Inverted:'
print inverted_pix

print ''
print filename
print ''

print 'Percentage:'
stretched_pix = list(map(lambda x: round((x * stretch_factor / MAX_8BIT_VAL), 3), pix_val))
#print stretched_pix
print_em(stretched_pix, height, width)

inverted_pix = list(map(lambda x: round(1.0 - (x * stretch_factor / MAX_8BIT_VAL), 3), pix_val))
print 'Inverted:'
#print inverted_pix
print_em(inverted_pix, height, width)


