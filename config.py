# File: config.py
import os
from utils import load_environment_variables

GROQ_API_KEY = None
try:
    GROQ_API_KEY = load_environment_variables()
except ValueError as e:
    print(f"Error loading API key: {e}")

# ✅ RECOMMENDED: Update to a valid and supported model
GROQ_MODEL_NAME = "llama3-70b-8192"  # You can also use "gemma-7b-it" or "llama3-8b-8192"
GROQ_TEMPERATURE = 0.5
