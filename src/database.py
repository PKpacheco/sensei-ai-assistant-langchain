from pathlib import Path
from dotenv import load_dotenv

from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings


BASE_DIR = Path(__file__).resolve().parent.parent

# load env 
env_path = BASE_DIR / ".env"
load_dotenv(dotenv_path=env_path)

KNOWLEDGE_BASE_DIR = BASE_DIR / "knowledge_base"
CHROMA_DIR = BASE_DIR / ".chroma_db"


def initialize_vector_store():
    """
    Reads the knowledge_base folder and creates a local ChromaDB vector database.
    """

    print("Loading documents from knowledge_base...")

    loader = DirectoryLoader(
        str(KNOWLEDGE_BASE_DIR),
        glob="**/*.txt",
        loader_cls=TextLoader,
    )

    docs = loader.load()

    if not docs:
        raise ValueError("No documents found in knowledge_base folder.")

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=100,
    )

    splits = text_splitter.split_documents(docs)

    # Use embedding model, not the chat/generation model
    embeddings = OllamaEmbeddings(
        model="nomic-embed-text"
    )

    print("Creating vector database...")

    vectorstore = Chroma.from_documents(
        documents=splits,
        embedding=embeddings,
        persist_directory=str(CHROMA_DIR),
    )

    print(f"Database created and saved in {CHROMA_DIR}")

    return vectorstore


if __name__ == "__main__":
    initialize_vector_store()
    