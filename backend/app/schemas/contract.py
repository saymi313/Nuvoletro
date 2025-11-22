from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

# --- INPUTS (What Frontend sends to Backend) ---

class VideoRequest(BaseModel):
    url: str
    platforms: List[str] = ["linkedin", "twitter"]
    language_style: str = "ur-en" # 'en', 'ur', or 'ur-en' (Roman Urdu)

class ContentEditRequest(BaseModel):
    content_id: int
    new_text: str

# --- OUTPUTS (What Backend sends to Frontend) ---

class ContentResponse(BaseModel):
    id: int
    platform: str
    body: str  # The generated text
    created_at: datetime

class ProjectResponse(BaseModel):
    id: int
    video_title: str
    youtube_url: str
    generated_content: List[ContentResponse]
    status: str # "processing", "completed", "failed"