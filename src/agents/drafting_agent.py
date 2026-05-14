from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate


TEMPLATE = """
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


def get_drafting_prompt(skill_instructions: str) -> PromptTemplate:
    """
    Builds the drafting prompt with skill instructions injected.

    Args:
        skill_instructions: The loaded skill markdown content.

    Returns:
        A PromptTemplate ready for use with RetrievalQA.
    """

    return PromptTemplate(
        input_variables=["context", "question"],
        partial_variables={"skill_instructions": skill_instructions},
        template=TEMPLATE,
    )


def get_llm(model: str = "llama3.1:8b", temperature: float = 0.3) -> ChatOllama:
    """
    Initializes the local Ollama LLM for response generation.

    args:
        model:  Ollama model name to use.
        temperature: controls randomness (lower = more deterministic)

    Returns:
        A ChatOllama instance.
    """

    return ChatOllama(
        model=model,
        temperature=temperature,
    )
