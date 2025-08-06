# File: main.py
import sys
from llm_service import get_code_explainer_chain

def get_user_input():
    """Prompts the user for the programming language and code snippet."""
    print("--- Code Explainer Service ---")
    
    language = input("Kaunsi language hai (jaise: Python, JS)?: ")
    if not language:
        print("Bhai, language toh bata. Chal, ab jaa.")
        sys.exit(1)
        
    print("\nAb code daal (Press Enter on an empty line to finish):")
    
    code_lines = []
    while True:
        line = input()
        if not line:
            break
        code_lines.append(line)
        
    code = "\n".join(code_lines).strip()
    if not code:
        print("Code kahaan hai bhai? Chal nikal.")
        sys.exit(1)
        
    return language, code

def main():
    """Main function to run the application."""
    language, code = get_user_input()
    
    try:
        print("\nSoch raha hoon...\n")
        
        explainer_chain = get_code_explainer_chain()
        if explainer_chain is None:
            sys.exit(1)
        
        result = explainer_chain.invoke({"language": language, "code": code})
        
        print("--- Explanation ---")
        print(result)
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Kuch gadbad ho gayi: {e}")

if __name__ == "__main__":
    main()