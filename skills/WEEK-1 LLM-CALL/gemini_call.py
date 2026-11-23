import os
from dotenv import load_dotenv
from google import genai

# Step 1: Load environment variables from .env
load_dotenv(override=True)

# Step 2: Read API key from environment
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError(
        "GEMINI_API_KEY not found! Please open https://aistudio.google.com, "
        "create a free API key, and paste it into your .env file as GEMINI_API_KEY=your_key"
    )

# Step 3: Initialize Google GenAI client
client = genai.Client(api_key=api_key)

# Step 4: Send prompt to Gemini
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="What is Artificial Intelligence? Explain in simple words."
)

# Step 5: Display AI response
print("\nGemini LLM Response:")
print(response.text)

