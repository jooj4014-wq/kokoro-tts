import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(BASE_DIR, "kokoro"))

from fastapi import FastAPI, Query
from fastapi.responses import FileResponse

from kokoro.pipeline import KPipeline

app = FastAPI()

pipeline = KPipeline(lang="en")

@app.get("/tts")
def tts(text: str = Query(...)):
    output_path = "output.wav"

    pipeline(
        text,
        voice="af",
        speed=1.0,
        output_file=output_path
    )

    return FileResponse(output_path, media_type="audio/wav")
