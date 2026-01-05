from fastapi import FastAPI
from fastapi.responses import FileResponse
import sys
import uuid

# إضافة مجلد kokoro لمسار بايثون
sys.path.append("./kokoro")

from kokoro import KPipeline

app = FastAPI()

# تهيئة Kokoro
pipeline = KPipeline(lang_code="a")  # a = English (تعمل بدون مشاكل)

@app.get("/")
def root():
    return {"status": "Kokoro TTS is running"}

@app.get("/tts")
def tts(text: str):
    # اسم ملف الصوت
    output_file = f"/tmp/{uuid.uuid4()}.wav"

    # توليد الصوت
    audio = pipeline(text)
    audio.save(output_file)

    return FileResponse(
        output_file,
        media_type="audio/wav",
        filename="speech.wav"
    )
