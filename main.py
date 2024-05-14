import os
import streamlit as st
from streamlit_navigation_bar import st_navbar


st.set_page_config(initial_sidebar_state="collapsed")

page = st_navbar(["Home", "Find Grants", "About"],logo_path="/work/icons8-logo.svg")

if page == "Home":
    st.write("Welcome to the home page")
if page == "Find Grants":
    st.write("Welcome again")