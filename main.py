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
        st.write("Using artificial intelligence to help match billions of dollars in federal grants to your projects and organizations")
        st.button("Find Grants",type="primary")
    with col2: 
        st.image("https://github.com/mtworth/grantr/blob/main/main/corp_art.jpg?raw=true")

    st.markdown('##')     

    #logos evenly distributed 

    seal1, seal2, seal3, seal4, seal5 = st.columns(5)
    with seal1:
        st.image("https://github.com/mtworth/grantr/blob/main/images/NIH_Master_Logo_Vertical_2Color.png?raw=true")
    with seal2:
        st.image("https://github.com/mtworth/grantr/blob/main/images/NIH_Master_Logo_Vertical_2Color.png?raw=true")
    with seal3:
        st.image("https://github.com/mtworth/grantr/blob/main/images/NIH_Master_Logo_Vertical_2Color.png?raw=true")
    with seal4:
        st.image("https://github.com/mtworth/grantr/blob/main/images/NIH_Master_Logo_Vertical_2Color.png?raw=true")
    with seal5:
        st.image("https://github.com/mtworth/grantr/blob/main/images/NIH_Master_Logo_Vertical_2Color.png?raw=true")

    st.markdown('######')     
    col3, col4 = st.columns(2)
    with col3: 
        st.image("https://github.com/mtworth/grantr/blob/main/main/corp_art.jpg?raw=true")
    with col4:
        st.subheader("Artificial Intelligence, Applied")
        st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.")

    st.markdown('##')     
    col5, col6 = st.columns(2)
    with col5:
        st.subheader("Fully Open Source")
        st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.")
    with col6:
        st.image("https://github.com/mtworth/grantr/blob/main/main/corp_art.jpg?raw=true")
 

if page == "About":
    st.write("Welcome again")
if page == "Find Grants":
    st.write("test")