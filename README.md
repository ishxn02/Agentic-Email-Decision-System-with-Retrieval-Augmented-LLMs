# Agentic Email Intelligence System

> An intelligent email automation system leveraging Embedding Gemma for semantic understanding and LLM-based reasoning for autonomous decision-making.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Ollama](https://img.shields.io/badge/Ollama-Gemma%202B-orange.svg)](https://ollama.com/)

---

## Overview

Traditional email systems use rigid rules and can't adapt to context. This project builds an agentic AI system that:

- Understands email semantics using Embedding Gemma
- Reasons about intent and urgency using LLM agents  
- Decides on appropriate actions autonomously
- Executes workflows through n8n integration

No rule-based logic. No static classifiers. Just intelligent reasoning.

---

## Key Features

- **LLM-Powered Reasoning**: Uses Gemma 2B for context-aware decisions
- **Semantic Understanding**: Embedding Gemma for vector-based email analysis
- **Confidence Scoring**: Built-in uncertainty handling with human escalation
- **Historical Context**: Retrieves similar past cases for informed decisions
- **RESTful API**: FastAPI endpoints for easy integration
- **Workflow Automation**: Seamless n8n integration
- **Local-First**: No external API costs (runs on Ollama)

---

## Quick Start

### Prerequisites
```bash
# Install Ollama
curl -fsSL https://ollama.com/install.sh | sh

# Pull required models
ollama pull gemma:2b
ollama pull embeddinggemma:300m-bf16
```

### Installation
```bash
git clone https://github.com/yourusername/agentic-email-intelligence.git
cd agentic-email-intelligence
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Usage
```bash
# Test the agent
python test_cases.py

# Start API server
uvicorn api:app --reload --port 8000
```

### Example Request
```bash
curl -X POST "http://127.0.0.1:8000/decide" \
  -H "Content-Type: application/json" \
  -d '{
    "subject": "Production server down",
    "body": "Users cannot login since 10 AM",
    "intent": "urgent_issue",
    "urgency": "high"
  }'
```

**Response:**
```json
{
  "action": "create_ticket",
  "confidence": 0.95,
  "priority": "high",
  "department": "engineering",
  "sla_risk": "medium",
  "reasoning": "High urgency production issue requiring immediate attention"
}
```

---

## Documentation

- [Installation Guide](docs/INSTALLATION.md) - Detailed setup instructions
- [Architecture](docs/ARCHITECTURE.md) - System design and flow
- [API Reference](docs/API_REFERENCE.md) - Complete endpoint documentation
- [n8n Integration](docs/N8N_INTEGRATION.md) - Workflow automation setup
- [Troubleshooting](docs/TROUBLESHOOTING.md) - Common issues and solutions

---

## Architecture Overview

```
Email → n8n Ingestion → Embedding Gemma (Retrieval) 
  → LLM Agent (Gemma 2B) → Structured Decision 
  → n8n Workflows → Action Execution
```

See [detailed architecture documentation](docs/ARCHITECTURE.md) for more information.

---

## Project Status

### Completed
- Core agent with LLM reasoning
- Embedding-based semantic retrieval
- REST API endpoints
- n8n email ingestion pipeline
- Structured decision output
- Testing suite

### In Progress
- Persistent vector database
- Performance optimization
- Extended historical cases

### Planned
- Multi-language support
- Custom action templates
- Analytics dashboard
- Fine-tuned domain models

See [CHANGELOG.md](CHANGELOG.md) for detailed version history.

---

## Technology Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| LLM Reasoning | Gemma 2B (Ollama) | Decision-making logic |
| Embeddings | Embedding Gemma | Semantic understanding |
| Orchestration | LangChain | Agent framework |
| API | FastAPI | REST endpoints |
| Workflows | n8n | Automation execution |

**Why local models?** No API costs, full privacy, reproducible research.

---

## Contributing

We welcome contributions. Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on:
- Submitting issues and pull requests
- Code style guidelines  
- Development setup
- Testing requirements

---

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

## Acknowledgments

Built with:
- [Gemma](https://ai.google.dev/gemma) by Google
- [Ollama](https://ollama.com/) for local LLM inference
- [LangChain](https://langchain.com/) for agent orchestration
- [n8n](https://n8n.io/) for workflow automation
- [FastAPI](https://fastapi.tiangolo.com/) for API framework

---

## Contact

- Issues: [GitHub Issues](https://github.com/yourusername/agentic-email-intelligence/issues)
- Email: ishan02@gmail.com

---

Made with open-source technologies | ![Status](https://img.shields.io/badge/status-active-success.svg)
