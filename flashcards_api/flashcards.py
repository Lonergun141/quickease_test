from openai import OpenAI
from dotenv import load_dotenv
import os
import json

load_dotenv()

client = OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))

def generate_flashcards(paragraph):
    prompt = (
        f"Convert the following paragraph into at least 10 flashcards. "
        f"Generate flashcards with the following structure: Each flashcard should have a 'Term' on the front and a 'Definition' on the back."
        f"Format should be in JSON format: Id:# Front: Term \n Back: Definition"
        f"Only JSON data is required. No other decoraters are needed."
        f"The terms should be related to [specific subject or topic]. Provide concise and accurate definitions for each term."
    )

    response = client.chat.completions.create(
        model='gpt-4o-mini',
        messages=[
            {"role": "system", "content": prompt },
            {"role": "user", "content": paragraph},
        ],
        max_tokens=500,  
        temperature=0.7,
    )
    
    flashcards_text = response.choices[0].message.content

    return flashcards_text