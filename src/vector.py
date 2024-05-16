"""
Copyright (c) leonardo-rocchi:z4ir3
"""
from src.point import Point


class Vector:
    """
    Vector from a first vertex called 'center' to a second 'vertex'
    """
    def __init__(self, center: Point, vertex: Point):
        self.x = vertex.x - center.x
        self.y = vertex.y - center.y