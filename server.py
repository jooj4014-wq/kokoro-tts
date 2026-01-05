import sys
import os

# إضافة مسار kokoro الصحيح
sys.path.append(os.path.join(os.path.dirname(__file__), "kokoro"))

from fastapi import FastAPI, Query
from fastapi.responses import FileResponse

from kokoro.pipeline import KPipeline

app = FastAPI()

pipeline = KPipeline(lang="en")

@app.get("/tts")
def tts(text: str = Query(...)):
    audio_path = "output.wav"

    pipeline(
        text,
        voice="af",
        speed=1.0,
        output_file=audio_path
    )

    return FileResponse(audio_path, media_type="audio/wav", filename="output.wav")
