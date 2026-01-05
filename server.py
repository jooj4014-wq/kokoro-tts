from fastapi import FastAPI, Query
from fastapi.responses import FileResponse
import tempfile
import os

from kokoro import KPipeline

app = FastAPI()

pipeline = KPipeline(lang="en")


@app.get("/")
def root():
    return {"status": "ok", "engine": "kokoro-tts"}


@app.get("/tts")
def tts(
    text: str = Query(..., min_length=1),
    voice: str = Query("af")
):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as f:
        output_path = f.name

    pipeline(
        text,
        voice=voice,
        output_file=output_path
    )

    return FileResponse(
        output_path,
        media_type="audio/wav",
        filename="speech.wav"
    )
