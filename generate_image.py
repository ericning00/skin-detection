from PIL import Image
import itertools

image = Image.open('../RF_Code/images/test.jpg')
pixels = image.load()
image2 = Image.open('../RF_Code/scoremap/test.jpg')

print image.mode
print image2.mode

all_pixels = itertools.product(xrange(256), repeat=3)
image_pixels_list = list(all_pixels)
print(len(image_pixels_list))

image_count = 0
image_chunk_size = 65500
for i in range(0, len(image_pixels_list), image_chunk_size):
    image_pixel_chunk = image_pixels_list[i: i + image_chunk_size]
    image3 = Image.new(image.mode, (1, image_chunk_size))

    image3.putdata(image_pixel_chunk)
    image3.save('images/images_{}.jpg'.format(image_count))
    image_count = image_count + 1
