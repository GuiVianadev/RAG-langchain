from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import PyPDFLoader


# Configuração do Text Splitter para separar o texto em pedaços (Chunks)
chunk_size = 300 #Tamanho de cada pedaço
chunk_overlap = 20 # repete 20 caracteres do chunk passado para não ter perda de contexto
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=chunk_size,
    chunk_overlap=chunk_overlap,
    separators=["\n\n", "\n", "", " "]
) # Instanciando a função Para separar o texto e configurando 


#Funçao para carregar e dividir o texto
def carregar_dividir_texto(caminho_arquivo):
    try: 
        loader = PyPDFLoader(caminho_arquivo) #Instanciando a função para fazer o carregamento do pdf
        documentos = loader.load_and_split(text_splitter) #Carregamento do pdf com a função de split de parametro
        return documentos #retorno dos documentos caso de tudo certo
    except FileNotFoundError: # Possivel erro 
        print(f'Erro: o arquivo {caminho_arquivo} não foi encontrado!')
    except Exception as e: # Possivel erro  
        print(f'Erro ao carregar o PDF: {e}')
    return None


caminho_pdf = "data/LLM.pdf" # Variavel com o caminho do pdf
chunks = carregar_dividir_texto(caminho_pdf) # variavel instanciando a função com o arquivo de parametro

#Teste para ver se o arquivo foi carregado e divido 
if chunks:
    print("Documento carregado e dividido com sucesso!")

    for i, chunk in enumerate(chunks[:5]):
        print(f"Chunk {i+1}:\n{chunk.page_content}\n{'-'*50}")
else:
    print('Falha ao carregar o PDF.')

diretorio = "data/store"
vector_store = Chroma.from_documents(
    documents=chunks,
    embedding=OpenAIEmbeddings(),
    persist_directory=diretorio
)
if vector_store is not None:
    print("Vector store foi criado com sucesso!")
else:
    print("Erro ao criar o vector store!")

