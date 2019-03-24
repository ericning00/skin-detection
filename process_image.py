from read_csv import is_raw_pixel_skin
from PIL import Image
import sys
import os

def getAdjacentPixelIndices(index, radius, height, width):
    indices = []

    # From top to bottom
    for rowDiff in range(-radius, radius + 1):
        # From left to right
        for colDiff in range(-radius, radius + 1):
            if rowDiff is 0 and colDiff is 0:
                continue

            indices.append(index + (width * rowDiff) + colDiff)

    return filter(
        lambda index: index >= 0 and index <= (height * width) - 1,
        indices
    )

def processNewSkinMapIteration(
    skinMap,
    radius,
    threshold_ratio,
    height,
    width,
    onlyIsSkin = False
):
    newSkinPixelMap = []
    for index, isCurrentPixelSkin in enumerate(skinMap):
        if onlyIsSkin and isCurrentPixelSkin is False:
            newSkinPixelMap.append(isCurrentPixelSkin)
            continue

        adjacentPixels = getAdjacentPixelIndices(index, radius, height, width);
        skinCount = 0.
        for adjacentPixelIndex in adjacentPixels:
            if skinMap[adjacentPixelIndex]:
                skinCount = skinCount + 1.

        newSkinPixelMap.append(
            True if (skinCount/len(adjacentPixels)) > threshold_ratio else False
        )

    return newSkinPixelMap

def outputPicture(mode, size, skinMap, image_name):
    processedImage = Image.new(mode, size)
    newPixels = []
    for isPixelSkin in skinMap:
        if isPixelSkin:
            newPixels.append((255, 255, 255))
        else:
            newPixels.append((0, 0, 0))
    processedImage.putdata(newPixels);
    processedImage.save("./{}.jpg".format(image_name))

# First arg is input, second arg is output, third arg is iterations
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

outputPicture(image.mode, image.size, skinPixelMap, 'image_0');

# Clean up patches
for iteration in range(0, 1):
    skinPixelMap = processNewSkinMapIteration(skinPixelMap, 4, 0.4, height, width, True)
    print "Cleanup Iteration {}".format(iteration + 1)
    outputPicture(image.mode, image.size, skinPixelMap, "image_cleanup_{}".format(iteration));

# Fill in patches
for iteration in range(0, 10):
    skinPixelMap = processNewSkinMapIteration(skinPixelMap, 1, 0.5, height, width)
    print "Fill-in Iteration {}".format(iteration + 1)
    outputPicture(image.mode, image.size, skinPixelMap, "image_fillin_{}".format(iteration));
