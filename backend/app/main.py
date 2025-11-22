from fastapi import FastAPI
from app.models import tables
from app.schemas import contract

app = FastAPI(title="Nuvoletro API", version="0.1.0")

@app.get("/")
def read_root():
    return {"message": "Nuvoletro Backend is Running!", "status": "healthy"}

@app.get("/health")
def health_check():
    return {"database": "disconnected", "redis": "disconnected"}

# --- NEW: Mock Endpoint to visualize the Contract ---
@app.post("/generate", response_model=contract.ProjectResponse)
def generate_content_mock(request: contract.VideoRequest):
    """
    MOCK ENDPOINT: This shows the Frontend team what the Input/Output looks like.
    It doesn't actually do anything yet.
    """
    return {
        "id": 101,
        "video_title": "Mock Video Title",
        "youtube_url": request.url,
        "status": "processing",
        "generated_content": []
    }