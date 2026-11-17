# Text-to-Speech (TTS) Module

## 1. Overview

This module converts English text into speech using Piper TTS and plays the generated audio locally on Ubuntu. It works offline using a local voice model.

## 2. Tools and Technologies

- **Python 3:** Main programming language.
- **Piper TTS 1.8.0:** Converts text into speech using a neural ONNX voice model.
- **Subprocess:** Executes Piper, FFmpeg, and paplay commands.
- **Threading:** Uses `threading.Lock` to prevent overlapping TTS operations.
- **Pathlib:** Handles file paths.
- **FFmpeg:** Adds 500 milliseconds of silence and configures the audio format.
- **paplay:** Plays the generated WAV audio.

## 3. Requirements and Installation

Required tools:
- Ubuntu
- Python 3
- FFmpeg
- paplay (`pulseaudio-utils`)
- Piper TTS 1.8.0

Install the system packages:

```bash
sudo apt update
sudo apt install ffmpeg pulseaudio-utils python3-venv
```

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install Piper TTS:

```bash
pip install -r requirements.txt
```

The `requirements.txt` file contains:

```text
piper-tts==1.8.0
```

## 4. Voice Model Setup

The following files are required:

- `en_US-lessac-medium.onnx`
- `en_US-lessac-medium.onnx.json`

They are not included in the GitHub repository because of their large size. They must be downloaded separately and placed inside:

```text
~/voice_os_audio/
```

## 5. Running the Test

After activating the virtual environment and preparing the voice model, run:

```bash
python test_tts.py
```

The test script uses five example sentences to check the TTS functionality.

## 6. Main Function and Implementation

The main function is:

```python
speak(text)
```

It performs the following operations:

1. Checks and cleans the input text.
2. Uses Piper TTS to generate speech.
3. Saves the generated audio as a WAV file.
4. Uses FFmpeg with `adelay=500|500` to add 500 milliseconds of silence at the beginning.
5. Uses `-ar 22050` to set the sample rate to 22050 Hz.
6. Uses `-ac 1` to set the audio output to mono (one channel).
7. Uses `paplay` to play the final audio.

The function also uses a thread lock to prevent overlapping playback and exception handling to report runtime errors.

## 7. Project Status

The TTS module currently works independently and supports English text-to-speech conversion. Integration with the other Voice OS components will be completed later.
