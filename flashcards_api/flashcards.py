from openai import OpenAI
from dotenv import load_dotenv
import os


load_dotenv()

client = OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))

def generate_flashcards(paragraph):
    prompt = (
        f"Convert the following paragraph into at least 10 flashcards. "
        f"Generate flashcards with the following structure: Each flashcard should have a 'Term' on the front and a 'Definition' on the back."
        f"Format should be: Front: Term \n Back: Definition"
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
    flashcards_strip = flashcards_text.strip()
    flashcards = flashcards_strip.split('\n')
    print(flashcards_text)
    print("\n\n\n")
    print(flashcards_strip)
    print("\n\n\n")
    print(flashcards)
    
    flashcard_list = []

    for flashcard in flashcards:
        if ',' in flashcard:
            frontCardText, backCardText = flashcard.split(',', 1)
            flashcard_list.append({
                "frontCardText": frontCardText.strip(),
                "backCardText": backCardText.strip()
            })

    return flashcard_list

paragraph = "The CPU, or Central Processing Unit, is the main processor of a computer, responsible for carrying out instructions and processing data. It interacts with other hardware components like memory and storage to perform tasks. The CPU is often called the 'brain' of the computer."

flashcards = generate_flashcards(paragraph)
#print(flashcards)

# Print the generated flashcards
#for i, flashcard in enumerate(flashcards, 1):
#   print(f"Flashcard {i}: Front: {flashcard['frontCardText']}, Back: {flashcard['backCardText']}")
