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
                'Error: Center of the function must be between init and end')
    else:
        raise ValueError(
            'Error: Function center element must be float or integer')
