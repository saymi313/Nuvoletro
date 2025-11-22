from sqlalchemy import Column, Integer, String, ForeignKey, Text, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    
    projects = relationship("Project", back_populates="owner")

class Project(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    youtube_url = Column(String)
    video_title = Column(String)
    transcript_text = Column(Text)  # The raw text from YouTube
    created_at = Column(DateTime, default=datetime.utcnow)

    owner = relationship("User", back_populates="projects")
    generated_content = relationship("GeneratedContent", back_populates="project")

class GeneratedContent(Base):
    __tablename__ = "generated_content"
    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("projects.id"))
    platform = Column(String) # e.g., "linkedin", "twitter", "veo_prompt"
    content_body = Column(Text) # The AI output
    created_at = Column(DateTime, default=datetime.utcnow)
    
    project = relationship("Project", back_populates="generated_content")