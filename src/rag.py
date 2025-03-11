from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain.schema.runnable import RunnablePassthrough
from langchain.schema.output_parser import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableMap
from retriever import get_retriever

# Inicializa o LLM com o modelo "chat-3.5-turbo"
llm = ChatOpenAI(model="gpt-3.5-turbo")

# Obtém o retriever
retriever = get_retriever()

# Template do prompt para a resposta final
prompt = PromptTemplate.from_template(
    """Use o seguinte contexto para responder a pergunta do usuário.  
Se não souber a resposta, diga que não sabe.  

### CONTEXTO:  
{context}  

### PERGUNTA:  
{question}  

### RESPOSTA:"""
)
qa_chain = (
    RunnableMap({
        "context": retriever | RunnablePassthrough(),  # Obtém os documentos relevantes
        "question": RunnablePassthrough()  # Passa a pergunta diretamente
    })
    | prompt
    | llm
    | StrOutputParser()  # Converte a saída para string legível
)

def ask(question):
    return qa_chain.invoke(question)

# Pergunta do usuário
user_question = input("User: ")
answer = ask(user_question)
print(f"Answer: {answer}")