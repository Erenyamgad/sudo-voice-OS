import subprocess
import threading
from pathlib import Path

MODEL = Path.home() / "voice_os_audio" / "en_US-lessac-medium.onnx"
OUTPUT = Path("/tmp/voice_os_tts.wav")
FINAL_OUTPUT = Path("/tmp/voice_os_tts_final.wav")

tts_lock = threading.Lock()

def speak(text):
    if not text or not str(text).strip():
        return

    with tts_lock:
        try:
            clean_text = str(text).replace("/", " ").replace("-", " ").replace("_", " ").replace("\n", " ").strip()

            subprocess.run(
                [
                    "python", "-m", "piper",
                    "-m", str(MODEL),
                    "-f", str(OUTPUT)
                ],
                input=clean_text + "\n",
                text=True,
                check=True
            )

            subprocess.run(
                [
                    "ffmpeg", "-y", "-i", str(OUTPUT),
                    "-af", "adelay=500|500",
                    "-ar", "22050", "-ac", "1",
                    str(FINAL_OUTPUT)
                ],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                check=True
            )

            subprocess.run(
                ["paplay", "--latency-msec=500", str(FINAL_OUTPUT)],
                check=True
            )

        except Exception as e:
            print(f"[-] TTS Error: {e}")
