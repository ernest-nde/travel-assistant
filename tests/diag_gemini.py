import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load explicitly to be sure
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
print(f"API Key begins with: {api_key[:4] if api_key else 'None'}... (length: {len(api_key) if api_key else 0})")

try:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")
    print("Sending test prompt...")
    response = model.generate_content("Hello")
    print("Success! Response:")
    print(response.text)
except Exception as e:
    import traceback
    print("ERROR OCCURRED:")
    traceback.print_exc()
