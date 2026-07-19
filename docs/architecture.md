# Architecture

```
┌───────────────────────┐        ┌────────────────────────┐
│  Frontend (Vite/JS)  │  POST  │  Backend (FastAPI)     │
│  served by nginx     │ ─────► │  google-genai SDK      │ ──► Google Gemini
│  /api → proxy        │ ◄───── │  text/event-stream     │
│  progressive render  │  tokens└────────────────────────┘
└───────────────────────┘
```

# Request flow

1. User submits the composer form.
2. `frontend/src/main.js` `POST`s JSON to `/api/generate`.
3. nginx (production) or Vite proxy (dev) forwards to the backend on `:8000`.
4. `backend/app/routes.py` validates the body with Pydantic and calls
   `stream_gemini()`.
5. `backend/app/gemini.py` opens an async streaming completion against Gemini
   and yields `event: token` SSE frames as chunks arrive.
6. The frontend reads the `ReadableStream`, parses SSE frames, and appends
   each token to the output panel in real time.
7. `event: done` ends the stream; the Stop button aborts the fetch early.

# Security model

- `GEMINI_API_KEY` lives only in the backend environment (env var or
  docker-compose secret). It is never imported by the frontend bundle.
- `.env` files are gitignored; only `.env.example` is committed.
- CORS is restricted to configured origins (`CORS_ORIGINS`).
- Input is length-bounded and validated by Pydantic before reaching Gemini.

# Local development

See the root `README.md` for full instructions. Short version:

```bash
cp .env.example .env   # set GEMINI_API_KEY
docker compose up --build
# open http://localhost:8080
```

Or run the services separately for hot-reload:

```bash
# backend
cd backend && python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
export $(grep -v '^#' ../.env | xargs)
uvicorn app.main:app --reload --port 8000

# frontend (separate terminal)
cd frontend && npm install && npm run dev
# open http://localhost:5173
```
