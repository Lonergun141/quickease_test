import os
from typing import List, Tuple, Optional
from openai import OpenAI
import tiktoken
from tqdm import tqdm

with open("data/artificial_intelligence_wikipedia.txt", "r") as file:
    artificial_intelligence_wikipedia_text = file.read()
