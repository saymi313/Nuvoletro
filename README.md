# Nuvoletro

*AI-Powered Content Repurposer for YouTube Creators*

Nuvoletro is an innovative AI-driven SaaS application that transforms long-form YouTube videos into platform-optimized textual content, including titles, descriptions, social media captions, and short scripts. Supporting bilingual (English/Urdu) generation and brand voice consistency through Retrieval-Augmented Generation (RAG), it streamlines content repurposing workflows for creators and marketing teams.

## Features

- **YouTube Video Ingestion**: Automatically fetch and transcribe videos via YouTube API or Whisper for seamless processing.
- **Multi-Platform Outputs**: Generate tailored content for LinkedIn, Twitter, Instagram, and more, with hooks, bullet points, and captions.
- **Bilingual Support**: Handles English, Urdu, and code-switched text for diverse audiences.
- **Brand Voice Memory**: RAG-based vector store remembers your style from past posts for consistent outputs.
- **User Dashboard**: Simple React-based interface for uploads, output selection, history, and exports.
- **Production-Ready Backend**: Scalable FastAPI service with LangChain orchestration for agentic workflows.
- **Deployment**: Dockerized for local/cloud deployment with CI/CD support.

## Tech Stack

- **Frontend**: React.js (with Next.js for routing and state management via Redux/Context API)
- **Backend**: Python 3.10+ with FastAPI for REST APIs
- **AI/ML Frameworks**: LangChain for agent orchestration, LlamaIndex for RAG pipelines
- **Language Models**: OpenAI GPT-4/Llama-3/Mistral via API; Whisper for transcription
- **Vector Storage**: ChromaDB/FAISS for per-user brand memory
- **Other Libraries**: 
  - YouTube Data API (video fetching)
  - spaCy/Transformers for NLP preprocessing
  - Pytest for testing
  - Docker & Docker Compose for containerization
- **Database**: SQLite/PostgreSQL for user data (optional Redis for caching)
- **Deployment**: Docker, optional cloud (Vercel for frontend, Heroku/AWS for backend)

## Architecture

┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   React UI      │◄──►│   FastAPI APIs   │◄──►│   LangChain     │
│   (Dashboard)   │    │   (Auth/Endpoints)│    │   (Agents/RAG)  │
└─────────────────┘    └──────────────────┘    └─────────────────┘
                                      │
                                      ▼
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│ YouTube API     │◄──►│   Vector Store   │◄──►│   LLM APIs      │
│ (Transcripts)   │    │   (ChromaDB)      │    │ (OpenAI/Mistral)│
└─────────────────┘    └──────────────────┘    └─────────────────┘

- **Frontend**: Handles user authentication, video uploads, and displays generated content.
- **Backend**: Exposes REST endpoints for ingestion, processing, and retrieval.
- **Core Pipeline**: Multi-agent workflow (Transcription Agent → Planning Agent → Generation Agent) with RAG for brand consistency.

## Prerequisites

- Node.js 18+ (for React frontend)
- Python 3.10+ (for backend)
- Docker & Docker Compose (recommended for development/deployment)
- API Keys: OpenAI (or alternative LLM), YouTube Data API
- Git

## Setup Instructions

### 1. Clone the Repository

git clone https://github.com/saymi313/nuvoletro.git
cd nuvoletro


### 2. Backend Setup (Python/FastAPI)
Navigate to backend directory
cd backend

Create virtual environment
python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate

Install dependencies
pip install -r requirements.txt

Set environment variables (create .env file)
cp .env.example .env

Edit .env with your API keys:
OPENAI_API_KEY=your_openai_key
YOUTUBE_API_KEY=your_youtube_key
DATABASE_URL=sqlite:///nuvoletro.db # Or PostgreSQL URL
Run migrations (if using SQLAlchemy)
alembic upgrade head

Start the server
uvicorn main:app --reload --host 0.0.0.0 --port 8000


Key dependencies from `requirements.txt`:
fastapi==0.104.1
uvicorn[standard]==0.24.0
langchain==0.0.350
openai==1.3.7
chromadb==0.4.18
google-api-python-client==2.111.1
pydantic[email]==2.5.0
pytest==7.4.3


Docker Compose handles separate services for frontend, backend, and optional database.

## Usage

1. **Login/Register**: Use the React dashboard to create an account.
2. **Upload Video**: Paste a YouTube URL or upload a file.
3. **Select Outputs**: Choose platforms (e.g., LinkedIn, Instagram) and languages.
4. **Generate Content**: The backend processes via LangChain agents; view results in the dashboard.
5. **Export & History**: Download as TXT/MD or browse past generations.

Example API Call (for testing):
curl -X POST "http://localhost:8000/api/generate"
-H "Content-Type: application/json"
-d '{
"video_url": "https://youtube.com/watch?v=example",
"platforms": ["linkedin", "twitter"],
"language": "en-ur"
}'

Response includes generated titles, descriptions, etc., with citations from brand memory.

## Development Workflow

- **Frontend**: Use `npm run dev` for hot-reloading; edit components in `src/components/`.
- **Backend**: Run with `uvicorn` for auto-reload; add endpoints in `app/routers/`.
- **Testing**: 
  - Backend: `pytest` in `/backend`
  - Frontend: `npm test`
- **LangChain Agents**: Customize in `/backend/agents/` (e.g., TranscriptionAgent, GeneratorAgent).
- **RAG Setup**: Brand memory vectors are stored per-user in ChromaDB; seed with sample posts via `/api/brand-memory`.

## Contributing

1. Fork the repo and create a feature branch (`git checkout -b feature/amazing-feature`).
2. Commit changes (`git commit -m 'Add some amazing feature'`).
3. Push to the branch (`git push origin feature/amazing-feature`).
4. Open a Pull Request.

We welcome contributions for new platforms, LLM integrations, or UI improvements!

## Testing

- **Unit Tests**: Run `pytest` in backend for API and agent coverage (>80% target).
- **Integration Tests**: Test full pipeline with sample videos.
- **E2E Tests**: Use Cypress in frontend (`npm run cypress`).
- **Performance**: Monitor latency for <30s video processing.

## Deployment

- **Local**: Docker Compose as above.
- **Production**:
  - Frontend: Vercel/Netlify (static export).
  - Backend: Heroku/Railway (with PostgreSQL add-on) or AWS ECS.
  - Database: Scale to PostgreSQL for multi-user.
  - Monitoring: Add Sentry for errors, Prometheus for metrics.
- **Scaling**: Use Celery for async tasks (video processing); Redis for queues.

Environment Variables for Production:
- `ENVIRONMENT=production`
- `SECRET_KEY=your_jwt_secret`
- Database and API keys as in dev.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built for CS4063 NLP Course Project (Development Track).
- Inspired by modern AI frameworks and creator economy needs.
- Special thanks to LangChain community and OpenAI for accessible APIs.

## Contact

For questions or collaborations, reach out via GitHub Issues or email: [your-contact@example.com].

---

*Nuvoletro: From one video to endless voices.*  
Version: 1.0.0 | Last Updated: November 2025
