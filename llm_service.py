# llm_service.py

from groq import Groq

def get_code_explainer_chain(api_key):
    if not api_key:
        raise ValueError("GROQ API key is missing!")

    client = Groq(api_key=api_key)

    class ExplainerChain:
        def invoke(self, inputs):
            prompt = f"Explain the following {inputs['language']} code:\n\n{inputs['code']}"
            response = client.chat.completions.create(
                model="llama3-70b-8192",  # ✅ Use currently supported model
                messages=[{"role": "user", "content": prompt}]
            )
            return response.choices[0].message.content.strip()

    return ExplainerChain()
