"""
Copyright (c) leonardo-rocchi:z4ir3
"""
import streamlit as st

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

import plotly.io as pio
pio.renderers.default = "browser"
import plotly.graph_objs as go 

# from src.utils import get_Smax, get_Smin, bscolors
# from models.blackscholes import BSOption


def iplotest(
    nss: int = 80,
    sensname: list = ["Price","Delta","Gamma","Vega","Theta","Rho"],#,"Lambda"],
    rnd: int = 6
) -> None:
    """
    """
    # Page title
    st.title("Shape Playground")
    
    # Hiding "Made with Streamlit message"
    st.write('''
        <style>
            footer {visibility:hidden;}
        </style>
        ''',
        unsafe_allow_html = True
    )

    # par1, par2, par3, par4 = st.columns([1,1,1,0.5], gap="small") 
    # with par1:
    #     # Call or Put price
    #     cp = st.selectbox(
    #         label = "Option type",
    #         options = ["Call","Put"],
    #         index = None,
    #         placeholder = "Call or Put",
    #         key = "option-type"
    #     )
    #     CP = "C" if cp == "Call" else "P"         
    # with par2:
    #     # Strike price 
    #     K = st.number_input(
    #         label = "Option strike ($K$)",
    #         min_value = 0.1,
    #         format = "%f", 
    #         value = None, #100.0,
    #         placeholder = "Enter Strike price",
    #         help = "'Exercise' price of the option",
    #         key = "strike"
    #         # on_change=
    #     ) 
    # with par3:
    #     # Dividend Yield
    #     q = st.number_input(
    #         label = "Dividend Yield ($q$)",
    #         min_value = 0.0,
    #         max_value = None,
    #         format = "%f",
    #         value = 0.0,
    #         help = None,
    #         key = "div-yield"
    #         # on_change=
    #     )
    # with par4:
    #     # Expiration type
    #     TType = st.selectbox(
    #         label = "Expiration type",
    #         options = ["Days","Years"],
    #         index = 0,
    #         key = "dte-type"
    #     ) 

    # with st.sidebar:
    #     with st.container():
    #         # Expiration Slider 
    #         T = st.slider(
    #             label = f"Time-to-Expiration ({TType}) ($\\tau$)", 
    #             min_value = 0 if TType == "Days" else 0.0, 
    #             # max_value = 1825 if TType == "Days" else float(5), 
    #             max_value = 1095 if TType == "Days" else float(3), 
    #             value = 182 if TType == "Days" else 0.50, 
    #             # value = 90 if TType == "Days" else 0.25, 
    #             step = 1 if TType == "Days" else 0.05, 
    #             # format = None, 
    #             key = "slider-exp", 
    #             help = None, 
    #             # on_change = get_T(TType, minvt, maxvt)
    #         )
    #         if TType == "Days": 
    #             T = T / 365

    #     col1, col2 = st.columns(2)
    #     with col1:
    #         # Volatilty Slider 
    #         v = st.slider(
    #             label =  "Volatility (%) ($\sigma$)", 
    #             min_value = 1.0,
    #             max_value = 99.9,
    #             value = 30.0, 
    #             step = 1.0, 
    #             # format = None, 
    #             key = "slider-vola", 
    #             help = None, 
    #             # on_change = get_T(TType, minvt, maxvt)
    #         )
    #         v = v / 100
    #     with col2:
    #         # Interes Rate Slider 
    #         # r = st.sidebar.slider(
    #         r = st.slider(
    #             label = "Interest Rate (%) ($r$)", 
    #             min_value = 0.0,
    #             max_value = 8.0,
    #             value = 2.0, 
    #             key = "slider-irate", 
    #             help = None, 
    #             # on_change = get_T(TType, minvt, maxvt)
    #         )
    #         r = r / 100

    # if True: #(cp is not None) and (K is not None):
        # # Call/Put and Strike inserted

        # # Set up Options
        # uset = np.linspace(get_Smin(K),get_Smax(K),nss)
        # Options = [BSOption(CP=CP, S=s, K=K, T=T, r=r, v=v, q=q) for s in uset]

        # Sens = dict()
        # for s in sensname: 
        #     grk = [o.greeks(grk=s, rnd=rnd) for o in Options]
        #     Sens[s] = pd.Series(grk, index=uset, name=s)
        # # st.write(Sens)
        # # st.write(options[40].greeks()["Price"])

        # # Save ATM points for metric and to be passed in plot functions
        # ATM = {k: dict() for k in sensname}
        # with st.container():
        #     atms = st.columns(len(sensname))        
        #     for idx, s in enumerate(sensname):
        #         # Save ATM points
        #         atmidx = np.argmin(pd.Series(Sens[s].index).apply(lambda x: abs(x - K)))
        #         ATM[s]["x"] = [Sens[s].index[atmidx]]
        #         ATM[s]["y"] = [Sens[s].values[atmidx]]
        #         # ATM[s]["x"] = [K]
        #         # ATM[s]["y"] = [Sens[s].loc[K]]
        #         with atms[idx]:
        #             st.metric(
        #                 label = f"ATM {s}",
        #                 value = f"{ATM[s]['y'][0]:.2f}",
        #                 help = None
        #             )

    with st.container():
        # _, mplt, _ = st.columns([1,8,1], gap="small") 
        # with plot1:   
        # ss = "Price"
        # with mplt:
        fig = _plotshapes()
        st.plotly_chart(fig, use_container_width=False)

    # fig_2 = _plotshapes_2()
    # st.plotly_chart(fig_2, use_container_width=False)


            # with plot2:
            #     ss = "Delta"
            #     fig = _plotgreeks(
            #         Sens[ss], 
            #         CP, 
            #         K, 
            #         lcol = bscolors(ss),
            #         atmv = (ATM[ss]["x"], ATM[ss]["y"]),
            #         yaxside = "right"
            #     )
            #     st.plotly_chart(fig, use_container_width=True)

        # Gamma and Vega
        # with st.container():
        #     plot1, plot2 = st.columns(2)
        #     with plot1:   
        #         ss = "Gamma"
        #         fig = _plotgreeks(
        #             Sens[ss], 
        #             CP, 
        #             K, 
        #             lcol = bscolors(ss),
        #             atmv = (ATM[ss]["x"], ATM[ss]["y"])
        #         )
        #         st.plotly_chart(fig, use_container_width=True)
        #     with plot2:
        #         ss = "Vega"
        #         fig = _plotgreeks(
        #             Sens[ss], 
        #             CP, 
        #             K, 
        #             lcol = bscolors(ss),
        #             atmv = (ATM[ss]["x"], ATM[ss]["y"]),
        #             yaxside = "right"
        #         )
        #         st.plotly_chart(fig, use_container_width=True)

        # # # Theta and Lambda
        # # Theta and Rho
        # with st.container():
        #     plot1, plot2 = st.columns(2)
        #     with plot1: 
        #         ss = "Theta"
        #         fig = _plotgreeks(
        #             Sens[ss], 
        #             CP, 
        #             K, 
        #             lcol = bscolors(ss),
        #             atmv = (ATM[ss]["x"],ATM[ss]["y"]),
        #             xlab = True
        #         )
        #         st.plotly_chart(fig, use_container_width=True)
        #     with plot2:
        #         # ss = "Lambda"
        #         ss = "Rho"
        #         fig = _plotgreeks(
        #             Sens[ss], 
        #             CP, 
        #             K, 
        #             lcol = bscolors(ss),
        #             atmv = (ATM[ss]["x"],ATM[ss]["y"]),
        #             yaxside = "right", 
        #             xlab = True
        #         )
        #         st.plotly_chart(fig, use_container_width=True)



    # except:
    # else:
    #     # Call/Put and Strike not inserted yet 
    #     st.write("insert option and strike")




