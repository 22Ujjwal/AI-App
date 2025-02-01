import streamlit as st                                    # to get webbased interface
from langchain_ollama import ChatOllama                   # for generation of ai solution responses
from langchain_core.output_parsers import StrOutputParser # For formating output

from langchain_core.prompts import (
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    AIMessagePromptTemplate,
    ChatPromptTemplate
)

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
st.title("🧠 DeepSeek Career Coach")
st.caption("🚀 Your AI Pair to Navigate the Professional Skills")

# Sidebar configuration
with st.sidebar:
    st.header("⚙️ Configuration")
    selected_model = st.selectbox(
        "Choose Model",
        ["deepseek-r1:1.5b", "deepseek-r1:7b", "deepseek-r1:8B"],
        index=0
    )
    st.divider()
    st.markdown("### Model Capabilities")



# Main content
st.markdown("""
### 🛠️ Skill Enhancement Roadmap for Professionals

Welcome to the **DeepSeek Code Companion**, your personalized AI-powered assistant designed to help you stay ahead in your career. Whether you're looking to learn new skills or deepen your expertise in your current field, we've got you covered.

#### How It Works:
1. **Skill Assessment**: Based on your current resume, the model will suggest skills that can enhance your professional growth.
2. **Personalized Learning Path**: If you've already mastered the suggested skills, the model will ask where you want to improve and suggest higher-level concepts.
3. **Roadmap Generation**: Get a detailed roadmap with descriptions, resources, and milestones to achieve your learning goals.

#### Example Roadmap:
- **Beginner Level**: 
  - Learn the basics of Python programming.
  - Understand data structures and algorithms.
- **Intermediate Level**:
  - Dive into web development with frameworks like Django or Flask.
  - Explore data analysis with Pandas and NumPy.
- **Advanced Level**:
  - Master machine learning concepts with TensorFlow or PyTorch.
  - Learn about cloud computing and deployment with AWS or Azure.

#### Get Started:
- **Choose a Model**: Select the model that best fits your needs from the sidebar.
- **Input Your Resume**: Upload your resume to get personalized skill suggestions.
- **Select Your Focus Area**: Choose the area you want to improve, and let the model generate a detailed roadmap for you.

**Pro Tip**: Regularly update your resume and revisit the model to keep your skills up-to-date with the latest industry trends.

""")
    
st.divider()
st.markdown("Supported by [LangChain](https://python.langchain.com/) | [Ollama](https://ollama.ai/)")

# Example button for uploading resume
st.button("📄 Upload Resume")

# Example button for generating roadmap
st.button("🛣️ Generate Roadmap")