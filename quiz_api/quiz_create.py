from openai import OpenAI
from dotenv import load_dotenv
import os
import json

load_dotenv()

client = OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))

def generate_questions(paragraph):
    prompt = (
        f"Convert the following paragraph into at least 2 questions, each question should have six choices and only unique one asnwer."
        f'''Generate the questions and choices with the following structure:
        "Question":"Question description", 
        "choice1":"Choice description", 
        "choice2":"Choice description", 
        "choice3":"Choice description", 
        "choice4":"Choice description", 
        "choice5":"Choice description", 
        "choice6":"Choice description",
        "Answer":"Choice description"
        '''  
        f"The format must only be in JSON format."
        f"Only JSON data is required. No other decoraters like ``` are needed."
    )

    response = client.chat.completions.create(
        model='gpt-4o-mini',
        messages=[
            {"role": "system", "content": prompt },
            {"role": "user", "content": paragraph},
        ],
        max_tokens=1500, 
        temperature=0.7,
    )
    
    flashcards_text = response.choices[0].message.content

    return flashcards_text

para = '''Ecology is the study of organisms and how they interact with the environment around them. An ecologist studies the relationship between living things and their habitats. In order to learn about the natural world, ecologists must study multiple aspects of life ranging from the moss that grows on rocks to the wolf population in the United States' Yellowstone National Park. In order to research the environment, scientists ask questions, such as: How do organisms interact with the living and nonliving factors around them? What do organisms need to survive and thrive in their current environments? To find the answers to these questions, ecologists must study and observe all forms of life and their ecosystems throughout our world.
In addition to examining how ecosystems function, ecologists study what happens when ecosystems do not function normally. Changes in ecosystems can result from many different factors including diseases among the organisms living in the area, increases in temperature, and increased human activities. Understanding these changes can help ecologists anticipate future ecological challenges and inform other scientists and policymakers about the challenges facing their local ecosystems.
Ecology first began gaining popularity in the 1960s, when environmental issues were rising to the forefront of public awareness. Although scientists have been studying the natural world for centuries, ecology in the modern sense has only been around since the 19th century. Around this time, European and American scientists began studying how plants functioned and their effects on the habitats around them. Eventually, this led to the study of how animals interact with plants, other animals, and shaped the ecosystems in which they lived. Today, modern ecologists build on the data collected by their predecessors and continue to pass on information about the ecosystems around the world. The information they gather continues to affect the future of our planet.
Human activity plays an important role in the health of ecosystems all around the world. Pollution emitted from fossil fuels or factories can contaminate the food supply for a species, potentially changing an entire food web. Introducing a new species from another part of the world into an unfamiliar environment can have unintended and negative impacts on local lifeforms. These kinds of organisms are called invasive species. Invasive species can be any form of living organism that is brought by humans to a new part of the world where they have no natural predators. The addition or subtraction of a single species from an ecosystem can create a domino effect on many others, whether that be from the spread of disease or overhunting.'''

print(generate_questions(para))
