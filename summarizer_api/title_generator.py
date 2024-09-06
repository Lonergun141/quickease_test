from openai import OpenAI
from dotenv import load_dotenv
import os
import json

load_dotenv()

client = OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))

def generate_title(paragraph: str):
    prompt = (
        f"You are a title generator. Generate a title for the following paragraph. "
        f"Make sure the title is short and descriptive. "
        f"Remove quotes from the title"
    )

    response = client.chat.completions.create(
        model='gpt-4o-mini',
        messages=[
            {"role": "system", "content": prompt },
            {"role": "user", "content": paragraph},
        ],
        max_tokens=20,  
        temperature=0.7,
    )
    
    title = response.choices[0].message.content
    

    return title