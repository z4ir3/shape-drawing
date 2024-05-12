"""
Copyright (c) leonardo-rocchi:z4ir3
"""
from src.point import Point
from src.vector import VectorFromCenter

class Rectangle:
    """
    Rectangle
    """
    def __init__(self, center, width: float, height: float):
        self.center = center
        self.width = Rectangle._valid_lh(width)
        self.height = Rectangle._valid_lh(height)
        # self.v1 = Rectangle.vertex1(self.center, self.width, self.height)
        # self.v1 = self._vertex1(self)

    @staticmethod
    def _valid_lh(lh: float) -> float:
        if lh <= 0:
            raise ValueError("Cannot insert non-negative width/height")
        else:
            return lh

    def init_vertices(self):
        """
        Initialize Rectangle vertices (aligned with x and y axes)
        """
        # First vertex (bottom right) and corr. vector from the center
        vx = self.center.x + 0.5 * self.width
        vy = self.center.y - 0.5 * self.height
        self.v1 = Point(vx, vy)
        self.vec1 = VectorFromCenter(self.center, self.v1)

        # Second vertex (top right) and corr. vector from the center
        vx = self.center.x + 0.5 * self.width
        vy = self.center.y + 0.5 * self.height
        self.v2 = Point(vx, vy)
        self.vec2 = VectorFromCenter(self.center, self.v2)

        # Third vertex (top left) and corr. vector from the center
        vx = self.center.x - 0.5 * self.width
        vy = self.center.y + 0.5 * self.height
        self.v3 = Point(vx, vy)
        self.vec3 = VectorFromCenter(self.center, self.v3)

        # Fourth vertex (bottom left) and corr. vector from the center
        vx = self.center.x - 0.5 * self.width
        vy = self.center.y - 0.5 * self.height
        self.v4 = Point(vx, vy)
        self.vec4 = VectorFromCenter(self.center, self.v4)









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
        return (self.width**2 + self.height**2)**(0.5)




# from src.point import Point

# class Rectangle:
#     """
#     Rectangle
#     """
#     def __init__(self, center, width: float, height: float):
#         self.center = center
#         self.width = Rectangle._valid_lh(width)
#         self.height = Rectangle._valid_lh(height)
#         # self.v1 = Rectangle.vertex1(self.center, self.width, self.height)
#         # self.v1 = self._vertex1(self)




#     def diagonal(self):
#         """
#         width of the diagonal of the Rectangle
#         """
#         return (self.width**2 + self.height**2)**(0.5)

#     def init_v1(self):
#         """
#         Initialize the first Rectangle vertex
#         """
#         vx = self.center.x + 0.5 * self.length
#         vy = self.center.y - 0.5 * self.heigh
#         return Point(vx,vy)






# # class Shape(object):
# #     def area(self):
# #         raise NotImplementedError

# #     def perimeter(self):
# #         raise NotImplementedError

# class Rectangle(): #Shape):
#     """
#     Rectangle
#     """
#     def __init__(self, center, width: float, height: float):
#         # super(Rectangle, self).__init__() # this is useless in this case, but it's good practice
#         self.center = center
#         self.width = Rectangle._valid_lh(width)
#         self.height = Rectangle._valid_lh(height)

#     @staticmethod
#     def _valid_lh(lh: float) -> float:
#         if lh is None:
#             return None
#         else:
#             if lh <= 0:
#                 raise ValueError("Cannot insert non-negative width/height")
#             else:
#                 return lh

#     @property
#     def center(self):
#         return self.__center

#     @property
#     def width(self):
#         return self.__width

#     @property
#     def height(self):
#         return self.__height




#     @center.setter
#     def center(self, center):
#         self.__center = center

#     @width.setter
#     def width(self, width):
#         self.__width = width

#     @height.setter
#     def height(self, height):
#         self.__height = height



#     def area(self):
#         """
#         Area of the Rectangle
#         """
#         return self.width * self.height

#     def perimeter(self):
#         """
#         Perimeter of the Rectangle
#         """
#         return 2 * (self.width + self.height)





