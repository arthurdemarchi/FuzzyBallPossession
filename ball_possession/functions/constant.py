class Constant:
    ### Constructor ###
    def __init__(self, value):
        # initialize attributes
        self._value = value
        
    ### Desctructor ###
    def __close__(self):
        # releases attributes
        self._value = None
       
    ### Getters and Setter (as Properties) ###
    ## value
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if type(value) == float or type(value) == int:
            self._value = value
        else:
            raise ValueError(
                'Error: Function value must be float or integer')

    ### Methods ###
    def function(self, x):
        return self.value