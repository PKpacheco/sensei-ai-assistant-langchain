from pathlib import Path
from dotenv import load_dotenv

from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_classic.chains.retrieval_qa.base import RetrievalQA
from langchain_core.prompts import PromptTemplate

from src.agents.policy_guard import requires_human_review, human_review_response
from src.agents.triage_agent import classify_email
from src.agents.skill_loader import load_skill
from src.agents.qa_agent import clean_response
from src.tools.retrieval_tool import get_retriever

# Project root folder
BASE_DIR = Path(__file__).resolve().parent.parent

# Load environment variables from the root .env file
env_path = BASE_DIR / ".env"
load_dotenv(dotenv_path=env_path)

# Local ChromaDB path
CHROMA_DIR = BASE_DIR / ".chroma_db"


def generate_smart_response(user_email: str) -> str:
    """
    Orchestrates the Sensei AI Assistant workflow.

    Flow:
    1. Classify the incoming email as technical or non-technical.
    2. Load the correct skill instructions.
    3. Retrieve relevant documentation from ChromaDB.
    4. Generate a drafted response using Ollama.
    5. Clean and validate the final output.
    """

    try:
        if requires_human_review(user_email):
            return human_review_response()
        
        # 1. Triage Agent: classify email type
        skill_name = classify_email(user_email)

        # 2. Skill Loader: load the correct behavior instructions
        skill_instructions = load_skill(skill_name)

        # 3. Embeddings model for semantic search
        embeddings = OllamaEmbeddings(
            model="nomic-embed-text"
        )

        # 4. connect to local Chroma vector database
        vectorstore = Chroma(
            persist_directory=str(CHROMA_DIR),
            embedding_function=embeddings,
        )

        # 5. Retrieval Tool
        retriever = get_retriever(
            vectorstore=vectorstore,
            k=2,
        )

        # 6. Local llm using Ollama
        llm = ChatOllama(
            model="llama3.1:8b",
            temperature=0.3,
        )

        template = """
            You are Sensei AI Assistant, a professional support assistant.

            Your goal is to draft helpful support responses using ONLY the internal documentation provided.

            Skill Instructions:
            {skill_instructions}

            Global Constraints:
            1. ONLY use information that is EXPLICITLY and LITERALLY written in the Documentation Context below.
            2. If the user's question is about a topic NOT explicitly covered in the Documentation Context, you MUST respond with ONLY this: "Thank you for reaching out. A human support agent will follow up with you shortly to assist with your request." Do NOT add any other information, explanation, or reference to documentation.
            3. NEVER say "we do not offer", "we don't have", "that is not available", or make ANY claim about what the company does or does not do unless that exact information is in the Documentation Context.
            4. If the retrieved documentation is about a different topic than the user's question, treat it as if no documentation was provided and follow constraint 2.
            5. Do not combine unrelated documentation topics to construct an answer.
            6. If the customer's name is not provided in the incoming email, start the response with exactly: "Hello,"
            7. Never use placeholders such as "[Customer's Name]", "[User]", "[Name]", or similar.
            8. Maintain a professional, empathetic, and concise tone.
            9. All responses must be in English.
            10. Sign the response as "Sensei AI - Support Team".

            Documentation Context:
            {context}

            Incoming User Email:
            {question}

            Drafted Professional Response:
            """

        prompt = PromptTemplate(
            input_variables=["context", "question"],
            partial_variables={"skill_instructions": skill_instructions},
            template=template,
        )

        qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            retriever=retriever,
            chain_type_kwargs={"prompt": prompt},
        )

        response = qa_chain.invoke({"query": user_email})
        
        final_response = response["result"]

        # 7. QA agent
        final_response = clean_response(final_response)

        return final_response

    except Exception as e:
        return f"Error processing request: {str(e)}"


if __name__ == "__main__":
    test_email = (
        "I'm having trouble with the login. "
        "Also, how do I request a refund for my last month's sub?"
    )

    print("\n[LOG] Initializing Sensei AI Assistant workflow...")
    final_answer = generate_smart_response(test_email)

    print("\n[AI OUTPUT]:\n")
    print(final_answer)