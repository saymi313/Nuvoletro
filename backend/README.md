# Nuvoletro Backend API ☁️

The core backend API service for **Nuvoletro**, built with **FastAPI** and **Python 3.11**.

This service handles:

* YouTube ingestion
* RAG memory retrieval using ChromaDB
* LLM text generation using LangChain

---

## 🛠 Prerequisites

* **Python 3.11** (strict requirement — do **not** use 3.12 or 3.13)
* **Docker Desktop** (for PostgreSQL, Redis, and ChromaDB)

---

## 🚀 Quick Start (Local Development)

Follow these steps to set up and run the backend locally.

### 1. Create a virtual environment

> **Do NOT** upload your `venv` directory to GitHub.

#### Windows (PowerShell)

```powershell
py -3.11 -m venv venv
.\venv\Scripts\Activate.ps1
```

#### macOS / Linux

```bash
python3.11 -m venv venv
source venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Start infrastructure (Postgres, Redis, ChromaDB)

Run from the **project root** (`/nuvoletro`):

```bash
docker-compose up -d
```

This will start:

* PostgreSQL
* Redis
* ChromaDB

### 4. Run the API server

From the backend folder (where `app` lives):

```bash
uvicorn app.main:app --reload
```

---

## 📚 API Documentation

When the server is running, open the interactive docs:

* **Swagger UI:** `http://localhost:8000/docs`
* **ReDoc:** `http://localhost:8000/redoc`

---

## 📂 Project structure

```text
backend/
├── app/
│   ├── main.py            # App entry point
│   ├── models/            # SQLAlchemy models (DB tables)
│   ├── schemas/           # Pydantic request/response schemas
│   ├── routers/           # API endpoints (routes)
│   ├── services/          # Business logic (scraper, AI, RAG)
│   ├── core/              # Config, security, utilities
│   └── config.py          # Environment variable settings
├── requirements.txt       # Python dependencies
└── Dockerfile             # Production build
```

---

## 🔑 Environment variables

Create a `.env` file in the backend folder to override defaults. Example dev values:

```bash
DATABASE_URL=postgresql://user:password@localhost:5432/nuvoletro
OPENAI_API_KEY=sk-...  # get this from your Team Lead
```

> Keep secrets out of source control. Use a secrets manager for production.

---

## 🧪 Running tests

```bash
pytest
```

---

## ✅ Optional additions (I can add these if you want)

* Badges (CI, Python, Docker) at the top
* `CONTRIBUTING.md` and `CODE_OF_CONDUCT.md`
* GitHub Actions CI workflow (lint, tests, build)
* Production `docker-compose.prod.yml` and deployment notes
* Architecture diagram (ASCII or image)

If you want any of the above, tell me which and I’ll add it.
