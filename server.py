from flask import Flask, request, send_file
import subprocess
import os
import uuid

app = Flask(__name__)

@app.route("/")
def home():
    return "Piper TTS is running ✅"

@app.route("/tts", methods=["POST"])
def tts():
    text = request.json.get("text", "")
    if not text:
        return {"error": "No text provided"}, 400

    output_file = f"/tmp/{uuid.uuid4()}.wav"

    cmd = [
        "piper",
        "--model", "en_US-lessac-medium",
        "--output_file", output_file
    ]

    process = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    process.stdin.write(text.encode("utf-8"))
    process.stdin.close()
    process.wait()

    return send_file(output_file, mimetype="audio/wav")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
