import os
from dotenv import load_dotenv
from openai import OpenAI

# Step 1: Load API key from .env file
load_dotenv(override=True)

# Step 2: Read Token Harbor API key
api_key = os.getenv("TOKENHARBOR_API_KEY") or os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("API key not found! Please check your .env file.")

# Step 3: Initialize OpenAI client pointing to Token Harbor endpoint
client = OpenAI(
    api_key=api_key,
    base_url="https://tokenharbor.ai/v1"
)

# Step 4: Send prompt to AI (using Token Harbor's free model)
response = client.chat.completions.create(
    model="deepseek-v4.1-flash:free",
    messages=[
        {"role": "user", "content": "What is Artificial Intelligence? Explain in simple words."}
    ]
)

# Step 5: Display AI response
print("\nLLM Response from Token Harbor:")
print(response.choices[0].message.content)
