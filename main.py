"""
Copyright (c) leonardo-rocchi:z4ir3
"""
import streamlit as st

# Importing absolute path for deployment as streamlit app
# import sys
# sys.path.insert(1,"/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages/streamlit_option_menu")
from streamlit_option_menu import option_menu


from src.movements import rotation
from src.plots import iplot

from src.input_shapes import input_rectangle



def main():
    """
    """
    # Page configuration
    # Streamlit supported icons:
    # https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/
    st.set_page_config(
        page_title = "OOP",
        page_icon = ":arrows_counterclockwise:",
        layout = "wide",
        initial_sidebar_state = "expanded",
        menu_items={
            "About": "# OOP"
        }
    )
    # Remove extra white space
    st.write('''
        <style>
            div.block-container {
                padding-top: 0rem;
            }
        </style>
        ''',
        unsafe_allow_html = True
    )

    # Page title
    st.title("Shape Playground")

    with st.sidebar:
        # Sidebar title
        st.sidebar.title("")


        shape = st.selectbox(
            label = "Select the shape",
            options = ["Rectangle","Circle"],
            index = 0,
            placeholder = "",
            # key = ""
        )

        match shape:
            case "Rectangle":
                Rect = input_rectangle()
                if Rect is not None:
                    st.write(Rect.v1)
                    st.write(Rect.vec1) #, Rect.vec2, Rect.vec3, Rect.vec4)


    col1, col2, col3 = st.columns([1,1,1], gap="small")
    with col1:
        st.metric(label = "", value = "Sliding")
    with col2:
        st.metric(label = "", value = "Rotation")
        with st.container():
            # Angle rotation of the Rectangle
            theta_deg = st.slider(
                label = "Angle (degrees)",
                min_value = -360,
                max_value = +360,
                value = 0,
                step = 5,
                format = "%d",
                # keyk = "slider-exp",
                # help = None,
                # on_change = get_T(TType, minvt, maxvt)
            )
            try:
                Rect = rotation(Rect, theta_deg)
                # st.write(Rect.v1, Rect.v2, Rect.v3, Rect.v4)
                # st.write(Rect.vec1)
            except:
                pass

    with col3:
        st.metric(label = "", value = "Stretching")
        # Stretching scaling factor
        scaling_factor = st.slider(
            label = "Scaling Factor",
            min_value = 0.1,
            max_value = 5.0,
            value = 1.0,
            step = 0.1,
            format = "%f"
            # keyk = "slider-exp",
            # help = None,
            # on_change = get_T(TType, minvt, maxvt)
        )
        # try:
        #     Rect = stretch(Rect, scaling_factor)
        #     # st.write(Rect.v1, Rect.v2, Rect.v3, Rect.v4)
        #     # st.write(Rect.vec1)
        # except:
        #     pass


    if shape == "Rectangle":
        with st.sidebar:
            # Show Rectangle info
            info = Rect.objectinfo

            st.header(f"{info.name}'s vertices")
            with st.container():
                col1, col2 = st.columns([1,1], gap="small")
                with col1:
                    st.write(f"1st: {info.v1}") #({info['v1x']}, {info['v']}))
                with col2:
                    st.write(f"2nd: {info.v2}")
            with st.container():
                col1, col2 = st.columns([1,1], gap="small")
                with col1:
                    st.write(f"3rd: {info.v3}")
                with col2:
                    st.write(f"4th: {info.v4}")

            st.header(f"{info.name}'s center-to-vertex vectors")
            with st.container():
                col1, col2 = st.columns([1,1], gap="small")
                with col1:
                    st.write(f"1st: {info.vec1}")
                with col2:
                    st.write(f"2nd: {info.vec2}")
            with st.container():
                col1, col2 = st.columns([1,1], gap="small")
                with col1:
                    st.write(f"3rd: {info.vec3}")
                with col2:
                    st.write(f"4th: {info.vec4}")

            st.header(f"{info.name}'s other data")
            with st.container():
                col1, col2 = st.columns([1,1], gap="small")
                with col1:
                    st.write(f"Area: {info.area}")
                with col2:
                    st.write(f"Perimeter: {info.perimeter}")
            with st.container():
                col1, col2 = st.columns([1,1], gap="small")
                with col1:
                    st.write(f"Diagonal: {info.diagonal}")



    # Plot shape
    # try:
    iplot(Rect)
    # except:
    #     pass


    #     PageSelected = option_menu(
    #         menu_title = "Option Playgrounds",
    #         menu_icon = "bar-chart",
    #         options=[
    #             # "Home",
    #             "Option Pricing",
    #             "Option Strategies"
    #         ],
    #         icons = [
    #             # "house",
    #             "box-arrow-in-right",
    #             "stack"
    #         ], # icons from the bootstrap webpage
    #         default_index = 0,
    #         orientation = "vertical",
    #         # orientation = "horizontal"
    #         # styles={
    #         #     "container": {"padding": "0!important", "background-color": "#fafafa"},
    #         #     "icon": {"color": "orange", "font-size": "25px"},
    #         #     "nav-link": {"font-size": "25px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
    #         #     "nav-link-selected": {"background-color": "green"},
    #         # }
    #         styles={
    #             "nav-link": {"--hover-color": "#aaa"},
    #         }
    #     )

    #     ss = """
    #     <style>
    #         .nav-link:hover {
    #         color:rgb(100,100,150);
    #     }
    #     </style>
    #     """
    #     st.markdown(ss, unsafe_allow_html=True)




    # Hiding "Made with Streamlit message"
    st.write('''
        <style>
            footer {visibility:hidden;}
        </style>
        ''',
        unsafe_allow_html = True
    )


if __name__ == "__main__":
    main()
