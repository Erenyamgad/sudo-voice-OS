# Text-to-Speech (TTS)

## 1. Overview

This module converts text into speech using Piper TTS and plays the generated audio.

## 2. Requirements

* Ubuntu
* Python
* Piper TTS version 1.8.0
* FFmpeg
* paplay (provided by `pulseaudio-utils` on Ubuntu)
* Piper voice model and its JSON configuration file

## 3. Installation

### Step 1: Install the required system packages

Open the Ubuntu Terminal and run:

```bash
sudo apt update
sudo apt install ffmpeg pulseaudio-utils
```

### Step 2: Set up the Python environment

Open the project directory and create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install Piper TTS:

```bash
pip install -r requirements.txt
```

### Step 3: Obtain the Voice Model Files

The voice model files are not included in this GitHub repository because of their relatively large size.

To run the TTS module, obtain the following files separately and place them in the project directory:

* `en_US-lessac-medium.onnx`
* `en_US-lessac-medium.onnx.json`

Both files are required by Piper TTS to generate speech.


## 4. Running the Test

With the virtual environment activated, run:

```bash
python test_tts.py
```

The test script uses five example sentences to check that the text-to-speech module works correctly.

## 5. Main Function

The main function is:

```python
speak(text)
```

It receives a text string and performs the following operations:

1. Uses Piper TTS to convert the text into speech.
2. Saves the generated audio to a WAV file.
3. Uses FFmpeg to add one second of silence at the beginning of the audio.
4. Plays the resulting audio using `paplay`.

## 6. Project Status

The TTS module currently works independently and can speak English text. Integration with the other Voice OS project components will be completed later.
