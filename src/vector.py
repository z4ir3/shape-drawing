"""
Copyright (c) leonardo-rocchi:z4ir3
"""


class VectorFromCenter:
    """
    Vector
    """
    def __init__(self, center, vertex):
        self.x = vertex.x - center.x
        self.y = vertex.y - center.y