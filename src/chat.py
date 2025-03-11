from rag import ask

user_question = input("User: ")
answer = ask(user_question)
print(f"Answer: {answer}")