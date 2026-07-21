# 🚀 Content Studio — AI Content Generation Platform

Content Studio is a full-stack AI-powered content generation platform that generates content in real time using Large Language Models (LLMs). It features a provider-based architecture, allowing different AI providers to be integrated without changing the application logic.

The application consists of a **FastAPI backend** that securely communicates with the LLM and a **Vite-powered frontend** that displays streaming responses using **Server-Sent Events (SSE)**.

---

# 🌐 Live Demo

### Frontend
https://content-generation-frontend.onrender.com

### Backend API
https://content-generation-tool.onrender.com

### API Documentation
https://content-generation-tool.onrender.com/docs

---

# ✨ Features

- 🤖 AI-powered content generation
- ⚡ Real-time streaming responses using Server-Sent Events (SSE)
- 🧩 Provider-based LLM architecture
- 🚀 FastAPI backend
- 💻 Vanilla JavaScript + Vite frontend
- 🔒 Secure server-side API key management
- ❤️ Backend health monitoring
- 🎛 Configurable model, temperature, and max tokens
- 🌐 Live deployment on Render
- 📦 Docker & Docker Compose support
- 🔄 Easily extensible for additional AI providers

---

# 🛠 Tech Stack

## Frontend

- HTML5
- CSS3
- Vanilla JavaScript
- Vite

## Backend

- FastAPI
- Pydantic
- Uvicorn
- Server-Sent Events (SSE)

## AI Provider

Current Provider

- Groq (Llama 3.3 70B Versatile)

Supported Architecture

- Groq
- OpenAI
- Google Gemini
- Ollama

## Deployment

- Render (Frontend)
- Render (Backend)
- Docker
- Docker Compose

---

# 📂 Project Structure

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
│
├── docker-compose.yml
├── .env.example
├── .gitignore
└── README.md
```

---

# 🏗 Architecture

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
                 +---------------------------+
                 |      FastAPI Backend      |
                 |                           |
                 | Input Validation          |
                 | REST API                  |
                 | Streaming (SSE)           |
                 +------------+--------------+
                              |
                              ▼
                    +----------------------+
                    |     LLM Factory      |
                    +----------+-----------+
                               |
              +----------------+----------------+
              |                |                |
              ▼                ▼                ▼
           Groq            OpenAI          Gemini
              |
              ▼
       Streaming Tokens
              |
              ▼
        Browser Output
```

---

# 📷 Screenshots

> Add screenshots here after deployment.

Suggested screenshots:

- Home Page
- Streaming Content Generation
- Backend Ready Status
- API Documentation

---

# ⚙️ Environment Variables

Example `.env`

```env
LLM_PROVIDER=groq

GROQ_API_KEY=your_api_key

GROQ_MODEL=llama-3.3-70b-versatile

CORS_ORIGINS=http://localhost:5173,http://127.0.0.1:5173,http://localhost:8080
```

For production, include your deployed frontend URL in `CORS_ORIGINS`.

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/vaibhavmamgain29-blip/content-generation-tool.git

cd content-generation-tool
```

---

# 🐳 Running with Docker

```bash
docker compose up --build
```

Application

```
http://localhost:8080
```

---

# 💻 Local Development

## Backend

```bash
cd backend

python -m venv .venv
```

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create `.env`

```env
LLM_PROVIDER=groq
GROQ_API_KEY=your_api_key
GROQ_MODEL=llama-3.3-70b-versatile
```

Run backend

```bash
uvicorn app.main:app --reload
```

Backend

```
http://localhost:8000
```

Swagger

```
http://localhost:8000/docs
```

---

## Frontend

```bash
cd frontend

npm install
```

Create

```
.env
```

Add

```env
VITE_API_URL=http://localhost:8000
```

Run

```bash
npm run dev
```

Frontend

```
http://localhost:5173
```

---

# 📡 API Endpoints

## Health Check

```
GET /api/health
```

Example Response

```json
{
  "status": "ok",
  "llm_configured": true,
  "model": "groq:llama-3.3-70b-versatile"
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
  "prompt": "Write a blog on Artificial Intelligence",
  "temperature": 0.7,
  "max_tokens": 2048
}
```

---

# ⚡ Streaming Response

The backend streams responses using **Server-Sent Events (SSE)**.

Example stream

```text
data: {"type":"token","content":"Artificial"}

data: {"type":"token","content":" Intelligence"}

