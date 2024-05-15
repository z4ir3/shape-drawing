"""
Copyright (c) leonardo-rocchi:z4ir3
"""
from src.point import Point


class Vector:
    """
    Vector from a first vertex called 'center' to a second 'vertex'
    """
    decround = 1
    def __init__(self, center: Point, vertex: Point):
        self.x = round(vertex.x - center.x, self.decround)
        self.y = round(vertex.y - center.y, self.decround)