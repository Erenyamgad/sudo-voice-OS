import pyaudio
import wave
import whisper
import os

# Audio Recording Settings
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
SECONDS = 5
AUDIO_FILE = "recording.wav"


def record_audio():
    audio = pyaudio.PyAudio()
    stream = None

    try:
        print("\nRecording... Speak now!")

        stream = audio.open(
            format=FORMAT,
            channels=CHANNELS,
            rate=RATE,
            input=True,
            frames_per_buffer=CHUNK
        )

        frames = []

        for _ in range(int(RATE / CHUNK * SECONDS)):
            data = stream.read(
                CHUNK,
                exception_on_overflow=False
            )
            frames.append(data)

        print("Recording finished!")

        stream.stop_stream()
        stream.close()
        stream = None

        with wave.open(AUDIO_FILE, "wb") as file:
            file.setnchannels(CHANNELS)
            file.setsampwidth(audio.get_sample_size(FORMAT))
            file.setframerate(RATE)
            file.writeframes(b"".join(frames))

        print(f"Audio saved to {AUDIO_FILE}")

    finally:
        if stream is not None:
            stream.close()

        audio.terminate()


def speech_to_text():
    try:
        print("\nLoading Whisper model...")
        model = whisper.load_model("base")

        record_audio()

        print("\nTranscribing audio...")

        result = model.transcribe(
            AUDIO_FILE,
            language="en",
            fp16=False
        )

        recognized_text = result["text"].strip()

        print("\nRecognized Text:")
        print(recognized_text or "No speech recognized.")

        return recognized_text

    except Exception as error:
        print(f"Error: {error}")
        return ""


if __name__ == "__main__":
    command_text = speech_to_text()

    

