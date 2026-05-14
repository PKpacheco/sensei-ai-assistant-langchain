# Sensei AI Assistant

Sensei AI Assistant is a portfolio project built to explore practical AI engineering concepts such as RAG, local LLMs, vector search, skills, tools, guardrails, and evals.

The app simulates a customer support assistant that reads an incoming email, retrieves relevant internal documentation, and drafts a professional response.

## Project Goal

The main goal of this project is learning and experimentation.

I built it to practice:

- Building a local RAG workflow     
- Using LangChain with a vector database
- Running a local LLM with Ollama
- Creating reusable AI skills
- Structuring a simple agent-inspired workflow
- Adding guardrails for sensitive requests
- Writing basic evals to test AI responses

## Tech Stack

- Python
- Streamlit
- LangChain
- ChromaDB
- Ollama
- Llama 3.1 8B
- Nomic Embed Text

## AI Concepts Included

- **RAG:** retrieves documentation before generating a response
- **Vector Search:** uses ChromaDB for semantic document search
- **Local LLM:** runs Llama 3.1 locally through Ollama
- **Skills:** stores reusable response instructions
- **Tools:** separates document retrieval into a callable tool
- **Agent-inspired workflow:** uses triage, retrieval, drafting, and QA steps
- **Guardrails:** escalates sensitive policy requests to human review
- **Evals:** tests classification and response behavior

## Architecture

```text
Incoming Email
      ↓
Policy Guard
      ↓
Triage Agent
      ↓
Skill Selection
      ↓
Retrieval Tool
      ↓
ChromaDB
      ↓
Llama 3.1 via Ollama
      ↓
QA Agent
      ↓
Draft Response
```

## Project Structure

```text
sensei-ai-assistant-langchain/
├── evals/
├── knowledge_base/
├── skills/
├── src/
│   ├── agents/
│   ├── tools/
│   ├── app.py
│   ├── chains.py
│   └── database.py
├── README.md
└── requirements.txt
```

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/sensei-ai-assistant-langchain.git
cd sensei-ai-assistant-langchain
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Start Ollama

```bash
ollama serve
```

Keep this terminal open.

### 5. Pull the required models

Open another terminal and run:

```bash
ollama pull llama3.1:8b
ollama pull nomic-embed-text
```

### 6. Build the local vector database

```bash
python src/database.py
```

### 7. Run the app

```bash
python -m streamlit run src/app.py
```

The app should open at:

```text
http://localhost:8501
```

## Running Evals

```bash
python -m evals.run_evals
```

## Notes

This project runs locally with Ollama, so no paid API key is required.

The local ChromaDB database is not included in the repository. To recreate it, run:

```bash
python src/database.py
```

## Future Improvements

- Add source citations
- Add PDF and DOCX document support
- Add confidence scoring
- Add Docker support
- Add more eval cases
- Add optional cloud model support

## License

Portfolio project for learning and experimentation.