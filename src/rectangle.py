"""
Copyright (c) leonardo-rocchi:z4ir3
"""

class Rectangle:
    def __init__(self, c1: float, c2: float, lenght: float, height: float):
        self.c1 = c1
        self.c2 = c2
        self.lenght = Rectangle._valid_ll(lenght)
        self.height = Rectangle._valid_hh(height)

    @staticmethod
    def _valid_ll(lh: float) -> float:
        if lh <= 0:
            raise ValueError("Cannot insert non-negative lenght/height")
        else:
            return lh


    # def areaRett(object):
    #     return object.lenght * object.height;

    # def perimRett(object):
    #     return (2 * object.lenght) + (2 * object.height);

    # def diagRett(object):
    #     return (object.lenght**2 + object.height**2)**(0.5);
