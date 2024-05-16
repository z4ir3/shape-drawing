"""
Copyright (c) leonardo-rocchi:z4ir3
"""

from src.utils import DotDict
from src.point import Point
from src.vector import Vector


class Rectangle:
    """
    Rectangle
    """
    prc = 1

    def __init__(self, center: Point, width: float, height: float):
        self.center = center
        self.width = Rectangle._valid_lh(width)
        self.height = Rectangle._valid_lh(height)

    @staticmethod
    def _valid_lh(lh: float) -> float:
        if lh <= 0:
            raise ValueError("Cannot insert non-negative width/height")
        else:
            return lh

    def set_vertices(self) -> None:
        """
        Initialize Rectangle vertices (aligned with x and y axes)
        """
        # First vertex (bottom right) and corr. vector from the center
        vx = self.center.x + 0.5 * self.width
        vy = self.center.y - 0.5 * self.height
        self.v1 = Point(vx, vy)
        self.vec1 = Vector(self.center, self.v1)

        # Second vertex (top right) and corr. vector from the center
        vx = self.center.x + 0.5 * self.width
        vy = self.center.y + 0.5 * self.height
        self.v2 = Point(vx, vy)
        self.vec2 = Vector(self.center, self.v2)

        # Third vertex (top left) and corr. vector from the center
        vx = self.center.x - 0.5 * self.width
        vy = self.center.y + 0.5 * self.height
        self.v3 = Point(vx, vy)
        self.vec3 = Vector(self.center, self.v3)

        # Fourth vertex (bottom left) and corr. vector from the center
        vx = self.center.x - 0.5 * self.width
        vy = self.center.y - 0.5 * self.height
        self.v4 = Point(vx, vy)
        self.vec4 = Vector(self.center, self.v4)

    def area(self) -> float:
        """
        Area of the Rectangle
        """
        return round(self.width * self.height, self.prc)

    def perimeter(self) -> float:
        """
        Perimeter of the Rectangle
        """
        return round(2 * (self.width + self.height), self.prc)

    def diagonal(self) -> float:
        """
        width of the diagonal of the Rectangle
        """
        return round((self.width**2 + self.height**2)**(0.5), self.prc)

    @property
    def objectinfo(self) -> dict:
        info = {
            "name": "Rectangle",
            "center": (round(self.center.x, self.prc), round(self.center.y, self.prc)),
            "width": round(self.width, self.prc),
            "height": round(self.height, self.prc),
            "area": round(self.area(), self.prc),
            "perimeter": round(self.perimeter(), self.prc),
            "diagonal": round(self.diagonal(), self.prc),
            "v1": (round(self.v1.x, self.prc), round(self.v1.y, self.prc)),
            "v2": (round(self.v2.x, self.prc), round(self.v2.y, self.prc)),
            "v3": (round(self.v3.x, self.prc), round(self.v3.y, self.prc)),
            "v4": (round(self.v4.x, self.prc), round(self.v4.y, self.prc)),
            "vec1": (round(self.vec1.x, self.prc), round(self.vec1.y, self.prc)),
            "vec2": (round(self.vec2.x, self.prc), round(self.vec2.y, self.prc)),
            "vec3": (round(self.vec3.x, self.prc), round(self.vec3.y, self.prc)),
            "vec4": (round(self.vec4.x, self.prc), round(self.vec4.y, self.prc)),
        }
        return DotDict(info)
