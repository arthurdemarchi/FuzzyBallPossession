from math import log
from copy import deepcopy, copy


class Region:

    ### Constructor ###
    def __init__(self, name, npoints, init, end, function):
        # initialize attributes
        self._name = name
        self._npoints = npoints
        self._init = init
        self._end = end
        self._size = self._end - self._init
        self._function = function
        self._fuzzy = self.__generate_fuzzy()

    ### Desctructor ###
    def __close__(self):
        self._name = None
        self._npoints = None
        self._init = None
        self._end = None
        self._size = None
        self._fuzzy = None
        self._function = None

    ### Getters and Setter (as Properties) ###
    ## name
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if type(name) == str:
            self._name = name
        else:
            raise ValueError('Error: Region name must be string')

    ## npoints
    @property
    def npoints(self):
        return self._npoints

    @npoints.setter
    def npoints(self, npoints):
        if type(npoints) == int:
            self._npoints = npoints
            self._fuzzy = self.__generate_fuzzy()
        else:
            raise ValueError('Error: Region number of points must be integer')

    ## init
    @property
    def init(self):
        return self._init

    @init.setter
    def init(self, init):
        if type(init) == float or type(init) == int:
            if init >= self._end:
                raise ValueError(
                    'Error: Region inital element must be smaller than last element'
                )
            if init < self._init:
                discretization_ration = self._size / self._npoints
                self._init = init
                self._size = self._end - init
                self._npoints = round(self._size / discretization_ration)
                self._fuzzy = self.__generate_fuzzy()
            else:
                list_to_iterate = deepcopy(self._fuzzy)
                for fuzzy_element in list_to_iterate:
                    if fuzzy_element['x'] < init:
                        self._fuzzy.remove(fuzzy_element)
                self._init = init
                self._npoints = len(self._fuzzy)
                self._size = self._end - self._init
        else:
            raise ValueError(
                'Error: Region initial element must be float or integer')

    ## end
    @property
    def end(self):
        return self._end

    @end.setter
    def end(self, end):
        if type(end) == float or type(end) == int:
            if end <= self._init:
                raise ValueError(
                    'Error: Region last element must be greater than initial element'
                )
            if end > self._end:
                discretization_ration = self._size / self._npoints
                self._end = end
                self._size = end - self._init
                self._npoints = round(self._size / discretization_ration)
                self._fuzzy = self.__generate_fuzzy()
            else:
                list_to_iterate = deepcopy(self._fuzzy)
                for fuzzy_element in list_to_iterate:
                    if fuzzy_element['x'] > end:
                        self._fuzzy.remove(fuzzy_element)
                self._end = end
                self._npoints = len(self._fuzzy)
                self._size = self._end - self._init
        else:
            raise ValueError(
                'Error: Region last element must be float or integer')

    ## size
    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        raise ValueError('Error: Can\'t directly set size')

    ## function
    @property
    def function(self):
        return self._function

    @function.setter
    def function(self, function):
        if type(function) == 'function':
            self._function = function
            self._fuzzy = self.__generate_fuzzy()
        else:
            raise ValueError('Error: region function must be of function type')

    ## fuzzy
    @property
    def fuzzy(self):
        return self._fuzzy

    @fuzzy.setter
    def fuzzy(self, fuzzy):
        if type(fuzzy) == list:
            self._fuzzy = fuzzy
            self._function = None
            self._npoints = len(fuzzy)
            self._init = fuzzy[0]['x']
            self._end = fuzzy[self._npoints - 1]['x']
            self._size = self._end - self._init
        else:
            raise ValueError('Error: region fuzzy must be a list')

    ### Private Methods ###
    def __discretize(self, x):
        discretized_x = (x / self.npoints) * self._size
        ndigits = int(log(self.npoints, 10) + 1)
        discretized_x = round(discretized_x, ndigits)
        discretized_x = discretized_x + self._init
        return discretized_x

    def __generate_fuzzy(self):
        if self._function == None:
            raise ValueError(
                'Error: This region was defined directly trhought fuzzy attribute wich means it can\'t be redifined'
            )
        fuzzy = list()
        # fill self._fuzzy with fuzzy region elements and pertineces
        for x in range(0, self.npoints):
            x = self.__discretize(x)
            u = self._function(x)
            region_item = {'x': x, 'u': u}
            fuzzy.append(region_item)
        return fuzzy
    
    ### Methods ###
    def get_u(self, x):
        for i, item in enumerate(self.fuzzy):
            if x == item['x']:
                return item['u']
            if x < item['x']:
                return self.fuzzy[i-1]['u']
    
    def is_active(self, x):
        if self.get_u(x) == 0: 
            return False
        else:
            return True

    def mandani(self, treshold):
        for item in self._fuzzy:
            item['u'] = min(item['u'], treshold)
        self.fuzzy = self._fuzzy

    def zadeh(self, treshold):
        for item in self._fuzzy:
            item['u'] = max(1-treshold, min(item['u'], treshold))
        self.fuzzy = self._fuzzy

    def larsen(self, treshold):
        for item in self._fuzzy:
            item['u'] = item['u']*treshold
        self.fuzzy = self._fuzzy

    def cda(self):
        u_times_x = 0
        u = 0
        for item in self.fuzzy:
            u_times_x = u_times_x + item['u']*item['x']
            u = u + item['u']
        return round(u_times_x/u, 2)

    def mdm(self):
        max_u = 0
        for item in self.fuzzy:
            max_u = max(item['u'], max_u)
		
        sum_x = 0
        number_of_x = 0
        for item in self.fuzzy:
            if item['u'] == max_u:
                sum_x = sum_x + item['x']
                number_of_x = number_of_x + 1
        return round(sum_x/number_of_x, 2)

    def mpm(self):
        max_u = 0
        for item in self.fuzzy:
            max_u = max(item['u'], max_u)

        for item in self.fuzzy:
            if item['u'] == max_u:
                return round(item['x'], 2)

