import cohere
import os
from dotenv import load_dotenv
from pathlib import Path

dotenv_path = Path('../.env')
load_dotenv(dotenv_path=dotenv_path)               # this line is used to connect then you can use os.environ

print("type of os.environ is", type(os.environ))
print(os.environ)
print()


COHERE_API_KEY = os.environ.get("COHERE_API_KEY")
print(COHERE_API_KEY)