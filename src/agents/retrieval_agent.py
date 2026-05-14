from pathlib import Path
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma


BASE_DIR = Path(__file__).resolve().parent.parent.parent
CHROMA_DIR = BASE_DIR / ".chroma_db"


def get_vectorstore():
    """Connects to the local ChromaDB vector store with Ollama"""

    embeddings = OllamaEmbeddings(model="nomic-embed-text")

    return Chroma(
        persist_directory=str(CHROMA_DIR),
        embedding_function=embeddings,
    )


def retrieve_context(user_email: str, k: int = 2) -> list:
    """
    Retrieves the most relevant documentation chunks related to the email.

    Args:
        user_email: The incoming customer email text.
        k: Number of top results to retrieve.

    Returns:
        A list of relevant Document objects from the knowledge base.
    """

    vectorstore = get_vectorstore()
    retriever = vectorstore.as_retriever(search_kwargs={"k": k})

    return retriever.invoke(user_email)
