from pathlib import Path
from dotenv import load_dotenv
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings

env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)


def initialize_vector_store():
    """Reads the knowledge_base folder and creates a local vector database."""

    print("Loading documents from knowledge_base...")
    loader = DirectoryLoader("./knowledge_base", glob="./*.txt", loader_cls=TextLoader)
    docs = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    splits = text_splitter.split_documents(docs)

    embeddings = OllamaEmbeddings(model="llama3.1:8b")

    print("Creating vector database...")
    vectorstore = Chroma.from_documents(
        documents=splits,
        embedding=embeddings,
        persist_directory="./.chroma_db",
    )

    print("Database created and saved in .chroma_db/")
    return vectorstore


if __name__ == "__main__":
    initialize_vector_store()
