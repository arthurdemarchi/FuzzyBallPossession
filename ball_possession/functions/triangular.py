class Triangular:
    ### Constructor ###
    def __init__(self, init, end, center=None, peak=1, floor=0):
        # initialize attributes
        self._init = init
        self._end = end
        if center:
            #using property to test if its bewtween init and end
            self.center = center
        else:
            self._center = (end + init) / 2
        self._peak = peak
        self._floor = floor

    ### Desctructor ###
    def __close__(self):
        # releases attributes
        self._function = None
        self._init = None
        self._end = None
        self._peak = None
        self._floor = None

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

    ## peak
    @property
    def peak(self):
        return self._peak

    @peak.setter
    def peak(self, peak):
        if type(peak) == float or type(peak) == int:
            self._peak = peak
        else:
            raise ValueError(
                'Error: Function peak element must be float or integer')

    ## floor
    @property
    def floor(self):
        return self._floor

    @floor.setter
    def floor(self, floor):
        if type(floor) == float or type(floor) == int:
            self._floor = floor
        else:
            raise ValueError(
                'Error: Function floor element must be float or integer')

    ### Methods ###
    def function(self, x):
        if x <= self._init:
            return self._floor

        elif x <= self._center:
            delta_y = self._peak - self._floor
            delta_x = self._center - self._init
            slope = delta_y / delta_x
            return slope * (x - self._init) + self._floor

        elif x <= self._end:
            delta_y = self._floor - self._peak
            delta_x = self._end - self._center
            slope = delta_y / delta_x
            return slope * (x - self._center) + self._peak

        else:
            return self._floor