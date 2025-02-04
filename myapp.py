import streamlit as st
import PyPDF2
import json
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import (
    SystemMessagePromptTemplate, HumanMessagePromptTemplate, ChatPromptTemplate
)

# Blue Theme
st.markdown("""
    <style>
        .main { background-color: #15202B; color: #ffffff; }
        .sidebar .sidebar-content { background-color: #192734; color: #ffffff; }
        .stTextInput textarea, .stSelectbox div[data-baseweb="select"], div[role="listbox"] div {
            background-color: #1E2A38 !important; color: white !important; border-radius: 8px;
            transition: all 0.3s ease-in-out; padding: 8px;
        }
        .stTextInput textarea:hover, .stSelectbox div[data-baseweb="select"]:hover, div[role="listbox"] div:hover {
            background-color: #1DA1F2 !important; color: black !important;
        }
        .stButton button {
            background-color: #1DA1F2 !important; color: white !important; border-radius: 25px;
            font-weight: bold; padding: 12px 24px; transition: 0.3s ease-in-out, transform 0.2s;
        }
        .stButton button:hover { background-color: #0D8DDC !important; transform: scale(1.07); }
        h1, h2, h3, h4, h5, h6, a { color: #1DA1F2 !important; transition: color 0.3s ease-in-out; }
        h1:hover, h2:hover, h3:hover, h4:hover, h5:hover, h6:hover, a:hover { color: #ffffff !important; }
        .stDivider { border-bottom: 2px solid #1DA1F2 !important; margin-bottom: 10px; }
    </style>
""", unsafe_allow_html=True)

st.title("🤝 Trusted Ally")
st.caption("Your AI-Powered Career & Workplace Coach")

# 🎯 Sidebar with user-friendly guidance
with st.sidebar:
    st.markdown("""
        ## 🚀 I am your Career & Workplace Companion
        - 💡 Helps You Navigate Success
        - 🎯 Personalized Learning Paths
        - 🏢 Guidance for Workplace Challenges
    """)
    selected_model = st.selectbox("⚙️ Choose AI Model", [
        "deepseek-r1:1.5b", "deepseek-r1:8b", "deepseek-r1:14b", "deepseek-r1:32b", "deepseek-r1:70b", "deepseek-r1:671b"
    ], index=0)


# 📂 Resume Upload Section
uploaded_file = st.file_uploader("📥 Upload Your Resume (PDF)", type=["pdf"])
st.session_state.resume_text = ""
if uploaded_file:
    with st.spinner("📄 Extracting resume content..."):
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        for page in pdf_reader.pages:
            st.session_state.resume_text += page.extract_text()


# AI Engine Setup
llm_engine = ChatOllama(model=selected_model, base_url="http://localhost:11434", temperature=0.4)

system_prompt = SystemMessagePromptTemplate.from_template(
    """
    You are a highly skilled AI Career & Workplace Coach. 
    Analyze users' resumes, career aspirations, and workplace concerns to provide actionable advice. 
    Guide users on skill development, strategic career moves, and professional growth. 
    Offer solutions for workplace challenges. Always respond in English unless requested otherwise.
    """
)

def generate_ai_response(prompt_chain):
    processing_pipeline = prompt_chain | llm_engine | StrOutputParser()
    return processing_pipeline.invoke({})

def build_prompt_chain(user_query=""):
    prompt_sequence = [system_prompt]
    if st.session_state.resume_text:
        prompt_sequence.append(HumanMessagePromptTemplate.from_template(f"Here is my resume:\n{st.session_state.resume_text}"))
    if user_query:
        prompt_sequence.append(HumanMessagePromptTemplate.from_template(user_query))
    else:
        prompt_sequence.append(HumanMessagePromptTemplate.from_template("I want career guidance and help with workplace situations."))
    return ChatPromptTemplate.from_messages(prompt_sequence)

# 🚀 Career & Workplace Guidance Button
if st.button("💡 Get Insights & Strategies"):
    if not st.session_state.resume_text:
        st.warning("⚠️ Please upload a resume for more personalized insights!")
    else:
        with st.spinner("🔍 Analyzing & Generating Your Career Roadmap..."):
            prompt_chain = build_prompt_chain()
            roadmap = generate_ai_response(prompt_chain)
            roadmap_file = "career_guidance.txt"
            with open(roadmap_file, "w") as file:
                file.write(roadmap)
            st.success("✅ Career insights generated successfully!")
            st.download_button("📥 Download Insights", data=roadmap, file_name=roadmap_file, mime="text/plain")

# 💬 AI Chat Section
if "message_log" not in st.session_state:
    st.session_state.message_log = [{"role": "ai", "content": "Hello! I'm your personal Career & Workplace Coach. How can I assist you today? 😊"}]

chat_container = st.container()
with chat_container:
    for message in st.session_state.message_log:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

user_query = st.chat_input("Type your question here... ✍️")
if user_query:
    st.session_state.message_log.append({"role": "user", "content": user_query})
    with st.spinner("🤖 Thinking..."):
        prompt_chain = build_prompt_chain(user_query)
        ai_response = generate_ai_response(prompt_chain)
    st.session_state.message_log.append({"role": "ai", "content": ai_response})
    st.rerun()
