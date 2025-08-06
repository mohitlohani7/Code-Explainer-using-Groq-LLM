# app.py
import streamlit as st
import os
from dotenv import load_dotenv
from llm_service import get_code_explainer_chain

# Load environment variables
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Set Streamlit app config
st.set_page_config(page_title="Code Explainer", layout="centered")

st.title("🤖 Code Explainer using Groq LLM")
st.markdown("Enter your code and get a plain-language explanation powered by a Groq LLM.")

# Input: Programming language
language = st.selectbox("👨‍💻 Select Programming Language", ["Python", "JavaScript", "C++", "Java", "Other"])

# Input: Code snippet
code = st.text_area("🧾 Paste your code here", height=300, placeholder="e.g., print('Hello India')")

# Button: Trigger explanation
if st.button("🔍 Explain Code"):
    if not GROQ_API_KEY:
        st.error("❌ GROQ_API_KEY not found. Please set it in a .env file or environment variable.")
    elif not code.strip():
        st.warning("⚠️ Please paste some code first.")
    else:
        try:
            st.info("🤔 Thinking...")
            explainer_chain = get_code_explainer_chain(api_key=GROQ_API_KEY)
            result = explainer_chain.invoke({"language": language, "code": code})
            st.success("✅ Here's the explanation:")
            st.markdown(f"```\n{result}\n```")
        except Exception as e:
            st.error(f"🚨 Error: {e}")
