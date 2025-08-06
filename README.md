# Code-Explainer-using-Groq-LLM
Groq-Powered Code Explainer
This project is a real-time code explanation tool built with LangChain and powered by Groq's high-speed AI inference. It quickly helps users understand code snippets across various programming languages.

✨ Features
Instant Explanations: Get quick, concise code summaries.

Multi-Language Support: Explains code from diverse programming languages.

Groq-Accelerated: Leverages Groq's LPUs for ultra-low latency responses.

Modular Design: Organized for clear structure and easy maintenance.

Secure API Keys: Manages credentials safely using .env files.

💡 Real-world Use Cases
This tool is valuable in development and learning:

Developer Onboarding: Helps new team members quickly understand existing codebases.

Code Review & Debugging: Speeds up logic comprehension during reviews and troubleshooting.

Learning & Prototyping: Aids in efficiently grasping new concepts and experimenting with code.

Automated Documentation: Provides initial summaries for faster documentation creation.

🚀 Getting Started
Follow these steps to set up and run the project locally.

Installation
Clone the repository:

git clone https://github.com/your-username/groq_code_explainer.git
cd groq_code_explainer

Create & Activate Virtual Environment:

python -m venv venv
# Windows: .\venv\Scripts\activate
# macOS / Linux: source venv/bin/activate

Install Dependencies:
Create requirements.txt:

langchain-groq
langchain-core
python-dotenv

Then run: pip install -r requirements.txt

Set Up Groq API Key:

Get your API key from the Groq Console.

Create a .env file in your project root.

Add your key: GROQ_API_KEY=gsk_YOUR_ACTUAL_GROQ_API_KEY_HERE

Important: Add .env to your .gitignore file.

🏃 Usage
Run the application:

python main.py

Follow prompts: Enter language (e.g., Python), paste code, and press Enter on a blank line to finish input.

🌐 Local Hosting (Example)
This is a command-line tool. You can access the local network address here: 👉 http://192.168.1.15:8501. Please note, this project does not directly expose a web interface.

🤝 Contributing
Contributions are welcome! Open an issue or submit a pull request for improvements.

📄 License
This project is created and licensed by Mr. Mohit Lohani. 
