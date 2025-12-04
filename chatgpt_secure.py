# Chatgpt_secure.py 
# This is a simple console chat to test the API key outside Streamlit

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

messages = [{"role": "system", "content": "You are a helpful assistant."}]
print("Secure Console Chat (type 'quit' to exit)")

while True:
    user_input = input("You: ").strip()
    if user_input.lower() == "quit":
        print("Goodbye!")
        break

    messages.append({"role": "user", "content": user_input})
    response = client.chat.completions.create(model="gpt-4o", messages=messages)
    reply = response.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})
    print(f"AI: {reply}\n")