data: {"type":"done"}
```

The frontend renders each token immediately, providing a smooth real-time generation experience.

---

# 🔧 Configuration

The active AI provider is selected using

```env
LLM_PROVIDER
```

Supported providers

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

No changes to the API routes are required.

---

# 🔐 Security

- API keys remain on the backend
- Environment-variable based configuration
- CORS protection enabled
- Request validation using Pydantic
- Secure streaming using FastAPI
- No API keys exposed to the frontend

---

# 🚀 Deployment

The project is currently deployed on **Render**.

### Frontend

https://content-generation-frontend.onrender.com

### Backend

https://content-generation-tool.onrender.com

### API Documentation

https://content-generation-tool.onrender.com/docs

The project can also be deployed using Docker on AWS, Azure, Google Cloud, or any VPS.

---

# 🔮 Future Enhancements

- User Authentication
- Conversation History
- Prompt Templates
- Multiple AI Providers
- Export to PDF
- Export to DOCX
- Markdown Export
- AI Rewrite
- AI Summarization
- AI Translation
- Dark Mode
- User Accounts
- Usage Analytics

---

# 👨‍💻 Author

**Vaibhav Mamgain**

B.Tech Computer Science Engineering

GitHub

https://github.com/vaibhavmamgain29-blip

LinkedIn

(Add your LinkedIn profile)

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

---

# License

This project is developed for educational and demonstration purposes.# 🚀 Content Studio — AI Content Generation Platform

Content Studio is a full-stack AI-powered content generation platform that generates content in real time using Large Language Models (LLMs). It features a provider-based architecture, allowing different AI providers to be integrated without changing the application logic.

The application consists of a **FastAPI backend** that securely communicates with the LLM and a **Vite-powered frontend** that displays streaming responses using **Server-Sent Events (SSE)**.

---

# 🌐 Live Demo

### Frontend
https://content-generation-frontend.onrender.com

### Backend API
https://content-generation-tool.onrender.com

### API Documentation
https://content-generation-tool.onrender.com/docs

---

# ✨ Features

- 🤖 AI-powered content generation
- ⚡ Real-time streaming responses using Server-Sent Events (SSE)
- 🧩 Provider-based LLM architecture
- 🚀 FastAPI backend
- 💻 Vanilla JavaScript + Vite frontend
- 🔒 Secure server-side API key management
- ❤️ Backend health monitoring
- 🎛 Configurable model, temperature, and max tokens
- 🌐 Live deployment on Render
- 📦 Docker & Docker Compose support
- 🔄 Easily extensible for additional AI providers

---

# 🛠 Tech Stack

## Frontend

- HTML5
- CSS3
- Vanilla JavaScript
- Vite

## Backend

- FastAPI
- Pydantic
- Uvicorn
- Server-Sent Events (SSE)

## AI Provider

Current Provider

- Groq (Llama 3.3 70B Versatile)

Supported Architecture

- Groq
- OpenAI
- Google Gemini
- Ollama

## Deployment

- Render (Frontend)
- Render (Backend)
- Docker
- Docker Compose

---

# 📂 Project Structure

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
│
├── docker-compose.yml
├── .env.example
├── .gitignore
└── README.md
```

---

# 🏗 Architecture

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
                 +---------------------------+
                 |      FastAPI Backend      |
                 |                           |
                 | Input Validation          |
                 | REST API                  |
                 | Streaming (SSE)           |
                 +------------+--------------+
                              |
                              ▼
                    +----------------------+
                    |     LLM Factory      |
                    +----------+-----------+
                               |
              +----------------+----------------+
              |                |                |
              ▼                ▼                ▼
           Groq            OpenAI          Gemini
              |
              ▼
       Streaming Tokens
              |
              ▼
        Browser Output
```

---

# 📷 Screenshots

> Add screenshots here after deployment.

Suggested screenshots:

- Home Page
- Streaming Content Generation
- Backend Ready Status
- API Documentation

---

# ⚙️ Environment Variables

Example `.env`

```env
LLM_PROVIDER=groq

GROQ_API_KEY=your_api_key

GROQ_MODEL=llama-3.3-70b-versatile

CORS_ORIGINS=http://localhost:5173,http://127.0.0.1:5173,http://localhost:8080
```

For production, include your deployed frontend URL in `CORS_ORIGINS`.

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/vaibhavmamgain29-blip/content-generation-tool.git

cd content-generation-tool
```

---

# 🐳 Running with Docker

```bash
docker compose up --build
```

Application

```
http://localhost:8080
```

---

# 💻 Local Development

## Backend

```bash
cd backend

python -m venv .venv
```

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create `.env`

```env
LLM_PROVIDER=groq
GROQ_API_KEY=your_api_key
GROQ_MODEL=llama-3.3-70b-versatile
```

Run backend

```bash
uvicorn app.main:app --reload
```

Backend

```
http://localhost:8000
```

Swagger

```
http://localhost:8000/docs
```

---

## Frontend

```bash
cd frontend

npm install
```

Create

```
.env
```

Add

```env
VITE_API_URL=http://localhost:8000
```

Run

```bash
npm run dev
```

Frontend

```
http://localhost:5173
```

---

# 📡 API Endpoints

## Health Check

```
GET /api/health
```

Example Response

```json
{
  "status": "ok",
  "llm_configured": true,
  "model": "groq:llama-3.3-70b-versatile"
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
  "prompt": "Write a blog on Artificial Intelligence",
  "temperature": 0.7,
  "max_tokens": 2048
}
```

---

# ⚡ Streaming Response

The backend streams responses using **Server-Sent Events (SSE)**.

Example stream

```text
data: {"type":"token","content":"Artificial"}

data: {"type":"token","content":" Intelligence"}

data: {"type":"done"}
```

The frontend renders each token immediately, providing a smooth real-time generation experience.

---

# 🔧 Configuration

The active AI provider is selected using

```env
LLM_PROVIDER
```

Supported providers

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

No changes to the API routes are required.

---

# 🔐 Security

- API keys remain on the backend
- Environment-variable based configuration
- CORS protection enabled
- Request validation using Pydantic
- Secure streaming using FastAPI
- No API keys exposed to the frontend

---

# 🚀 Deployment

The project is currently deployed on **Render**.

### Frontend

https://content-generation-frontend.onrender.com

### Backend

https://content-generation-tool.onrender.com

### API Documentation

https://content-generation-tool.onrender.com/docs

The project can also be deployed using Docker on AWS, Azure, Google Cloud, or any VPS.

---

# 🔮 Future Enhancements

- User Authentication
- Conversation History
- Prompt Templates
- Multiple AI Providers
- Export to PDF
- Export to DOCX
- Markdown Export
- AI Rewrite
- AI Summarization
- AI Translation
- Dark Mode
- User Accounts
- Usage Analytics

---

# 👨‍💻 Author

**Vaibhav Mamgain**

B.Tech Computer Science Engineering

GitHub

https://github.com/vaibhavmamgain29-blip

LinkedIn

(Add your LinkedIn profile)

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

---

# License

This project is developed for educational and demonstration purposes.