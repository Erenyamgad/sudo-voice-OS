Sound-to-Text 

Overview

This project is a Python-based speech-to-text application. It records audio from a microphone for 5 seconds and uses OpenAI Whisper to convert spoken English into text.

Features

- Records audio using a microphone.
- Saves the recording as a WAV file.
- Uses the Whisper Base model for speech recognition.
- Displays the recognized text in the terminal.
- Handles errors during recording and transcription.

Technologies Used

- Python
- PyAudio
- OpenAI Whisper
- Wave module

Requirements

- Python
- PyAudio
- OpenAI Whisper
- A working microphone
- FFmpeg, as required by Whisper

Installation

Install the required Python libraries:

pip install -r requirements.txt

Make sure FFmpeg is installed on your system.

How to Run

Run the following command in the terminal:

python sst.py

Speak in English when prompted. The application records audio for 5 seconds and then displays the recognized text.

Output

The recorded audio is saved as "recording.wav", and the recognized text is displayed in the terminal.

Notes

The application currently supports English speech recognition and uses the Whisper Base model.
