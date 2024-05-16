import streamlit as st
from streamlit_extras.buy_me_a_coffee import button

def load_custom_html():
    st.set_page_config(layout="wide")
    custom_html = """
        <style>
            .stTextInput input {
                height: 300px !important; /* Set the desired height */
                font-size: 16px !important; /* Increase the font size */
            }
            div[data-testid="column"]:nth-of-type(1) {
                padding-right: 2rem;
            }
            div[data-testid="column"]:nth-of-type(2) {
                padding-left: 2rem;
            }
            /* Custom CSS for the expander background color */
            div[role="group"] > div {
                background-color: #ADD8E6 !important; /* Replace this with your desired CSS color */
            }
        </style>
    """
    
    button(username="alexmhayes", floating=True, width=221)
    
    st.markdown(custom_html, unsafe_allow_html=True)

    left_column, right_column = st.columns([7, 2])

    with left_column:
        st.write("")
        
    with right_column:
        st.write("")

    st.sidebar.title("Settings for the model")
    
    st.sidebar.image("https://i.postimg.cc/6q36FdD0/icon.png", width=100)    
    with st.sidebar.expander("Settings", expanded=True):
        settings = {
            "read_documentation": st.checkbox("Read up on documentation", value=True),
            "iterate_on_code": st.checkbox("Refine my code iteratively", value=True),
            "find_mistakes": st.checkbox("Find and fix my own mistakes", value=True),
            "optimise_speed": st.checkbox("80/20 speed up code speed", value=False),
            "no_placeholders": st.checkbox("Write code without placeholders", value=True),
            "dependency_analysis": st.checkbox("Dependency compatibility analysis", value=False)
        }
        
    return settings
