import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    base_url="https://models.inference.ai.azure.com",
    api_key=os.environ["GITHUB_TOKEN"],
)

response = client.chat.completions.create(
    model=os.environ["MODEL_NAME"],
    messages=[
        {
            "role": "system",
            "content": "You are a learning path curator for enterprise certifications."
        },
        {
            "role": "user",
            "content": "I am a Cloud Engineer. What certification should I study for first?"
        }
    ]
)

print(response.choices[0].message.content)