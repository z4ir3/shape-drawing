"""
Copyright (c) leonardo-rocchi:z4ir3
"""
import streamlit as st

# Importing absolute path for deployment as streamlit app
# import sys
# sys.path.insert(1,"/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages/streamlit_option_menu")
from streamlit_option_menu import option_menu

from src.test import iplotest

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
                _ = input_rectangle()


    # Plot shape
    _ = iplotest()



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
