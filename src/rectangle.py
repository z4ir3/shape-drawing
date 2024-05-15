"""
Copyright (c) leonardo-rocchi:z4ir3
"""
from src.point import Point
from src.vector import Vector

class Rectangle:
    """
    Rectangle
    """
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
        return self.width * self.height

    def perimeter(self) -> float:
        """
        Perimeter of the Rectangle
        """
        return 2 * (self.width + self.height)

    def diagonal(self) -> float:
        """
        width of the diagonal of the Rectangle
        """
        return round((self.width**2 + self.height**2)**(0.5), 2)

    @property
    def objectinfo(self) -> dict:
        info = {
            "name": "Rectangle",
            "width": self.width,
            "height": self.height,
            "area": self.area(),
            "perimeter": self.perimeter(),
            "diagonal": self.diagonal(),
            "v1": (self.v1.x, self.v1.y),
            "v2": (self.v2.x, self.v2.y),
            "v3": (self.v3.x, self.v3.y),
            "v4": (self.v4.x, self.v4.y),
            "vec1": (self.vec1.x, self.vec1.y),
            "vec2": (self.vec2.x, self.vec2.y),
            "vec3": (self.vec3.x, self.vec3.y),
            "vec4": (self.vec4.x, self.vec4.y)
        }
        return DotDict(info)
