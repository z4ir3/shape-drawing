"""
Copyright (c) leonardo-rocchi:z4ir3
"""

import streamlit as st

import pandas as pd
import numpy as np

from typing import ClassVar

import matplotlib.pyplot as plt
import plotly.io as pio
pio.renderers.default = "browser"
import plotly.graph_objs as go


def iplot(Rect: ClassVar) -> None:
    """
    """
    # Hiding "Made with Streamlit message"
    st.write('''
        <style>
            footer {visibility:hidden;}
        </style>
        ''',
        unsafe_allow_html = True
    )

    with st.container():
        # _, mplt, _ = st.columns([1,8,1], gap="small")
        # with plot1:
        # ss = "Price"
        # with mplt:
        fig = _plotshapes(Rect)
        st.plotly_chart(fig, use_container_width=False)


def _plotshapes(
    Rect: ClassVar,
    plotw: int = 800,
    ploth: int = 800,
    gridcolor: str = "#EEF4F4",
):
    """
    """
    # Create figure
    fig = go.Figure()

    # Creating a first trace for the horizontal zero line
    # fig.add_trace(
    #     go.Scatter(
    #         x = [1.2,2], #data.index,
    #         y = [1,2], #np.repeat(0,len(data.index)),
    #         name = None,
    #         line_dash = "longdash",
    #         line_color = "#C6C6C6",
    #         line_width = 1,
    #         showlegend = False,
    #         hoverinfo = "none"
    #     )
    # )

    # # Lable x-axis
    # if xlab:
    #     xlabel = f"Underlying S (K={K})"
    # else:
    #     xlabel = None

    # # legend position
    # if (CP == "P") and (data.name in ["Price","Lambda"]):
    #     legpos = dict(yanchor = "top", y = 0.99, xanchor = "right", x = 0.99)
    # elif (CP == "C") and (data.name == "Lambda"):
    #     legpos = dict(yanchor = "top", y = 0.99, xanchor = "right", x = 0.99)
    # elif data.name == "Theta":
    #     legpos = dict(yanchor = "bottom", y = 0.01, xanchor = "left", x = 0.01)
    # else:
    #     legpos = dict(yanchor = "top", y = 0.99, xanchor = "left", x = 0.01)



    # fig.add_trace(go.Scatter(
    #     x=[1.5, 4.5],
    #     y=[0.75, 0.75],
    #     text=["Unfilled Rectangle", "Filled Rectangle"],
    #   mode="text",
    # ))

    # fig.add_trace(go.Scatter(
    #     x=[0,1,2,0],
    #     y=[0,2,0,0],
    #     fill="toself"
    # ))


    # st.write(Rect.v1, Rect.v2, Rect.v3, Rect.v4)

    fig.add_trace(go.Scatter(
        x=[Rect.v1.x, Rect.v2.x, Rect.v3.x, Rect.v4.x, Rect.v1.x],
        y=[Rect.v1.y, Rect.v2.y, Rect.v3.y, Rect.v4.y, Rect.v1.y],
        fill="toself"
    ))


    # # Add shapes
    # fig.add_shape(type="rect",
    #     x0=1, y0=1.3, x1=1, y1=4.6,
    #     line=dict(color="RoyalBlue"),
    # )
    # fig.add_shape(type="rect",
    #     x0=3, y0=1, x1=6, y1=2,
    #     line=dict(
    #         color="RoyalBlue",
    #         width=2,
    #     ),
    #     fillcolor="LightSkyBlue",
    # )


    # # Add circles
    # fig.add_shape(type="circle",
    #     xref="x", yref="y",
    #     x0=1, y0=1, x1=3, y1=3,
    #     line_color="LightSeaGreen",
    # )
    # fig.add_shape(type="circle",
    #     xref="x", yref="y",
    #     fillcolor="PaleTurquoise",
    #     x0=3, y0=3, x1=4, y1=5,
    #     line_color="LightSeaGreen",
    # )

    fig.update_shapes(dict(xref='x', yref='y'))
    # fig.show()  # open the plot in a new browser's tab


    # Update layout
    fig.update_layout(
        # title = {"text": "", "font_size": 22},
        xaxis = dict(title = None),
        yaxis = dict(title = None, side = "left"),
        hovermode = "x",
        hoverlabel = dict(
            #bgcolor = "white",
            font_size = 14,
            # font_family = "Rockwell"
        ),
        autosize = False,
        # legend = legpos,
        plot_bgcolor = "#E6E6E6",
        legend_bgcolor = "#E6E6E6",
        legend_font_color = "#000000",
        legend_borderwidth = 0,
        margin_pad = 0,
        width = plotw,  # Specify the width of the plot in pixels
        height = ploth,  # Specify the height of the plot in pixels
        margin = dict(l=0, r=0, t=32, b=0)  # Set margins around the plot
    )
    fig.update_xaxes(
        showgrid = True,
        zeroline = False,
        gridcolor = gridcolor,
        range = [0, 6]
    )
    fig.update_yaxes(
        showgrid = True,
        zeroline = False,
        gridcolor = gridcolor,
        range = [0, 6]
    )
    return fig
