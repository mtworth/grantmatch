import os
import streamlit as st
from streamlit_navigation_bar import st_navbar
from streamlit_extras.stylable_container import stylable_container 
import requests
import zipfile
import io
import pandas as pd
import numpy as np
import torch
from sentence_transformers.util import semantic_search
from sentence_transformers import SentenceTransformer
import replicate

###############################################################################################################################################
###### SET-UP NAVIGATION BAR ##################################################################################################################
###############################################################################################################################################

st.set_page_config(initial_sidebar_state="collapsed")

styles = {
    "nav": {
        "background-color": "#2A1E5C",
        "justify-content": "right",
    },
    "img": {
        "padding-right": "14px",
    },
    "span": {
        "color": "white",
        "padding": "14px",
    },
    "hover": {
        "background-color": "white",
        "color": "var(--text-color)",
        "font-weight": "normal",
        "padding": "14px",
    }
}


page = st_navbar(["","","","","Home", "Find Grants"],styles=styles)#,logo_path="https://raw.githubusercontent.com/mtworth/grantr/f558bf2f6245deaa1035d12f04df8e181492017a/images/logoipsum-311.svg")

###### IMPORT GRANTS EMBEDDING ##################################################################################################################
###############################################################################################################################################

# URL of the zip file
url = "https://github.com/mtworth/grantmatch/blob/main/embedded_grants.zip?raw=true"

# Download the zip file
response = requests.get(url)
if response.status_code == 200:
    # Open the zip file as a byte stream
    with zipfile.ZipFile(io.BytesIO(response.content)) as z:
        # List all contents of the zip file
        print(z.namelist())
        
        # Extract the .csv file
        with z.open('embedded_grants.csv') as f:
            # Read the .csv file into a pandas DataFrame
            grants_df = pd.read_csv(f)

model = SentenceTransformer("Snowflake/snowflake-arctic-embed-m")

def convert(item):
    item = item.strip()  # remove spaces at the end
    item = item[1:-1]    # remove `[ ]`
    item = np.fromstring(item, sep=' ')  # convert string to `numpy.array`
    return item

grants_df['document_embeddings'] = grants_df['document_embeddings'].apply(convert)

document_embeddings = np.array(grants_df['document_embeddings'].tolist(), dtype=np.float32)

###### CREATE APP FLOW ##################################################################################################################


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
 

#if page == "About":
#    st.write("Grant Match is a live, working tool I developed to help individuals and organizations match to the billions of dollars in grants awarded by the federal government every year. After a decade in the public sector and having applied to dozens of grants and contracts, I saw an opportunity to experiment with generative AI to smooth this process. This tool is fully open source and free to use. For more details, check out the GitHub repo. Made with ❤ with Streamlit and Snowflake. -Maxwell")
             
