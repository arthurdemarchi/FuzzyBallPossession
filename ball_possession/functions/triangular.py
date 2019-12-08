class triangular:
    ### Constructor ###
    def __init__(self, init, end, center=None, maximum=1, minimum=0):
        # initialize attributes
        self._init = init
        self._end = end
        if center:
            #using property to test if its bewtween init and end
            self.center = center
        else:
            self._center = (init - end) / 2
        self._maximum = maximum
        self._minimum = minimum

    ### Desctructor ###
    def __close__(self):
        # releases attributes
        self._function = None
        self._init = None
        self._end = None
        self._maximum = None
        self._minimum = None

    ### Getters and Setter (as Properties) ###
    ## init
    @property
    def init(self):
        return self._init

    @init.setter
    def init(self, init):
        if type(init) == float or type(init) == int:
            self._init = init
        else:
            raise ValueError(
                'Error: Function initial element must be float or integer')

    ## end
    @property
    def end(self):
        return self._end

    @end.setter
    def end(self, end):
        if type(end) == float or type(end) == int:
            self._end = end
        else:
            raise ValueError(
                'Error: Function end element must be float or integer')

    ## center
    @property
    def center(self):
        return self._center

    @center.setter
    def center(self, center):
        if type(center) == float or type(center) == int:
            if center > self._init and center < self._end:
                self._center = center
            else:
                raise ValueError(
                    'Error: Center of the function must be between init and end'
                )
        else:
            raise ValueError(
                'Error: Function center element must be float or integer')

    ## maximum
    @property
    def maximum(self):
        return self._maximum

    @maximum.setter
    def maximum(self, maximum):
        if type(maximum) == float or type(maximum) == int:
            self._maximum = maximum
        else:
            raise ValueError(
                'Error: Function maximum element must be float or integer')

    ## minimum
    @property
    def minimum(self):
        return self._minimum

    @minimum.setter
    def minimum(self, minimum):
        if type(minimum) == float or type(minimum) == int:
            self._minimum = minimum
        else:
            raise ValueError(
                'Error: Function minimum element must be float or integer')

    ### Methods ###
    def function(self, x):
        if x <= self._center:
            delta_y = self._maximum - self._minimum
            delta_x = self._center - self._init
            slope = delta_y / delta_x
            return slope * (x - self._init)

        if x > self._center:
            delta_y = self._minimum - self._maximum
            delta_x = self._end - self._center
            slope = delta_y / delta_x
            return self._maximum + slope * (x - self._center)

        return self._minimum