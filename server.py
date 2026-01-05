from fastapi import FastAPI
from pydantic import BaseModel
import torch

from kokoro.pipeline import KPipeline

app = FastAPI()

# تحميل نموذج Kokoro مرة واحدة عند تشغيل السيرفر
pipeline = KPipeline(lang="en")

class TTSRequest(BaseModel):
    text: str

@app.post("/tts")
def tts(request: TTSRequest):
    audio = pipeline(request.text)

    # حفظ الصوت مؤقتًا
    output_path = "output.wav"
    audio.save(output_path)

    return {
        "status": "success",
        "file": output_path
    }

@app.get("/")
def root():
    return {"message": "Kokoro TTS is running"}
