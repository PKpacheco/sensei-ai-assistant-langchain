from pathlib import Path
from dotenv import load_dotenv

from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_classic.chains.retrieval_qa.base import RetrievalQA
from langchain_core.prompts import PromptTemplate

env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)


def generate_smart_response(user_email: str) -> str:
    embeddings = OllamaEmbeddings(model="llama3.1:8b")

    vectorstore = Chroma(
        persist_directory="./.chroma_db",
        embedding_function=embeddings,
    )

    llm = ChatOllama(
        model="llama3.1:8b",
        temperature=0.3,
    )

    template = """
You are Sensei AI Assistant, a professional support assistant.
Your goal is to draft helpful support responses using ONLY the internal documentation provided.

Constraints:
1. If the documentation does not contain the answer, politely say that a human agent will follow up.
2. Do not invent policies, deadlines, fees, penalties, or procedures.
3. If the customer's name is not provided in the incoming email, start the response with exactly: "Hello,"
4. Never use placeholders such as "[Customer's Name]", "[User]", "[Name]", or similar.
5. Maintain a professional, empathetic, and concise tone.
6. All responses must be in English.
7. Sign the response as "Sensei AI - Support Team".

Documentation Context:
{context}

Incoming User Email:
{question}

Drafted Professional Response:
"""

    prompt = PromptTemplate(
        input_variables=["context", "question"],
        template=template,
    )

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vectorstore.as_retriever(search_kwargs={"k": 2}),
        chain_type_kwargs={"prompt": prompt},
    )

    try:
        response = qa_chain.invoke({"query": user_email})
        return response["result"]
    except Exception as e:
        return f"Error processing request: {str(e)}"


if __name__ == "__main__":
    test_email = (
        "I'm having trouble with the login. "
        "Also, how do I request a refund for my last month's sub?"
    )

    print("\n[LOG] Initializing AI retrieval and inference...")
    final_answer = generate_smart_response(test_email)

    print("\n[AI OUTPUT]:\n")
    print(final_answer)
