with open('silver_map.csv', 'w+') as csv_file:
    with open('./golden_map.csv', 'r') as ins:
        for line in ins:
            rbg, score = line.rstrip('\n').split(' ')
            if int(score) > (255/4):
                csv_file.write(line)
