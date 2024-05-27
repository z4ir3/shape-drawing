"""
Copyright (c) leonardo-rocchi:z4ir3
"""
import streamlit as st

# Importing absolute path for deployment as streamlit app
# import sys
# sys.path.insert(1,"/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages/streamlit_option_menu")
from streamlit_option_menu import option_menu


from src.movements import rotation, stretch
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
            "About": ""
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
    # ss = """
    # <style>
    #     .nav-link:hover {
    #     color:rgb(100,100,150);
    # }
    # </style>
    # """
    # st.markdown(ss, unsafe_allow_html=True)

    # Hiding "Made with Streamlit message"
    st.write('''
        <style>
            footer {visibility:hidden;}
        </style>
        ''',
        unsafe_allow_html = True
    )

    # Page title
    st.title("Shape Playground")

    with st.sidebar:
        # Sidebar title
        st.sidebar.title("")

        # Shape selection
        shape = st.selectbox(
            label = "Select the shape",
            options = ["Rectangle","Circle"],
            index = None,
            placeholder = "Shape",
            # key = ""
        )

    if shape is not None:

        match shape:
            case "Rectangle":
                Rect = input_rectangle()
                # if Rect is not None:

            case "Circle":
                pass
                # Circ = input_circle()
                # if Circ is not None:
                #     st.write(Rect.v1)
                #     st.write(Rect.vec1)
            # case _:
            #     return 0

        col1, col2, col3 = st.columns([1,1,1], gap="small")
        with col1:
            st.metric(label = "", value = "Sliding")

            # col1, col2, col3 = st.columns([1,1,1], gap="small")
            # with col1:
            #     # x-coordinate of the Rectangle center
            #     cx = st.number_input(
            #         label = "Center $x$",
            #         min_value = None,
            #         max_value = None,
            #         value = None,
            #         step = 0.1,
            #         format = "%f",
            #         placeholder = "0",
            #         help = "x-coordinate of the Rectangle's center"
            #         # key = None
            #         # on_change=
            #     )

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
                max_value = 3.0,
                value = 1.0,
                step = 0.1,
                format = "%f"
                # keyk = "slider-exp",
                # help = None,
                # on_change = get_T(TType, minvt, maxvt)
            )
            try:
                Rect = stretch(Rect, scaling_factor)
                # st.write(Rect.v1, Rect.v2, Rect.v3, Rect.v4)
                # st.write(Rect.vec1)
            except:
                pass


        if shape == "Rectangle":
            with st.sidebar:
                # Show Rectangle info
                info = Rect.objectinfo

                st.header(f"{info.name}'s vertices")
                with st.container():
                    col1, col2 = st.columns([1,1], gap="small")
                    with col1:
                        st.write(f"1st: {info.v1}")
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
                        st.write(f"Center: {info.center}")
                    with col2:
                        st.write(f"Area: {info.area}")
                with st.container():
                    col1, col2 = st.columns([1,1], gap="small")
                    with col1:
                        st.write(f"Perimeter: {info.perimeter}")
                    with col2:
                        st.write(f"Diagonal: {info.diagonal}")

        # Plot shape
        iplot(Rect)

    else:
        st.write("")
        st.write("")
        st.subheader("...Select a shape from the sidebar menu")



if __name__ == "__main__":
    main()