###TODO Add form submission to session state. Display buttons if session state is not empty. 
if page == "Find Grants":

    # Initialize index
    if 'index' not in st.session_state:
        st.session_state.index = 0

    with st.container(border = True):
    #with st.form("Submission Form"):
        if 'proposal' not in st.session_state:
            st.session_state.proposal = ''
        st.subheader("Grant Match Submission Form")
        st.write("Before we can match you to open federal grants, we need to know a bit more about and what you're trying to accomplish with grant funds.")
        #st.write("Who are you?")
        #entity = st.text_input("Examples: local nonprofit, city government, individual, etc.")
        st.write("What are you trying to fund?")
        proposal = st.text_area("Examples: a research project on ocean acidiciation, a local community program, building a new bridge, etc.")
        #submitted = st.form_submit_button("Match My Project!",type="primary")
        if st.button("Match My Project!",type="primary"):
            st.session_state.proposal = proposal
            st.session_state.index = 0


    #if proposal session state is not empty, then do the below. 
    if st.session_state.proposal:
        query_embeddings = model.encode(proposal, prompt_name="query")
        dataset_embeddings_torch = torch.from_numpy(document_embeddings).to(torch.float)
        query_embeddings_torch = torch.FloatTensor(query_embeddings)
        k = len(dataset_embeddings_torch)
        hits = semantic_search(query_embeddings_torch, dataset_embeddings_torch, top_k=k)

        # Flatten the nested list and convert to DataFrame
        search_df = pd.DataFrame([item for sublist in hits for item in sublist])

        # Set index and join with grants_df
        result = (
            grants_df[['opportunityid','opportunitytitle','agencyname','eligibleapplicants',
                    'additionalinformationoneligibility','description','awardfloor',
                    'awardceiling','postdate','closedate','grantorcontactemail']]
            .join(search_df.set_index('corpus_id'))
        )

        # Filter and sort in one step
        dataset = result[(result['score'] > 0.25) & (result['description'].str.len() > 100)].sort_values(by='score', ascending=False).reset_index(drop=True)
        
        


        num_results = len(dataset)
        award_ceiling_sum = dataset['awardceiling'].dropna().sum() / 1000000
        award_ceiling_sum = dataset['awardceiling'].dropna().sum() / 1000000
        if award_ceiling_sum >= 1000:
            award_ceiling_display = f"${award_ceiling_sum / 1000:.2f} billion"
        else:
            award_ceiling_display = f"${award_ceiling_sum:.2f} million"

        
        if num_results > 0:

            with st.container(border = True):

                st.subheader("**Search Results**")
                st.write(f"**{num_results}** grants found with more than **{award_ceiling_display}** available in funding! Use the buttons below to page through the results.")
                behindbutton, forwardbutton = st.columns(2)
                with behindbutton:
                    if st.button("◀ Prior Grant", key='behindbutton', use_container_width=True):
                        #st.session_state.index = max(0, st.session_state.index - 1)
                        st.session_state.index -= 1
                with forwardbutton:
                    if st.button("Next Grant ▶",use_container_width=True):
                        st.session_state.index += 1





            page = st.session_state.index
            description = dataset.iloc[page]['description']
            opportunitytitle = dataset.iloc[page]['opportunitytitle']
            opportunityid = dataset.iloc[page]['opportunityid']
            awardceiling = dataset.iloc[page]['awardceiling']
            awardfloor = dataset.iloc[page]['awardfloor']
            closedate = dataset.iloc[page]['closedate']
            agencyname = dataset.iloc[page]['agencyname']
            postdate = dataset.iloc[page]['postdate']
            grantorcontactemail = dataset.iloc[page]['grantorcontactemail']
            grant_link = "https://www.grants.gov/search-results-detail/"  + str(dataset.iloc[page]['opportunityid'])

            
            os.environ["REPLICATE_API_TOKEN"] = ""
            api = replicate.Client(api_token=os.environ["REPLICATE_API_TOKEN"])

            input = {
                "prompt": f"You a helpful grant assistant. Talk to a prospective applicant has proposed a project: {proposal}. The grant in question is {description}. Keep your response short and concise, no more than 2-3 sentences. Treat it like a snappy verdict. Include at least one helpful tip. Your personality is overly cheery. The grants have already been matched, so if you don't think it's a good match, include recommendations for how to tweak the project to meet the grant.",
                "temperature": 0.2
            }

            output = api.run(
                "snowflake/snowflake-arctic-instruct",
                input=input

            )

            verdict = "".join(output)


            grantmatchverdict = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

            with st.container(border = True):
                st.subheader(opportunitytitle)
                st.write(f"🏛️ **Agency**: {agencyname}")
                st.write(f"💵 **Grant Range**: \${awardfloor} - \${awardceiling}")
                st.write(f"📅 **Due Date**: {closedate}")
                st.write(f"**✉️ Grant Contact:** {grantorcontactemail}")
                st.write(f"**📄 Opportunity Description**")
                st.write(f"{description}")

                st.write("**🤖 Grant Match Verdict** (AI Generated)")
                
                st.info(verdict)

                col1, col2, col3 = st.columns(3)

                with col3: 
                    #TODOfix grants link 
                    st.link_button("**Apply** 😏",grant_link,type="primary",use_container_width=True)
        else:
            st.subheader("**Search Results**")
            st.write("Unfortunately, we couldn't find any grants that match your project. Consider updating your proposal. Better luck next time! 😃")

