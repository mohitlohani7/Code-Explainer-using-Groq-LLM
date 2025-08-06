import os
from dotenv import load_dotenv

def load_environment_variables():
    load_dotenv()
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY not found. Please set it in your .env file.")
    return api_key