def _plotshapes(
    plotw: int = 600,
    ploth: int = 600, 
    # data: pd.Series,
    # CP: str,
    # K: float,
    # lcol: str,    
    # atmv: tuple or None = None,
    # yaxside: str = "left",
    gridcolor: str = "#EEF4F4",
    # xlab: bool = False
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
    #     mode="text",
    # ))
    # Add shapes
    fig.add_shape(type="rect",
        x0=1, y0=1, x1=2, y1=3,
        line=dict(color="RoyalBlue"),
    )
    fig.add_shape(type="rect",
        x0=3, y0=1, x1=6, y1=2,
        line=dict(
            color="RoyalBlue",
            width=2,
        ),
        fillcolor="LightSkyBlue",
    )
 

    # Add circles
    fig.add_shape(type="circle",
        xref="x", yref="y",
        x0=1, y0=1, x1=3, y1=3,
        line_color="LightSeaGreen",
    )
    fig.add_shape(type="circle",
        xref="x", yref="y",
        fillcolor="PaleTurquoise",
        x0=3, y0=3, x1=4, y1=5,
        line_color="LightSeaGreen",
    )

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







def _plotshapes_2():
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=[0, 1, 2, 3, 4, 5, 6, 7, 8],
        y=[0, 1, 2, 3, 4, 5, 6, 7, 8]
    ))

    fig.update_layout(
        autosize=False,
        width=500,
        height=500,
        margin=dict(
            l=50,
            r=50,
            b=100,
            t=100,
            pad=4
        ),
        paper_bgcolor="LightSteelBlue",
    )
    return fig

