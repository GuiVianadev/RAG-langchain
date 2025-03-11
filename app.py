import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))
from src.rag import ask

user_question = input("Faça uma pergunta: ")
answer = ask(user_question)
print(f"Answer: {answer}")