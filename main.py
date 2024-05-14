import os
import streamlit as st
from streamlit_navigation_bar import st_navbar


st.set_page_config(initial_sidebar_state="collapsed")

page = st_navbar(["","","","","Home", "Find Grants", "About"])#,logo_path="https://raw.githubusercontent.com/mtworth/grantr/f558bf2f6245deaa1035d12f04df8e181492017a/images/logoipsum-311.svg")

if page == "Home":
    col1, col2 = st.columns(2)
    with col1: 
        #make this bold colored large font matching the brand primary color
        st.header("Grantr Match")
        st.write("Using artificial intelligence to help match billions of dollars in federal grants to your project and organization.")
        st.button("Find Grants",type="primary")
    with col2: 
        st.image("https://github.com/mtworth/grantr/blob/main/main/corp_art.jpg?raw=true")

    #logos evenly distributed 

    seal1, seal2, seal3, seal4, seal5 = st.columns(5)

    w = 50
    with seal1:
        st.image("https://github.com/mtworth/grantr/blob/main/images/NIH_Master_Logo_Vertical_2Color.png?raw=true",width=w)
    with seal2:
        st.image("https://github.com/mtworth/grantr/blob/main/images/NIH_Master_Logo_Vertical_2Color.png?raw=true",width =w)
    with seal3:
        st.image("https://github.com/mtworth/grantr/blob/main/images/NIH_Master_Logo_Vertical_2Color.png?raw=true",width=w)
    with seal4:
        st.image("https://github.com/mtworth/grantr/blob/main/images/NIH_Master_Logo_Vertical_2Color.png?raw=true",width=w)
    with seal5:
        st.image("https://github.com/mtworth/grantr/blob/main/images/NIH_Master_Logo_Vertical_2Color.png?raw=true",width=w)

    col3, col4 = st.columns(2)
    with col3: 
        st.image("https://github.com/mtworth/grantr/blob/main/main/corp_art.jpg?raw=true")
    with col4:
        st.subheader("Artificial Intelligence, Applied")
        st.write("We use state of the art generative AI to help remove the tedious work of searching grants and tell you whether a grant is the right match for you and your project.")

    col5, col6 = st.columns(2)
    with col5:
        st.subheader("Fully Open Source")
        st.write("This entire application is built entirely on the Snowflake open source ecosystem, including Streamlit and Artic LLM. No need to worry about shady data pipelines and questionable AI.")
    with col6:
        st.image("https://github.com/mtworth/grantr/blob/main/main/corp_art.jpg?raw=true")
 

if page == "About":
    st.write("Welcome again")
if page == "Find Grants":
    st.write("test")