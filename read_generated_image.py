from PIL import Image
import itertools
import json
import os

import os

def extract_csv(image_filename, input_folder, output_folder):
    image = Image.open('{}/{}.jpg'.format(input_folder, image_filename))
    pixels = image.getdata()
    pixels_list = list(pixels)

    all_pixels = itertools.product(xrange(256), repeat=3)
    all_pixels_list = list(all_pixels)

    max_pixel = 0

    image_number = int(image_filename.split('_')[1])
    image_chunk_size = 65500
    image_chunk_offset = image_chunk_size * image_number
    image_pixel_chunk = all_pixels_list[image_chunk_offset: image_chunk_offset + image_chunk_size]
    with open('{}/{}.csv'.format(output_folder, image_filename), 'w+') as csv_file:
        for i in xrange(image_chunk_size):
            formatted_rbg = '{},{},{}'.format(
                image_pixel_chunk[i][0],
                image_pixel_chunk[i][1],
                image_pixel_chunk[i][2])

            max_pixel = max(max_pixel, pixels_list[i])

            csv_file.write('{} {}\n'.format(formatted_rbg, pixels_list[i]))

    print max_pixel

completed_algo_dir = './scoremap'

completed_csv_extraction_dir = './db_table'
completed_files = map(
    lambda filename: os.path.splitext(filename)[0],
    os.listdir(completed_csv_extraction_dir),
)

print(completed_files)

for filename_with_extension in os.listdir(completed_algo_dir):
    filename = os.path.splitext(filename_with_extension)[0]
    if filename_with_extension.endswith('.jpg') and \
        filename not in completed_files:
        print(filename)
        extract_csv(filename, completed_algo_dir, completed_csv_extraction_dir)

quit()

image = Image.open('scoremap/images_0.jpg')
print image.mode
pixels = image.getdata()
pixels_list = list(pixels)

all_pixels = itertools.product(xrange(256), repeat=3)
all_pixels_list = list(all_pixels)

max_pixel = 0

image_chunk_size = 65500
image_pixel_chunk = all_pixels_list[0:image_chunk_size]
put_commands = []
with open('db_table/image_0.csv', 'w+') as csv_file:
    for i in xrange(image_chunk_size):
        # print i
        formatted_rbg = '{},{},{}'.format(
            image_pixel_chunk[i][0],
            image_pixel_chunk[i][1],
            image_pixel_chunk[i][2])
        # print '{} {}'.format(formatted_rbg, pixels_list[i])

        max_pixel = max(max_pixel, pixels_list[i])

        csv_file.write('{} {}\n'.format(formatted_rbg, pixels_list[i]))
            # put_commands.push({
        #     "PutRequest": {
        #         "Item": {
        #             "rbg": formatted_rbg,
        #             "value":
        #         }
        #     }
        # })

# with('db_table/images_0.json', 'w') as outfile:

# for i in range(0, len(image_pixels_list), image_chunk_size):
#     image_pixel_chunk = image_pixels_list[i: i + image_chunk_size]
#     image3 = Image.new(image.mode, (1, image_chunk_size))
#
#     image3.putdata(image_pixel_chunk)
#     image3.save('images/images_{}.jpg'.format(image_count))
#     image_count = image_count + 1
