def get_lookup_table():
    lookup_table = {}

    with open('./silver_map.csv', 'r') as ins:
        for line in ins:
            rbg, score = line.rstrip('\n').split(' ')

            lookup_table[rbg] = int(score)


    return lookup_table

map_lookup_table = get_lookup_table();

def is_raw_pixel_skin(rbg_tuple, confidence = 0.5):
    pixel_str = '{},{},{}'.format(rbg_tuple[0], rbg_tuple[1], rbg_tuple[2])

    if pixel_str in map_lookup_table:
        return ((map_lookup_table[pixel_str])/255.) > confidence
    else:
        return False
