import streamlit as st
import PyPDF2
import json
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import (
    SystemMessagePromptTemplate, HumanMessagePromptTemplate, AIMessagePromptTemplate, ChatPromptTemplate
)

# Custom CSS for Spotify-inspired theme
import streamlit as st

st.markdown("""
    <style>
        /* Background and text color for the main content */
        .main { 
            background-color: #121212; 
            color: #ffffff; 
        }

        /* Sidebar styling */
        .sidebar .sidebar-content { 
            background-color: #181818; 
            color: #ffffff; 
        }

        /* Input Fields (Text & Selectbox) */
        .stTextInput textarea, 
        .stSelectbox div[data-baseweb="select"], 
        div[role="listbox"] div { 
            background-color: #282828 !important; 
            color: white !important; 
            border-radius: 5px; 
            transition: all 0.3s ease-in-out;
        }
        
        /* Input Field Hover Effect */
        .stTextInput textarea:hover, 
        .stSelectbox div[data-baseweb="select"]:hover, 
        div[role="listbox"] div:hover { 
            background-color: #1DB954 !important; 
            color: black !important; 
        }

        /* Styled Buttons */
        .stButton button { 
            background-color: #1DB954 !important; 
            color: white !important; 
            border-radius: 20px; 
            font-weight: bold; 
            padding: 10px 20px; 
            transition: background-color 0.3s ease-in-out, transform 0.2s;
        }

        /* Button Hover & Click Effects */
        .stButton button:hover { 
            background-color: #17a34a !important; 
            transform: scale(1.05);
        }

        .stButton button:active { 
            transform: scale(0.95);
        }

        /* Headers & Links */
        h1, h2, h3, h4, h5, h6, a { 
            color: #1DB954 !important; 
            transition: color 0.3s ease-in-out; 
        }

        h1:hover, h2:hover, h3:hover, h4:hover, h5:hover, h6:hover, a:hover {
            color: #ffffff !important;
        }

        /* Divider Styling */
        .stDivider { 
            border-bottom: 2px solid #1DB954 !important; 
            margin-bottom: 10px; 
        }

        /* Sidebar Active Link Highlight */
        .sidebar .sidebar-content .stSelectbox div[data-baseweb="select"]:focus {
            background-color: #1DB954 !important;
            color: black !important;
        }

    </style>
""", unsafe_allow_html=True)


st.title("Trusted Ally")
st.caption("Professional Coach")

# Sidebar configuration
with st.sidebar:
    st.markdown("""## I am your Career Companion.
- Helps You Navigate Success
- Share Personalized Learning Path
- Guide to Tackle Situations at Workplace""")
    selected_model = st.selectbox("Large Language Model", ["deepseek-r1:1.5b", "deepseek-r1:8b", "deepseek-r1:14b", "deepseek-r1:32b", "deepseek-r1:70b", "deepseek-r1:671b"], index=0)
    
    st.markdown(""" your personalized AI-powered assistant to help you stay ahead at work. Whether you're looking to *learn new skills* or *deepen your expertise* in your current field, I can help you!""")
target_role = st.text_input("Target Role / Position", "Software Engineer")



uploaded_file = st.file_uploader("📥 Upload Resume (PDF)", type=["pdf"])
st.session_state.resume_text = ""
if uploaded_file:
    with st.spinner("Extracting resume content..."):
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        for page in pdf_reader.pages:
            st.session_state.resume_text += page.extract_text()

st.divider()
<<<<<<< HEAD
st.write("Tip 🛠️ : Update your resume to get more insightful results")

llm_engine = ChatOllama(model=selected_model, base_url="http://localhost:11434", temperature=0.4)

system_prompt = SystemMessagePromptTemplate.from_template(
    """
    You are an expert AI Career Coach. Analyze the skills and experiences of users based on their resume, 
    industry, and target role, and generate a strategic roadmap for their professional growth.
    Suggest technical and relevant skills to succeed. Avoid recommending behavioral skills unless asked.
    If requested, provide professional strategies for excelling at work. Always respond in English unless asked otherwise.
    """
)

def generate_ai_response(prompt_chain):
    processing_pipeline = prompt_chain | llm_engine | StrOutputParser()
    return processing_pipeline.invoke({})

def build_prompt_chain():
    prompt_sequence = [system_prompt]
    if st.session_state.resume_text:
        prompt_sequence.append(HumanMessagePromptTemplate.from_template(f"Here is my resume:\n{st.session_state.resume_text}"))
    prompt_sequence.append(HumanMessagePromptTemplate.from_template(f"I want a roadmap to become a {target_role}."))
    return ChatPromptTemplate.from_messages(prompt_sequence)

if st.button("💡 Generate Analysis"):
    if not st.session_state.resume_text:
        st.warning("Please upload a resume first.")
    else:
        with st.spinner("🧠 Generating career roadmap..."):
            prompt_chain = build_prompt_chain()
            roadmap = generate_ai_response(prompt_chain)
            roadmap_file = "career_roadmap.txt"
            with open(roadmap_file, "w") as file:
                file.write(roadmap)
            st.success("Career roadmap generated successfully!")
            st.download_button("📥 Download Roadmap", data=roadmap, file_name=roadmap_file, mime="text/plain")

# Chat section
if "message_log" not in st.session_state:
    st.session_state.message_log = [{"role": "ai", "content": "Hi! I'm your personal Career Guru. How can I help you today?"}]

chat_container = st.container()
with chat_container:
    for message in st.session_state.message_log:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

user_query = st.chat_input("Type your question here...")
if user_query:
    st.session_state.message_log.append({"role": "user", "content": user_query})
    with st.spinner("🧠 Thinking..."):
        prompt_chain = build_prompt_chain()
        ai_response = generate_ai_response(prompt_chain)
    st.session_state.message_log.append({"role": "ai", "content": ai_response})
    st.rerun()
=======
"Tip 🛠️ : Update your resume to get more insightful results"


llm_engine=ChatOllama(
    model=selected_model,
    base_url="",
    temperature=0.3

)
>>>>>>> 337d63b6559b2a210b4f2f9533616835ef91daf8
