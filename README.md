# Sensei AI Assistant

Sensei AI Assistant is a functional portfolio prototype that explores practical AI engineering concepts through a simulated customer-support workflow.

The application receives an inbound customer email, classifies the request, retrieves relevant internal documentation, applies reusable response instructions, and generates a professional draft for human review.

> **Project scope:** This project was created for hands-on learning and experimentation. It runs locally using simulated customer-support emails and a small demonstration knowledge base. It has not been deployed or used in a production customer-support environment.

## Overview

The project demonstrates how an AI-assisted internal tool can combine:

* Request triage
* Retrieval-augmented generation
* Semantic document search
* Reusable response skills
* Policy guardrails
* Human-review workflows
* Lightweight evaluations

The goal is not to automate customer support completely. Instead, the application demonstrates how AI can help organize inbound requests, retrieve relevant information, and prepare a grounded response for review.

## Example Workflow

```text
Incoming customer email
          ↓
Policy and sensitivity check
          ↓
Request classification
          ↓
Response skill selection
          ↓
Internal documentation retrieval
          ↓
RAG context assembly
          ↓
Draft response generation
          ↓
Quality-assurance check
          ↓
Draft presented for human review
```

## Example

The following example demonstrates how the application processes a simulated customer-support request.

### Incoming Email

```text
Subject: Refund request

Hello,

I purchased the annual plan yesterday, but I selected the wrong package.
Could you cancel the subscription and issue a refund?

Thank you.
```

### Processing Steps

```text
Request category: Billing / Refund
Policy-sensitive request: Yes
Selected workflow: Billing Support
Knowledge-base retrieval: Refund and cancellation policy
Human review required: Yes
```

The application classifies the request, retrieves the most relevant internal documentation, and uses the retrieved context to prepare a response draft.

Because the request involves a refund decision, the policy guard routes the draft for human review instead of treating the generated response as a final decision.

### Draft Response

```text
Hello,

Thank you for contacting us.

I understand that you selected the wrong annual plan and would like to request a cancellation and refund. I have forwarded your request for review according to our refund and cancellation policy.

A support representative will confirm your eligibility and provide the next steps.

Best,
Customer Support
```

> The example uses simulated data. Generated wording may vary because the application runs with a local language model. All responses should be reviewed before being sent to a customer.


## Main Features

### Email Triage

The application analyzes an incoming customer-support email and identifies the type of request before selecting the appropriate workflow.

### Retrieval-Augmented Generation

Relevant internal documentation is retrieved before the response is generated.

This helps ground the draft in the project’s demonstration knowledge base instead of relying only on the language model’s general knowledge.

### Semantic Vector Search

The project uses ChromaDB and Nomic Embed Text to store and retrieve documentation based on semantic similarity.

### Reusable Skills

Response instructions are stored separately as reusable skills.

These skills help control how different categories of customer requests should be handled and how responses should be written.

### Retrieval Tool

Document retrieval is separated into a callable tool, keeping retrieval logic independent from the main response-generation workflow.

### Agent-Inspired Workflow

The application uses separate workflow steps for:

* Policy checking
* Request triage
* Skill selection
* Document retrieval
* Draft generation
* Quality assurance

These components are organized as a structured, agent-inspired pipeline rather than a fully autonomous production agent.

### Guardrails and Human Review

Sensitive, unsupported, or policy-dependent requests can be routed for human review instead of receiving an automatic final response.

The generated response is treated as a draft and should be reviewed before being sent to a customer.

### Lightweight Evals

The project includes basic evaluations to test selected classification and response behaviours.

These evaluations are designed for experimentation and regression checking rather than comprehensive production AI evaluation.

## Tech Stack

* Python
* Streamlit
* LangChain
* ChromaDB
* Ollama
* Llama 3.1 8B
* Nomic Embed Text

## Architecture

