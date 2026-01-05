from fastapi import FastAPI
from fastapi.responses import FileResponse
import uuid
import os
from kokoro import Kokoro

app = FastAPI()

os.makedirs("audio", exist_ok=True)
tts = Kokoro()

@app.post("/tts")
async def tts_api(data: dict):
    text = data["text"]
    filename = f"audio/{uuid.uuid4()}.wav"
    tts.tts(text, filename)
    return {
        "audio_url": f"/audio/{os.path.basename(filename)}"
    }

@app.get("/audio/{file}")
def get_audio(file: str):
    return FileResponse(f"audio/{file}")
