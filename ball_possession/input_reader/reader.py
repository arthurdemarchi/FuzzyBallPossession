from pandas import read_csv
from os import listdir
from os.path import isdir


class Reader:

    ### Constructor ###
    def __init__(self, path='./data/'):
        self._path = path
        self.__list_of_files = self.__get_list_of_files(self._path)
        self.__list_index = 0

    ### Desctructor ###
    def __close__(self):
        self._path = None
        self.__list_of_files = None
        self.__list_of_files = None

    ### Getters and Setter (as Properties) ###
    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, path):
        if not path[0] == '.':
            raise ValueError(
                'Error: New path must be relative, syntax \'./data/path/to/file\'.'
            )
        if not path[0:7] == './data/':
            raise ValueError(
                'Error: New path can\'t be from outside data, syntax \'.data/path/to/file\'.'
            )
        self._path = path

    ### Methods ###
    def __get_list_of_files(self, directory):
        list_of_paths = listdir(directory)
        list_of_files = list()
        for path in list_of_paths:
            # file_path = directory+path
            file_path = directory + path
            if isdir(file_path):
                list_of_files = list_of_files + self.__get_list_of_files(
                    file_path)
            else:
                list_of_files.append(file_path)
        return list_of_files

    def __read_from_path(self, file_path):
        data = read_csv(file_path)
        print('Reading data from: ', file_path)
        distance = ((data['player_x'] - data['ball_x'])**2 +
                    (data['player_y'] - data['ball_y'])**2)**0.5
        relative_speed = ((data['player_vx'] - data['ball_vx'])**2 +
                          (data['player_vy'] - data['ball_vy'])**2)**0.5
        ball_speed = ((data['ball_vx']**2 + data['ball_vy'])**2)**0.5
        return distance, relative_speed, ball_speed

    def read_next_file(self):
        file_path = self.__list_of_files[self.__list_index]
        self.__list_index = self.__list_index + 1
        distance, relative_speed, ball_speed = self.__read_from_path(file_path)
        if self.__list_index >= len(self.__list_of_files):
            return False, distance, relative_speed, ball_speed
        return True, distance, relative_speed, ball_speed
