from openai import OpenAI
client = OpenAI() 

Response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {
            "role": "user",
            "content": "Hello, how are you?"
        }
    ]
)