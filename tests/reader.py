from ball_possession.input_reader.reader import Reader

#test reading all files from list
reader = Reader()

status = True
while status:
    status, distance, relative_speed, ball_speed = reader.read_next_file()
    print('distance \n', distance)
    print('relative speed \n', relative_speed)
    print('ball speed \n', ball_speed)
