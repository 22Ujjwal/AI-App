import streamlit as st                                    # to get webbased interface
from langchain_ollama import ChatOllama                   # for generation of ai solution responses
from langchain_core.output_parsers import StrOutputParser # For formating output

from langchain_core.prompts import (
    SystemMessagePromptTemplate, HumanMessagePromptTemplate, AIMessagePromptTemplate, ChatPromptTemplate )

# Custom CSS for Spotify-inspired theme
st.markdown("""
<style>
    /* Main background and text color */
    .main {
        background-color: #121212; /* dark background */
        color: #ffffff; /* White text */
    }
    
    /* Sidebar background and text color */
    .sidebar .sidebar-content {
        background-color: #181818; /* Slightly lighter than main background */
        color: #ffffff;
    }
    
    /* Text input styling */
    .stTextInput textarea {
        color: #ffffff !important;
        background-color: #282828 !important; /* Darker background for input */
        border-radius: 5px;
    }
    
    /* Select box styling */
    .stSelectbox div[data-baseweb="select"] {
        color: white !important;
        background-color: #282828 !important; /* Darker background for select box */
        border-radius: 5px;
    }
    
    .stSelectbox svg {
        fill: white !important;
    }
    
    .stSelectbox option {
        background-color: #282828 !important;
        color: white !important;
    }
    
    /* Dropdown menu items */
    div[role="listbox"] div {
        background-color: #282828 !important;
        color: white !important;
    }
    
    /* Button styling */
    .stButton button {
        background-color: #1DB954 !important; /* green */
        color: white !important;
        border-radius: 20px;
        border: none;
        padding: 10px 20px;
        font-weight: bold;
    }
    
    /* Header and title styling */
    h1, h2, h3, h4, h5, h6 {
        color: #1DB954 !important; /* green for headers */
    }
    
    /* Divider styling */
    .stDivider {
        border-bottom: 1px solid #1DB954 !important; /* green for dividers */
    }
    
    /* Link styling */
    a {
        color: #1DB954 !important; /* Spotify green for links */
        text-decoration: none;
    }
    
    a:hover {
        text-decoration: underline;
    }
</style>
""", unsafe_allow_html=True)

# Title and caption
st.title("Guru")
st.caption("Personal Coach Powered by Cutting Edge AI Technology")

# Sidebar configuration
with st.sidebar:
    st.markdown("""## Model Capabilities
- Skill Assessment
- Personalized Learning Path
- Roadmap Generation""")
    selected_model = st.selectbox(
        "Large Language Model",
        ["deepseek-r1","Further LLMs Unsupported"],
        index=0
    )
st.markdown("""
### 
I am your **Career Companion**, your personalized AI-powered assistant to help you stay ahead at work. 
Whether you're looking to *learn new skills* or *deepen your expertise* in your current field, I can help you!
""")
    


# Example button for uploading resume
st.button("📥 Upload Resume")

# Example button for generating roadmap
st.button("💡 Generate Analysis")

st.divider()
"Tip 🛠️ : Update your resume to get more insightful results"


llm_engine=ChatOllama(
    model=selected_model,
    base_url="",
    temperature=0.3

)