```text
┌─────────────────────┐
│   Incoming Email    │
└──────────┬──────────┘
           ↓
┌─────────────────────┐
│    Policy Guard     │
└──────────┬──────────┘
           ↓
┌─────────────────────┐
│    Triage Agent     │
└──────────┬──────────┘
           ↓
┌─────────────────────┐
│   Skill Selection   │
└──────────┬──────────┘
           ↓
┌─────────────────────┐
│   Retrieval Tool    │
└──────────┬──────────┘
           ↓
┌─────────────────────┐
│      ChromaDB       │
│    Vector Search    │
└──────────┬──────────┘
           ↓
┌─────────────────────┐
│ Llama 3.1 via Ollama│
└──────────┬──────────┘
           ↓
┌─────────────────────┐
│      QA Agent       │
└──────────┬──────────┘
           ↓
┌─────────────────────┐
│   Draft Response    │
│  for Human Review   │
└─────────────────────┘
```

## Project Structure

```text
sensei-ai-assistant-langchain/
├── evals/
│   └── run_evals.py
├── knowledge_base/
├── skills/
├── src/
│   ├── agents/
│   ├── tools/
│   ├── app.py
│   ├── chains.py
│   └── database.py
├── .gitignore
├── README.md
└── requirements.txt
```

## How to Run the Project

### Prerequisites

Before running the application, install:

* Python 3.10 or later
* Git
* Ollama

## 1. Clone the Repository

```bash
git clone https://github.com/PKpacheco/sensei-ai-assistant-langchain.git
cd sensei-ai-assistant-langchain
```

## 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on macOS or Linux:

```bash
source venv/bin/activate
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

## 3. Install the Dependencies

```bash
python -m pip install -r requirements.txt
```

## 4. Start Ollama

Open a terminal and run:

```bash
ollama serve
```

Keep this terminal open while using the application.

## 5. Download the Required Models

Open another terminal and run:

```bash
ollama pull llama3.1:8b
ollama pull nomic-embed-text
```

The project uses:

* `llama3.1:8b` for response generation
* `nomic-embed-text` for document embeddings and semantic retrieval

## 6. Build the Local Vector Database

```bash
python src/database.py
```

This command processes the demonstration knowledge base and creates the local ChromaDB vector store.

The generated local database is not included in the repository and must be recreated after cloning the project.

## 7. Run the Application

```bash
python -m streamlit run src/app.py
```

The application should become available at:

```text
http://localhost:8501
```

## Running the Evals

Run the project’s lightweight evaluation suite with:

```bash
python -m evals.run_evals
```

The evals are intended to help verify selected behaviours such as request classification, escalation decisions, and draft-response handling.

They are learning-oriented checks and should not be considered a complete production evaluation framework.

## Local and Private AI Setup

The application runs locally through Ollama.

No paid external AI API key is required, and the demonstration messages and documents remain within the local environment while the project is running.

## Current Limitations

* The application runs locally and has not been deployed.
* It uses simulated customer-support emails.
* The knowledge base is intentionally small and created for demonstration purposes.
* Generated responses may be incomplete or inaccurate.
* Human review is required before using any generated response.
* The workflow is agent-inspired but is not a fully autonomous agent system.
* Guardrails are limited to the scenarios implemented in the prototype.
* The evaluation suite is lightweight and does not measure all aspects of AI quality or safety.
* The project has not been tested for production scalability, reliability, authentication, privacy, or security.

## Possible Future Improvements

* Add structured output validation for model responses
* Add confidence scoring for classification and retrieval
* Add more comprehensive test and evaluation datasets
* Measure retrieval relevance separately from response quality
* Add tracing and workflow observability
* Add fallback behaviour when no relevant documentation is found
* Add webhook or ticketing-system integrations
* Add authentication and user roles
* Store processed requests and generated drafts in a database
* Add approval, editing, and feedback workflows
* Add support for multiple knowledge-base collections
* Add automated detection of low-confidence or unsupported answers

