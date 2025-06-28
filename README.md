# Text-to-Video Generator (Open-Source Models)

This project provides a text-to-video generation API using open-source models and diffusion-based techniques.

## Features

- Generate short videos from natural language prompts
- Easy-to-use REST API via FastAPI
- Placeholder integration for popular open-source text-to-video models (e.g., CogVideo, latent diffusion)
- Video frame processing and assembly utilities

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/yourname/text-to-video-generator.git
cd text-to-video-generator
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Download or prepare your model checkpoint

- Download pre-trained model from: https://huggingface.co/THUDM/CogVideoX-5b
- Place them in the models/ directory

### 4. Run the FastAPI server
```bash
uvicorn app.main:app --reload
```

### 5. Generate video via API
POST to /generate_video with JSON body:
```json
{
  "prompt": "a cat playing piano in a jazz club",
  "length_seconds": 5
}
```
The API returns a path to the generated video file.

### Notes
- The current implementation uses placeholders for model loading and video generation.
- Video generation is computationally intensive; use GPU for best performance.
