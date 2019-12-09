class Trapezoid:
    ### Constructor ###
    def __init__(self, init, end, peak_init, peak_end, peak=1, floor=0):
        # initialize attributes
        self._init = init
        self._end = end
        self._peak_init = peak_init
        self._peak_end = peak_end
        self._peak = peak
        self._floor = floor

    ### Desctructor ###
    def __close__(self):
        # releases attributes
        self._init = None
        self._end = None
        self._peak_init = None
        self._peak_end = None
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

    ## peak_init
    @property
    def peak_init(self):
        return self._peak_init

    @peak_init.setter
    def peak_init(self, peak_init):
        if type(peak_init) == float or type(peak_init) == int:
            self._peak_init = peak_init
        else:
            raise ValueError(
                'Error: Function first peak element must be float or integer')

    ## peak_end
    @property
    def peak_end(self):
        return self._peak_end

    @peak_end.setter
    def peak_end(self, peak_end):
        if type(peak_end) == float or type(peak_end) == int:
            self._peak_end = peak_end
        else:
            raise ValueError(
                'Error: Function final peak element must be float or integer')

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

        elif x <= self._peak_init:
            delta_y = self._peak - self._floor
            delta_x = self._peak_init - self._init
            slope = delta_y / delta_x
            return slope * (x - self._init) + self._floor

        elif x <= self._peak_end:
            return self._peak

        elif x <= self._end:
            delta_y = self._floor - self._peak
            delta_x = self._end - self._peak_end
            slope = delta_y / delta_x
            return slope * (x - self._peak_end) + self._peak

        else:
            return self._floor