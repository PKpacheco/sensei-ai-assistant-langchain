def get_retriever(vectorstore, k: int = 2):
    """
    Retrieval tool that searches the local ChromaDB knowledge base.
    """
    return vectorstore.as_retriever(search_kwargs={"k": k})