"""
Copyright (c) leonardo-rocchi:z4ir3
"""
import streamlit as st

from src.point import Point
from src.rectangle import Rectangle


def input_rectangle():
    """
    """
    # Rectangle input data (center's coordinates, lenght, and height)
    with st.sidebar:
        with st.container():
            col1, col2 = st.columns([1,1], gap="small")
            with col1:
                # x-coordinate of the Rectangle center
                cx = st.number_input(
                    label = "Center $x$",
                    min_value = None,
                    max_value = None,
                    value = None,
                    step = 0.1,
                    format = "%f",
                    placeholder = "0",
                    help = "x-coordinate of the Rectangle's center"
                    # key = None
                    # on_change=
                )
            with col2:
                # y-coordinate of the Rectangle center
                cy = st.number_input(
                    label = "Center $y$",
                    min_value = None,
                    max_value = None,
                    value = None,
                    step = 0.1,
                    format = "%f",
                    placeholder = "0",
                    help = "y-coordinate of the Rectangle's center"
                    # key = None
                    # on_change=
                )
        with st.container():
            col1, col2 = st.columns([1,1], gap="small")
            with col1:
                # Width of the Rectangle
                width = st.number_input(
                    label = "Width",
                    min_value = 0.1,
                    max_value = None,
                    value = None,
                    step = 0.1,
                    format = "%f",
                    placeholder = "10",
                    # # key = None
                    # # on_change
                )
            with col2:
                # Height of the Rectangle
                height = st.number_input(
                    label = "Height",
                    min_value = 0.1,
                    max_value = None,
                    value = None,
                    step = 0.1,
                    format = "%f",
                    placeholder = "5",
                    # # key = None
                    # # on_change=
                )

    try:
        # center = Point(cx,cy)
        # # st.write(center)
        # # st.write(center.x, center.y)

        # Rect = Rectangle(center, ll, hh)
        # Rect.init_vertices()
        # # st.write(Rect.v1, Rect.v2) #, Rect.vy)

        Rect = Rectangle(Point(cx,cy), width, height)
        Rect.init_vertices()
        # Rect.init_vectors()

        st.write(Rect.v1)
        st.write(Rect.vec1, Rect.vec2, Rect.vec3, Rect.vec4)


        return Rect
    except:
        None
