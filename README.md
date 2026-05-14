# Sensei AI Assistant

Sensei AI Assistant is a local RAG-powered customer support assistant that retrieves internal documentation and generates professional draft responses for incoming customer emails.

The project was built as a portfolio application to demonstrate practical AI integration using LangChain, ChromaDB, Ollama, and Streamlit.

## AI Concepts Demonstrated

This project demonstrates several practical AI engineering concepts:

- **RAG:** Retrieves relevant internal documentation before generating a response.
- **Vector Search:** Uses ChromaDB to perform semantic search over support documents.
- **Local LLMs:** Runs Llama 3.1 locally through Ollama.
- **Skills:** Uses reusable instruction files to define response behavior and constraints.
- **Tools:** Encapsulates document retrieval as a callable tool.
- **Subagent-inspired workflow:** Separates the workflow into triage, drafting, and QA validation steps.
- **Evals:** Includes test cases to validate response quality and reduce hallucinations.

## Features

- Generates professional customer support draft replies
- Uses Retrieval-Augmented Generation (RAG)
- Retrieves relevant information from internal documentation
- Runs locally with Ollama
- Uses ChromaDB as a local vector database
- Simple Streamlit web interface
- Avoids relying only on the LLM's general knowledge
- Designed to reduce hallucinations by grounding responses in documentation

## Tech Stack

- Python
- Streamlit
- LangChain
- ChromaDB
- Ollama
- Llama 3.1 8B
- Nomic Embed Text
- dotenv

## Architecture

```text
Customer Email
      ↓
Streamlit UI
      ↓
LangChain Retrieval Chain
      ↓
ChromaDB Vector Store
      ↓
Relevant Documentation Chunks
      ↓
Ollama / Llama 3.1
      ↓
Generated Support Response
```

## How to Run the Project

Follow the steps below to run **Sensei AI Assistant** locally.

### Prerequisites

Before running the project, make sure you have installed:

- Python 3.10+
- Git
- Ollama

---

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/sensei-ai-assistant-langchain.git
cd sensei-ai-assistant-langchain
```

---

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the virtual environment:

#### macOS 

```bash
source venv/bin/activate
```

---

### 3. Install Python Dependencies

```bash
python -m pip install -r requirements.txt
```

---

### 4. Start Ollama

Open a terminal and run:

```bash
ollama serve
```

Keep this terminal open while using the application.

---

### 5. Download the Required Ollama Model

Open a second terminal and run:

```bash
ollama pull llama3.1:8b
```

---

### 6. Generate the Local Vector Database

From the project root folder, run:

```bash
python src/database.py
```

This step reads the files from the `knowledge_base` folder, converts them into embeddings, and stores them locally in ChromaDB.

If you change the embedding model or update the knowledge base, delete the old database and run the ingestion script again:


---

### 7. Run the Streamlit App

Start the application with:

```bash
python -m streamlit run src/app.py
```

Streamlit will open the app in your browser.

If it does not open automatically, go to:

```text
http://localhost:8501
```
