from .input_reader.reader import Reader

#create reader with default data path values
reader = Reader()


distance, relative_speed, ball_speed = reader.read_next_file()
