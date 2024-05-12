"""
Copyright (c) leonardo-rocchi:z4ir3
"""

class Rectangle:
    """
    Rectangle
    """
    def __init__(self, center, lenght: float, height: float):
        self.center = center
        self.lenght = Rectangle._valid_lh(lenght)
        self.height = Rectangle._valid_lh(height)


    @staticmethod
    def _valid_lh(lh: float) -> float:
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
