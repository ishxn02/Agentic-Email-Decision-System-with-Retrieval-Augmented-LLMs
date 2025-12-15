# 🤖 Agentic Email Intelligence System

> An intelligent email automation system leveraging **Embedding Gemma** for semantic understanding and **LLM-based reasoning** for autonomous decision-making, integrated with workflow automation.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![LangChain](https://img.shields.io/badge/LangChain-0.1.16-green.svg)](https://langchain.com/)
[![Ollama](https://img.shields.io/badge/Ollama-Gemma%202B-orange.svg)](https://ollama.com/)

---

## 📋 Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [Architecture](#architecture)
- [Technology Stack](#technology-stack)
- [Project Progress](#project-progress)
- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [n8n Integration](#n8n-integration)
- [Project Structure](#project-structure)
- [Development Roadmap](#development-roadmap)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

---

## 🎯 Overview

Traditional email automation systems rely on rigid rule-based logic or simple classifiers that cannot adapt to context, understand intent, or reason about appropriate actions. This project addresses these limitations by building an **agentic AI system** that:

- **Understands** email semantics using Embedding Gemma
- **Reasons** about intent, urgency, and context using LLM-based agents
- **Decides** on appropriate actions autonomously
- **Executes** workflows through n8n integration

### What Makes This Different?

| Traditional Approach | Our Agentic Approach |
|---------------------|----------------------|
| ❌ Keyword-based rules | ✅ Semantic understanding |
| ❌ Static classifiers | ✅ Dynamic reasoning |
| ❌ No context awareness | ✅ Historical case retrieval |
| ❌ Hard-coded workflows | ✅ Autonomous decision-making |

---

## ✨ Key Features

### 🧠 Intelligent Decision Making
- **LLM-Powered Reasoning**: Uses Gemma 2B for context-aware decision logic
- **Semantic Understanding**: Embedding Gemma for vector-based email analysis
- **Confidence Scoring**: Built-in uncertainty handling with human escalation
- **Historical Context**: Retrieves similar past cases for informed decisions

### 🔄 Workflow Automation
- **n8n Integration**: Seamless connection to workflow automation
- **Multi-Action Support**: Auto-reply, ticket creation, escalation, archival
- **Department Routing**: Intelligent assignment to engineering, support, billing, etc.
- **SLA Risk Assessment**: Automatic priority and risk evaluation

### 🏗️ Production-Ready Architecture
- **RESTful API**: FastAPI-based endpoints for easy integration
- **Structured Output**: Pydantic-validated JSON responses
- **Local-First**: No external API dependencies (runs on Ollama)
- **Modular Design**: Clean separation of concerns

---

## 🏛️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     Incoming Email                          │
└──────────────────┬──────────────────────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────────────────────────┐
│              Email Ingestion Pipeline (n8n)                 │
│  • Parse email (subject, body, metadata)                    │
│  • Extract intent and urgency                               │
└──────────────────┬──────────────────────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────────────────────────┐
│           Semantic Retrieval (Embedding Gemma)              │
│  • Generate query embedding                                 │
│  • Retrieve top-k similar historical cases                  │
│  • Cosine similarity ranking                                │
└──────────────────┬──────────────────────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────────────────────────┐
│              LLM Agent (Gemma 2B via Ollama)                │
│  • Analyze email context + similar cases                    │
│  • Reason about appropriate action                          │
│  • Generate structured decision JSON                        │
│  • Confidence scoring & uncertainty handling                │
└──────────────────┬──────────────────────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────────────────────────┐
│                 Structured Decision Output                  │
│  {                                                           │
│    "action": "create_ticket",                               │
│    "confidence": 0.95,                                      │
│    "priority": "high",                                      │
│    "department": "engineering",                             │
│    "sla_risk": "medium"                                     │
│  }                                                           │
└──────────────────┬──────────────────────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────────────────────────┐
│           Workflow Execution Layer (n8n)                    │
│  • Route to appropriate department                          │
│  • Create tickets / send replies                            │
│  • Update databases / logs                                  │
│  • Trigger escalations if needed                            │
└─────────────────────────────────────────────────────────────┘
```

---

## 🛠️ Technology Stack

### Core Technologies
- **Python 3.8+**: Primary programming language
- **LangChain 0.1.16**: LLM orchestration and agent framework
- **Ollama**: Local LLM runtime (no API keys required)
- **Embedding Gemma (300M)**: Semantic vector embeddings
- **Gemma 2B**: Lightweight reasoning model

### Frameworks & Libraries
- **FastAPI**: High-performance async REST API
- **Pydantic**: Data validation and schema enforcement
- **NumPy**: Vector operations and similarity calculations
- **Uvicorn**: ASGI server for FastAPI

### Integration & Automation
- **n8n**: Open-source workflow automation platform
- **RESTful API**: Standard HTTP/JSON communication

### Why These Choices?

| Technology | Rationale |
|-----------|-----------|
| **Ollama + Gemma** | Local inference, no API costs, reproducible |
| **Embedding Gemma** | Required by project spec, optimized for semantic tasks |
| **LangChain** | Model-agnostic orchestration, easy to swap LLMs |
| **FastAPI** | Modern, fast, auto-documented APIs |
| **n8n** | Visual workflows, open-source, no-code integration |

---

## 📊 Project Progress

### ✅ Completed Components

#### Phase 1: Core Agent Development
- [x] Project architecture design
- [x] Environment setup with Ollama
- [x] Agent reasoning logic (`agent.py`)
- [x] LLM configuration (`config.py`)
- [x] Prompt engineering (`prompts.py`)
- [x] Pydantic schemas for structured output (`schemas.py`)
- [x] Constants and allowed values (`constants.py`)

#### Phase 2: Semantic Retrieval
- [x] Embedding Gemma integration (`embeddings.py`)
- [x] Cosine similarity implementation (`retrieval.py`)
- [x] Historical case retrieval system
- [x] Vector-based context enrichment

#### Phase 3: API Development
- [x] FastAPI REST endpoints (`api.py`)
- [x] `/health` endpoint for monitoring
- [x] `/decide` endpoint for email decisions
- [x] Request/response validation
- [x] API testing scripts (`test_api.py`)

#### Phase 4: Testing & Validation
- [x] CLI test cases (`test_cases.py`)
- [x] API integration tests
- [x] Ollama connection verification
- [x] End-to-end decision pipeline testing

#### Phase 5: n8n Integration
- [x] Email ingestion pipeline in n8n
- [x] Webhook connections to decision API
- [x] Workflow routing based on decisions
- [x] Action execution nodes (tickets, replies, etc.)

### 🔄 In Progress

- [ ] Persistent vector database (ChromaDB/Pinecone)
- [ ] Extended historical case library
- [ ] Performance optimization
- [ ] Comprehensive documentation

### 📅 Upcoming Work

#### Short-term (Next 2 Weeks)
- [ ] Add real email data processing
- [ ] Implement feedback loop for decision quality
- [ ] Create evaluation metrics dashboard
- [ ] Add logging and monitoring

#### Medium-term (Next Month)
- [ ] Multi-language email support
- [ ] Advanced intent classification
- [ ] Custom action templates
- [ ] User preference learning

#### Long-term (Future Enhancements)
- [ ] Fine-tuning on domain-specific data
- [ ] Multi-agent collaboration
- [ ] Real-time dashboard UI
- [ ] Mobile notifications integration

---

## 🚀 Installation

### Prerequisites

1. **Python 3.8+**
   ```bash
   python --version
   ```

2. **Ollama** (for local LLM inference)
   ```bash
   # Linux/Mac
   curl -fsSL https://ollama.com/install.sh | sh
   
   # Windows
   # Download from: https://ollama.com/download/windows
   ```

3. **Git** (for cloning the repository)
   ```bash
   git --version
   ```

### Step-by-Step Setup

#### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/agentic-email-intelligence.git
cd agentic-email-intelligence
```

#### 2. Create Virtual Environment
```bash
# Create venv
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (Linux/Mac)
source venv/bin/activate
```

#### 3. Install Python Dependencies
```bash
pip install -r requirements.txt
```

#### 4. Pull Required Models
```bash
# Pull Gemma 2B for reasoning (~1.5GB)
ollama pull gemma:2b

# Pull Embedding Gemma for semantic understanding (~300MB)
ollama pull embeddinggemma:300m-bf16

# Verify installation
ollama list
```

#### 5. Test the Setup
```bash
# Test CLI agent
python test_cases.py

# Start API server
uvicorn api:app --reload --port 8000

# In a new terminal, test API
python test_api.py
```

### Troubleshooting

**Issue: "Ollama connection failed"**
```bash
# Check if Ollama is running
ollama list

# Start Ollama service manually
ollama serve
```

**Issue: "Model not found"**
```bash
# Re-pull the models
ollama pull gemma:2b
ollama pull embeddinggemma:300m-bf16
```

**Issue: "Import errors"**
```bash
# Ensure virtual environment is activated
# Then reinstall dependencies
pip install --upgrade -r requirements.txt
```

---

## 💻 Usage

### Command-Line Interface

#### Basic Decision Test
```bash
python test_cases.py
```

**Output:**
```
Similar cases used for context:
- Database outage in production causing login failures
- Low-severity bug reported in staging environment

Structured decision:
{
  "action": "create_ticket",
  "confidence": 0.95,
  "reasoning": "High urgency production issue requiring immediate attention",
  "priority": "high",
  "sla_risk": "medium",
  "department": "engineering"
}
```

### API Usage

#### Start the Server
```bash
uvicorn api:app --reload --port 8000
```

#### Make API Requests

**Using cURL:**
```bash
curl -X POST "http://127.0.0.1:8000/decide" \
  -H "Content-Type: application/json" \
  -d '{
    "subject": "Payment failed multiple times",
    "body": "I have been trying to complete payment for 3 days. Transaction keeps failing.",
    "intent": "billing_query",
    "urgency": "medium"
  }'
```

**Using Python:**
```python
import requests

response = requests.post(
    "http://127.0.0.1:8000/decide",
    json={
        "subject": "Cannot access dashboard",
        "body": "Getting 403 error when trying to log in",
        "intent": "account_issue",
        "urgency": "high"
    }
)

print(response.json())
```

**Using JavaScript:**
```javascript
fetch('http://127.0.0.1:8000/decide', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    subject: 'Feature request: Dark mode',
    body: 'Would love to see dark mode support',
    intent: 'feedback',
    urgency: 'low'
  })
})
.then(res => res.json())
.then(data => console.log(data));
```

---

## 📚 API Documentation

### Endpoints

#### `GET /health`
Health check endpoint for monitoring.

**Response:**
```json
{
  "status": "ok"
}
```

---

#### `POST /decide`
Get an intelligent decision for an incoming email.

**Request Body:**
```json
{
  "subject": "string (required)",
  "body": "string (required)",
  "intent": "string (required)",
  "urgency": "string (required)"
}
```

**Allowed Values:**

**Intent Types:**
- `incident_report`
- `service_request`
- `account_issue`
- `billing_query`
- `sales_inquiry`
- `complaint`
- `feedback`
- `internal_request`
- `security_alert`
- `unknown`

**Urgency Levels:**
- `low`
- `medium`
- `high`
- `critical`

**Response:**
```json
{
  "action": "create_ticket",
  "confidence": 0.92,
  "reasoning": "High urgency account issue requires support ticket",
  "priority": "high",
  "sla_risk": "medium",
  "department": "support"
}
```

**Response Fields:**

| Field | Type | Description |
|-------|------|-------------|
| `action` | string | Recommended action (see actions below) |
| `confidence` | float | Agent confidence (0.0-1.0) |
| `reasoning` | string | Explanation for the decision |
| `priority` | string | Priority level (low/medium/high/critical) |
| `sla_risk` | string | SLA breach risk (none/low/medium/high) |
| `department` | string | Responsible department |

**Available Actions:**
- `send_auto_reply`
- `create_ticket`
- `notify_admin`
- `archive_email`
- `mark_important`
- `no_action`

**Departments:**
- `engineering`
- `support`
- `billing`
- `sales`
- `hr`
- `general`

---

## 🔗 n8n Integration

### Setup Instructions

#### 1. Install n8n
```bash
npm install -g n8n

# Or using Docker
docker run -it --rm \
  --name n8n \
  -p 5678:5678 \
  n8nio/n8n
```

#### 2. Create Email Ingestion Workflow

**Workflow Structure:**
```
Email Trigger → Parse Email → Extract Intent → 
Call Decision API → Route by Action → Execute Workflow
```

#### 3. Configure HTTP Request Node

**Settings:**
- **Method:** POST
- **URL:** `http://127.0.0.1:8000/decide`
- **Body Type:** JSON
- **Body:**
```json
{
  "subject": "{{ $json.subject }}",
  "body": "{{ $json.body }}",
  "intent": "{{ $json.intent }}",
  "urgency": "{{ $json.urgency }}"
}
```

#### 4. Route Based on Decision

Use **Switch** node with conditions:
- If `action === "create_ticket"` → Jira/ServiceNow node
- If `action === "send_auto_reply"` → Email send node
- If `action === "notify_admin"` → Slack/Teams notification
- If `action === "archive_email"` → Archive node

### Example n8n Workflow JSON

```json
{
  "nodes": [
    {
      "name": "Email Trigger",
      "type": "n8n-nodes-base.emailReadImap",
      "position": [250, 300]
    },
    {
      "name": "Decision API",
      "type": "n8n-nodes-base.httpRequest",
      "parameters": {
        "url": "http://127.0.0.1:8000/decide",
        "method": "POST",
        "bodyParametersJson": "={{ JSON.stringify($json) }}"
      },
      "position": [450, 300]
    },
    {
      "name": "Route Action",
      "type": "n8n-nodes-base.switch",
      "parameters": {
        "rules": {
          "rules": [
            {
              "conditions": {
                "conditions": [
                  {
                    "value1": "={{ $json.action }}",
                    "operation": "equals",
                    "value2": "create_ticket"
                  }
                ]
              }
            }
          ]
        }
      },
      "position": [650, 300]
    }
  ]
}
```

---

## 📁 Project Structure

```
agentic-email-intelligence/
│
├── agent.py                 # Core agent reasoning logic
├── api.py                   # FastAPI REST endpoints
├── config.py                # LLM configuration (Ollama)
├── embeddings.py            # Embedding Gemma integration
├── retrieval.py             # Semantic similarity search
├── schemas.py               # Pydantic data models
├── prompts.py               # LLM system and task prompts
├── constants.py             # Allowed values (intents, actions, etc.)
│
├── test_cases.py            # CLI testing script
├── test_api.py              # API testing script
│
├── requirements.txt         # Python dependencies
├── README.md                # This file
├── LICENSE                  # MIT License
│
├── n8n_workflows/           # n8n workflow exports (if applicable)
│   └── email_pipeline.json
│
└── docs/                    # Additional documentation
    ├── ARCHITECTURE.md      # Detailed architecture
    ├── API_REFERENCE.md     # Full API documentation
    └── EVALUATION.md        # Performance metrics
```

---

## 🗺️ Development Roadmap

### Version 1.0 (Current)
- ✅ Core agent with LLM reasoning
- ✅ Embedding-based retrieval
- ✅ REST API endpoints
- ✅ n8n integration
- ✅ Basic testing suite

### Version 1.1 (Q1 2025)
- [ ] Persistent vector database
- [ ] Enhanced historical case library
- [ ] Performance metrics dashboard
- [ ] Comprehensive logging

### Version 2.0 (Q2 2025)
- [ ] Multi-language support
- [ ] Custom action templates
- [ ] User preference learning
- [ ] Advanced analytics

### Version 3.0 (Future)
- [ ] Multi-agent collaboration
- [ ] Real-time web dashboard
- [ ] Mobile app integration
- [ ] Fine-tuned domain models

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### How to Contribute

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Commit your changes**
   ```bash
   git commit -m 'Add amazing feature'
   ```
4. **Push to the branch**
   ```bash
   git push origin feature/amazing-feature
   ```
5. **Open a Pull Request**

### Contribution Guidelines

- Follow PEP 8 style guide for Python code
- Add tests for new features
- Update documentation as needed
- Keep commits atomic and well-described
- Ensure all tests pass before submitting PR

### Areas We Need Help With

- [ ] Additional email intent categories
- [ ] Performance benchmarking
- [ ] Multi-language support
- [ ] UI/dashboard development
- [ ] Documentation improvements

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2024 [Your Name/Organization]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 🙏 Acknowledgments

### Technologies & Frameworks
- **Google** for Gemma and Embedding Gemma models
- **Ollama** for local LLM infrastructure
- **LangChain** for agent orchestration framework
- **n8n** for workflow automation platform
- **FastAPI** for modern API framework

### Inspiration
This project was inspired by the need for more intelligent, context-aware email automation systems that go beyond simple rule-based approaches.

### Academic Context
Developed as part of a research project exploring agentic AI systems for enterprise automation.

---

## 📞 Contact & Support

- **Issues:** [GitHub Issues](https://github.com/yourusername/agentic-email-intelligence/issues)
- **Discussions:** [GitHub Discussions](https://github.com/yourusername/agentic-email-intelligence/discussions)
- **Email:** ishan02@gmail.com

---

## 📊 Project Status



**Status:** 🟢 Active Development

---

<div align="center">

### ⭐ Star this repo if you find it useful!

</div>
