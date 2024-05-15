import os
import streamlit as st
from streamlit_navigation_bar import st_navbar
from streamlit_extras.stylable_container import stylable_container 


st.set_page_config(initial_sidebar_state="collapsed")

page = st_navbar(["","","","","Home", "Find Grants", "About"])#,logo_path="https://raw.githubusercontent.com/mtworth/grantr/f558bf2f6245deaa1035d12f04df8e181492017a/images/logoipsum-311.svg")

if page == "Home":
    col1, col2 = st.columns(2)
    with col1: 
        #make this bold colored large font matching the brand primary color
        st.header("Match to Grants")
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
    with st.form("Submission Form"):
        st.subheader("Grant Match Submission Form")
        st.write("Before we can match you to open federal grants, we need to know a bit more about and what you're trying to accomplish with grant funds.")
        st.write("Who are you?")
        entity = st.text_input("Examples: local nonprofit, city government, individual, etc.")
        st.write("What are you trying to fund?")
        proposal = st.text_input("Examples: a research project on ocean acidiciation, a local community program, building a new bridge, etc.")
        submitted = st.form_submit_button("Match My Project!",type="primary")
        
        #if st.button("Submit"):
        #    st.session_state.proposal = {"entity": entity, "proposal": proposal}
    if submitted:
        #TODO put them all in a container? 
        st.write("XX grants found!")
        behindbutton, forwardbutton = st.columns(2)
        with behindbutton:
            st.button("◀ Prior Grant",use_container_width=True)
        with forwardbutton:
            st.button("Next Grant ▶",use_container_width=True)
        with st.container(border = True):
            st.subheader("Opportunity Title")
            st.write("🏛️ **Agency**: US Department of Transportation")
            st.write("💵 **Grant Range**: \$50,000 to \$100,000")
            st.write("📅 **Due Date**: 5/14/2024")
            st.write("**📄 Opportunity Description**")
            st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")

            st.write("**🤖 Grant Match Verdict** (AI Generated)")
            #annotated_text((" ", "AI-Generated"))
            
            with stylable_container(
                    key="container_with_border",
                    css_styles="""
                        {
                            border: 1px solid rgba(49, 51, 63, 0.2);
                            border-radius: 0.5rem;
                            padding: calc(1em - 1px);
                            background-color: lightgreen

                        }
                        """,
                ):
                    st.markdown("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")
            ##st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")
            
            col1, col2, col3 = st.columns(3)

            with col1:
                st.link_button("**Email Details** ✉️","mailto:?subject=Exciting%20Grant%20Opportunity",use_container_width=True)
            with col3: 
                #TODOfix grants link 
                st.link_button("**Apply** 😏","https://www.grants.gov",type="primary",use_container_width=True)
