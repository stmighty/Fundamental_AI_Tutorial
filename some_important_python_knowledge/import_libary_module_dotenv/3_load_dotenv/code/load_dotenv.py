import cohere
import os
from dotenv import load_dotenv
from pathlib import Path

dotenv_path = Path('../.env')
config = load_dotenv(dotenv_path=dotenv_path)

print("type of os.environ is", type(os.environ))
print(os.environ)
print()


COHERE_API_KEY = os.environ.get("COHERE_API_KEY")
print(COHERE_API_KEY)