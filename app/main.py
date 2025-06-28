from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.video_generator import TextToVideoGenerator

app = FastAPI()
video_generator = TextToVideoGenerator()

class GenerateRequest(BaseModel):
    prompt: str
    length_seconds: int = 5

@app.post("/generate_video")
def generate_video(req: GenerateRequest):
    if not req.prompt:
        raise HTTPException(status_code=400, detail="Prompt cannot be empty")

    video_path = video_generator.generate_video(req.prompt, req.length_seconds)
    return {"video_path": video_path, "message": "Video generated successfully"}
