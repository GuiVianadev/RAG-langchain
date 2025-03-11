from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma


def get_retriever(persist_directory = "data/store", k=3):
    embeddings_model = OpenAIEmbeddings()

    vectordb = Chroma(persist_directory=persist_directory, embedding_function=embeddings_model)

    retriever = vectordb.as_retriever(search_kwargs={"k": k})
    return retriever

