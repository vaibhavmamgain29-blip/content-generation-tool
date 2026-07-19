# Content Generation Tool

# Content Studio — AI Content Generation Platform

Content Studio is a full-stack AI-powered content generation platform that streams responses in real time using Large Language Models (LLMs).

The project follows a provider-based architecture, allowing different AI providers to be plugged in without changing the application logic. Currently, the backend is configured to use **Groq** by default, with support for adding **OpenAI**, **Google Gemini**, **Ollama**, and other providers in the future.

The application consists of a FastAPI backend that securely communicates with the LLM and a Vite-powered frontend that displays streaming responses using Server-Sent Events (SSE).

---

# Features

- Real-time AI response streaming
- Provider-based LLM architecture
- FastAPI backend
- Vanilla JavaScript + Vite frontend
- Server-Sent Events (SSE)
- Secure server-side API key management
- Docker & Docker Compose support
- Health monitoring endpoint
- Configurable model, temperature, and max tokens
- Production-ready deployment structure

---

# Tech Stack

### Frontend

- HTML5
- CSS3
- Vanilla JavaScript
- Vite

### Backend

- FastAPI
- Pydantic
- Uvicorn
- Async Streaming (SSE)

### AI Provider

- Groq (Default)

Supported providers (extensible):

- Groq
- OpenAI
- Google Gemini
- Ollama

### Deployment

- Docker
- Docker Compose
- Nginx
- AWS App Runner
- AWS ECS
- Elastic Beanstalk

---

# Project Structure

```text
content-generation-tool/
│
├── frontend/
│   ├── src/
│   │   ├── index.html
│   │   ├── main.js
│   │   └── styles.css
│   │
│   ├── public/
│   ├── nginx.conf
│   ├── package.json
│   ├── vite.config.js
│   └── Dockerfile
│
├── backend/
│   ├── app/
│   │
│   ├── llm/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── factory.py
│   │   └── groq.py
│   │
│   ├── config.py
│   ├── routes.py
│   ├── schemas.py
│   ├── main.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── docs/
│   ├── architecture.md
│   └── deployment.md
│
├── docker-compose.yml
├── .env.example
├── .gitignore
└── README.md
```

---

# Architecture

```text
                    +----------------------+
                    |      Frontend        |
                    | HTML • CSS • JS      |
                    | Vite                 |
                    +----------+-----------+
                               |
                               | HTTP Request
                               |
                               ▼
                  +--------------------------+
                  |      FastAPI Backend     |
                  |                          |
                  |  Input Validation        |
                  |  API Routes              |
                  |  Streaming (SSE)         |
                  +------------+-------------+
                               |
                               |
                               ▼
                    +----------------------+
                    |    LLM Factory       |
                    +----------+-----------+
                               |
                +--------------+--------------+
                |              |              |
                ▼              ▼              ▼
             Groq         OpenAI        Gemini
                |
                ▼
          Streaming Tokens
                |
                ▼
           Browser Output
```

---

# Environment Variables

Example `.env`

```env
LLM_PROVIDER=groq

GROQ_API_KEY=your_api_key_here

GROQ_MODEL=llama-3.3-70b-versatile

CORS_ORIGINS=http://localhost:8080
```

---

# Installation

## Clone Repository

```bash
git clone <repository-url>

cd content-generation-tool
```

---

# Running with Docker

```bash
docker compose up --build
```

Application will be available at

```
http://localhost:8080
```

---

# Local Development

## Backend

```bash
cd backend

python -m venv .venv
```

### Windows

```bash
.venv\Scripts\activate
```

### Linux/macOS

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run backend

```bash
python -m uvicorn app.main:app --reload --port 8000
```

---

## Frontend

```bash
cd frontend

npm install

npm run dev
```

Open

```
http://localhost:5173
```

---

# API Endpoints

## Health Check

```
GET /api/health
```

Example Response

```json
{
    "status":"ok",
    "llm_configured":true,
    "model":"groq:llama-3.3-70b-versatile"
}
```

---

## Generate Content

```
POST /api/generate
```

Request

```json
{
    "prompt":"Write a blog on Artificial Intelligence.",
    "temperature":0.7,
    "max_tokens":2048
}
```

---

# Streaming Response

The backend streams responses using **Server-Sent Events (SSE).**

Example stream

```json
data: {
  "type":"token",
  "content":"Artificial"
}

data: {
  "type":"token",
  "content":" Intelligence"
}

data: {
  "type":"done"
}
```

The frontend renders each token immediately, providing a smooth real-time generation experience.

---

# Configuration

The AI provider is selected using

```env
LLM_PROVIDER
```

Supported values

```
groq
openai
gemini
ollama
```

Adding a new provider only requires implementing a new provider class inside

```
backend/app/llm/
```

No changes are required in the API routes.

---

# Security

- API keys are stored only on the backend.
- Secrets are loaded using environment variables.
- API keys are never exposed to the frontend.
- CORS protection enabled.
- Request validation using Pydantic.
- Streaming handled securely through FastAPI.

---

# Docker

The application uses two containers.

### Backend

- FastAPI
- Uvicorn
- AI Provider

### Frontend

- Nginx
- Vite Production Build

Docker Compose orchestrates both services.

---

# Deployment

The project is deployment-ready for

- AWS App Runner
- AWS ECS
- Elastic Beanstalk
- Docker-based VPS
- Azure App Service
- Google Cloud Run

Deployment only requires configuring the appropriate environment variables.

---

# Future Enhancements

- Authentication
- Conversation History
- Multiple AI Providers
- Prompt Templates
- Export to PDF
- Export to DOCX
- Markdown Export
- AI Rewrite
- AI Summarization
- AI Translation
- Usage Analytics
- Dark Mode
- Multi-user Support

---

# License

This project is developed for educational and demonstration purposes.