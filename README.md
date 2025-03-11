# RAG com LangChain

Este projeto implementa um sistema de Recuperação Aumentada por Geração (RAG) utilizando **LangChain**, **ChromaDB** e **OpenAI**. O objetivo é carregar documentos em PDF, dividir o texto em chunks, armazená-los em um banco vetorial e permitir consultas inteligentes baseadas nesses dados.

## 🛠️ Tecnologias Utilizadas
- Python 3.10+
- LangChain
- ChromaDB
- OpenAI API
- PyPDFLoader

## 🔧 Instalação
1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/rag-langchain.git
   cd rag-langchain
   ```

2. Crie e ative um ambiente virtual:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Mac/Linux
   .venv\Scripts\activate  # Windows
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## 🔄 Estrutura do Projeto
```
rag-langchain/
│── app.py                   # Ponto de entrada principal
│── requirements.txt         # Dependências do projeto
│── README.md                # Documentação
│── data/                    # Diretório para PDFs
│── files/                   # Diretório para armazenar embeddings
├── src/
│   ├── rag.py               # Lógica de consulta ao banco vetorial
│   ├── retriever.py         # Configuração do mecanismo de busca
│   ├── vector_store.py      # Criação e persistência da base vetorial
│   ├── document_loader.py   # Carregamento e divisão dos documentos
│   ├── chat.py              # Interface para perguntas e respostas
```

## Como Usar
1. Adicione seus documentos PDF na pasta `data/`.
2. Execute o script para carregar e indexar os documentos:
   ```bash
   python src/vector_store.py
   ```
3. Inicie o chatbot e envie perguntas:
   ```bash
   python app.py
   ```

## Configuração da API OpenAI
Crie um arquivo `.env` na raiz do projeto e adicione sua chave da OpenAI:
```
OPENAI_API_KEY=your_api_key_here
```

## Funcionalidades Implementadas
- Carregamento de documentos PDF
- Divisão inteligente do texto em chunks
- Armazenamento dos embeddings no ChromaDB
- Recuperação otimizada de informações
- Interface simples para perguntas e respostas




