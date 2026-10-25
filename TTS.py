import subprocess
from pathlib import Path

MODEL = Path.home() / "voice_os_audio" / "en_US-lessac-medium.onnx"
OUTPUT = Path("/tmp/voice_os_tts.wav")
DELAYED_OUTPUT = Path("/tmp/voice_os_tts_delayed.wav")


def speak(text):
    subprocess.run(
        [
            "python", "-m", "piper",
            "-m", str(MODEL),
            "-f", str(OUTPUT)
        ],
        input=text + "\n",
        text=True,
        check=True
    )

    subprocess.run(
        [
            "ffmpeg", "-y", "-i", str(OUTPUT),
            "-af", "adelay=1000|1000",
            str(DELAYED_OUTPUT)
        ],
        check=True
    )

    subprocess.run(
        ["paplay", str(DELAYED_OUTPUT)],
        check=True
    )


