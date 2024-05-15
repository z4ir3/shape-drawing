"""
Copyright (c) leonardo-rocchi:z4ir3
"""

class Point:
    """
    Point
    """
    decround = 1
    def __init__(self, x: float, y: float):
        self.x = round(x, self.decround)
        self.y = round(y, self.decround)