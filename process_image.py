from read_csv import is_raw_pixel_skin
from PIL import Image
import sys
import os

def getAdjacentPixelIndices()

# lookup_table = get_lookup_table()

# First arg is input, second arg is output
args = sys.argv[1:]

print args

image = Image.open(args[0])
width, height = image.size
print "{} {}".format(width, height)

pixels = list(image.getdata())
skinPixelMap = []

processedImage = Image.new(image.mode, image.size)
for pixel in pixels:
    skinPixelMap.append(is_raw_pixel_skin(pixel))

for x in range(0, 5):
    print "Iteration {}".format(x)

newPixels = []
for isPixelSkin in skinPixelMap:
    if isPixelSkin:
        newPixels.append((255, 255, 255))
    else:
        newPixels.append((0, 0, 0))



processedImage.putdata(newPixels);
processedImage.save(args[1])


# processedImage.putdata(image.getdata())
