# Agentic Email Decision Engine

This module implements the decision-making agent for the project:
**Agentic Email Intelligence System using Embedding Gemma**.

## Responsibilities
- Accept structured email context
- Reason using a pretrained LLM (Gemma via Ollama)
- Use Embedding Gemma for semantic similarity search
- Output a safe, structured action decision

## What This Module Does NOT Do
- Train models (uses pretrained models only)
- Execute actions (handled by n8n workflows)

## Quick Start

### 1. Install Dependencies
```powershell
pip install -r requirements.txt
```

### 2. Ensure Ollama is Running
Make sure you have pulled the required models:
```powershell
ollama pull gemma:2b
ollama pull embeddinggemma:300m-bf16
```

### 3. Test the Agent (CLI)
```powershell
python test_cases.py
```

### 4. Start the API Server
```powershell
uvicorn api:app --reload --port 8000
```

The API will be available at: `http://127.0.0.1:8000`

### 5. Test the API
In a new terminal (with venv activated):
```powershell
python test_api.py
```

Or manually test with curl:
```powershell
curl -X POST "http://127.0.0.1:8000/decide" `
  -H "Content-Type: application/json" `
  -d '{
    "subject": "Production server is down",
    "body": "Users cannot log in since 10:20 AM.",
    "intent": "urgent_issue",
    "urgency": "high"
  }'
```

## API Endpoints

### GET /health
Health check endpoint.

**Response:**
```json
{"status": "ok"}
```

### POST /decide
Get a structured decision for an email.

**Request Body:**
```json
{
  "subject": "Email subject",
  "body": "Email body text",
  "intent": "urgent_issue",
  "urgency": "high"
}
```

**Response:**
```json
{
  "action": "create_ticket",
  "confidence": 0.95,
  "reasoning": "High priority, urgent issue...",
  "priority": "high",
  "sla_risk": "none",
  "department": "engineering"
}
```

## Connecting to n8n

1. In n8n, add an **HTTP Request** node
2. Set method to `POST`
3. URL: `http://127.0.0.1:8000/decide`
4. Body: JSON with `subject`, `body`, `intent`, `urgency`
5. Use the response `action`, `priority`, `department` to route workflows

## Project Structure
- `agent.py` - LLM reasoning logic
- `api.py` - FastAPI endpoints
- `config.py` - LLM configuration (Ollama)
- `embeddings.py` - Embedding Gemma model loader
- `retrieval.py` - Semantic similarity search
- `schemas.py` - Pydantic response models
- `prompts.py` - LLM prompts
- `constants.py` - Allowed values (intents, actions, etc.)
- `test_cases.py` - CLI testing
- `test_api.py` - API testing