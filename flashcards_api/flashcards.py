from openai import OpenAI
from dotenv import load_dotenv
import os
import json

load_dotenv()

client = OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))

def generate_flashcards(paragraph):
    prompt = (
        f"Convert the following paragraph into at least 10 only 10 flashcards no need to go beyond. "
        f"Generate flashcards with the following structure: Each flashcard should have a 'Term' on the front and a 'Definition' on the back."
        f"Format should be in JSON format: Id:# Front: Term \n Back: Definition"
        f"Only JSON data is required. No other decoraters like ``` are needed."
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

    # Remove any leading/trailing whitespace and code block markers
    flashcards_text = flashcards_text.strip()
    if flashcards_text.startswith("```") and flashcards_text.endswith("```"):
        flashcards_text = flashcards_text[3:-3]
    
    # Remove any remaining "json" or other language specifiers
    flashcards_text = flashcards_text.lstrip("json").strip()

    # Parse the JSON
    try:
        flashcards = json.loads(flashcards_text)
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        print(f"Received content: {flashcards_text}")
        return None

    return flashcards