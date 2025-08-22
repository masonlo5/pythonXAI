import openai 
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
history = [
            {"role": "system", "content": "please use chinese to respond"},]
while True:
    user_input = input("You: ")
    if user_input == "exit":
        break
    history.append({"role": "user", "content": user_input})
    response = openai.chat.completions.create(
        model="gpt-5",
        messages=history,
    )

    assistant_message = response.choices[0].message.content
    history.append({"role": "assistant", "content": assistant_message})
    print(f"AI: {assistant_message}")