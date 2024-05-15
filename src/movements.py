"""
Copyright (c) leonardo-rocchi:z4ir3
"""
from typing import ClassVar
from math import pi, sin, cos

from src.point import Point
from src.vector import Vector


def rotation(Obj: ClassVar, angle: float) -> ClassVar:
    """
    Rotation of a shape.

    Rotation matrix:
        Rtheta = [cos(theta) -sin(theta)]
                 [sin(theta)  cos(theta)]

    where theta = angle * pi / 180, with
    angle being expressed in degrees

    Rotation: The new vertex is obtained by
        v_new = center + Rtheta * vec_old

    where vec_old is the current center-to-vertex vector
    with center being the center of the shape
    """
    # Angle in radiants
    theta = angle * pi / 180

    # New first vertex and corresponding center-to-vertex vector
    v1x = Obj.center.x + (Obj.vec1.x * cos(theta) - Obj.vec1.y * sin(theta))
    v1y = Obj.center.y + (Obj.vec1.x * sin(theta) + Obj.vec1.y * cos(theta))
    Obj.v1 = Point(v1x,v1y)
    Obj.vec1 = Vector(Obj.center, Obj.v1)

    # New second vertex and corresponding center-to-vertex vector
    v2x = Obj.center.x + (Obj.vec2.x * cos(theta) - Obj.vec2.y * sin(theta))
    v2y = Obj.center.y + (Obj.vec2.x * sin(theta) + Obj.vec2.y * cos(theta))
    Obj.v2 = Point(v2x,v2y)
    Obj.vec2 = Vector(Obj.center, Obj.v2)

    # New third vertex and corresponding center-to-vertex vector
    v3x = Obj.center.x + (Obj.vec3.x * cos(theta) - Obj.vec3.y * sin(theta))
    v3y = Obj.center.y + (Obj.vec3.x * sin(theta) + Obj.vec3.y * cos(theta))
    Obj.v3 = Point(v3x,v3y)
    Obj.vec3 = Vector(Obj.center, Obj.v3)

    # New fourth vertex and corresponding cetner-to-vertex vector
    v4x = Obj.center.x + (Obj.vec4.x * cos(theta) - Obj.vec4.y * sin(theta))
    v4y = Obj.center.y + (Obj.vec4.x * sin(theta) + Obj.vec4.y * cos(theta))
    Obj.v4 = Point(v4x,v4y)
    Obj.vec4 = Vector(Obj.center, Obj.v4)

    return Obj


def stretch(Obj: ClassVar, sfactor: float) -> ClassVar:
    """
    Uniform stretching (homothety):
    - dilation: |sfactor| > 1
    - contraction: 0 < |sfactor| < 1
    """
    if sfactor < 0:
        raise ValueError("The stretching scaling factor must be > 0")

    # New first vertex and corresponding center-to-vertex vector
    v1x = Obj.center.x + sfactor * Obj.vec1.x
    v1y = Obj.center.y + sfactor * Obj.vec1.y
    Obj.v1 = Point(v1x,v1y)
    Obj.vec1 = Vector(Obj.center, Obj.v1)

    # New second vertex and corresponding center-to-vertex vector
    v2x = Obj.center.x + sfactor * Obj.vec2.x
    v2y = Obj.center.y + sfactor * Obj.vec2.y
    Obj.v2 = Point(v2x,v2y)
    Obj.vec2 = Vector(Obj.center, Obj.v2)

    # New third vertex and corresponding center-to-vertex vector
    v3x = Obj.center.x + sfactor * Obj.vec3.x
    v3y = Obj.center.y + sfactor * Obj.vec3.y
    Obj.v3 = Point(v3x,v3y)
    Obj.vec3 = Vector(Obj.center, Obj.v3)

    # New fourth vertex and corresponding center-to-vertex vector
    v4x = Obj.center.x + sfactor * Obj.vec4.x
    v4y = Obj.center.y + sfactor * Obj.vec4.y
    Obj.v4 = Point(v4x,v4y)
    Obj.vec4 = Vector(Obj.center, Obj.v4)

    # Stretching a shape also change




