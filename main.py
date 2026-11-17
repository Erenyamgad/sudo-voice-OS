import whisper
from pydub import AudioSegment
import threading
from flask import Flask, render_template, request, jsonify
from stt import speech_to_text
from executor import execute_command
from tts import speak
import speech_recognition as sr
import sys
import platform
import time
import os
from nlp_parser import parse_command

app = Flask(__name__)

#Load Local Whisper model once at startup for 100% offline transcription
print("[*] Loading local Whisper STT model ...")
whisper_model = whisper.load_model("base")
print("[*] Whisper STT model loaded and ready!")


@app.route("/")
def index():
   """Render the main web interface"""
   return render_template(
      "index.html",
       os_name="Ubuntu Linux",
       workspace="~/Desktop/sudo-voice-os"
   )

@app.route("/api/transcribe", methods=["POST"])
def api_transcribe():
   """Receive recorded audio from browser, cinvert to WAV, and transcribe."""
   if "audio" not in request.files:
     return jsonify({"error": "No audio received"})

   audio_file = request.files["audio"]
   webm_path = "recording.webm"
   wav_path = "recording.wav"

   audio_file.save(webm_path)

   try:
      # Convert browser WebM audio to 16kHz Mono WAV
      audio = AudioSegment.from_file(webm_path)
      audio = audio.set_channels(1).set_frame_rate(16000)
      audio.export(wav_path, format="wav")
      
      #Transcribe offline using local Whisper model
      result = whisper_model.transcribe(wav_path, language="en", fp16=False)
      text = result.get("text", "").strip()
      return jsonify({"text": text})
   except sr.UnknownValueError:
      return jsonify({"error": "No speech detected. The mic might be recording silence."})
   except sr.RequestError as e:
      return jsonify({"error": f"Google API Error: {e}"})
   except Exception as e:
      return jsonify({"error": f"Tech Error: {str(e)}"})
   finally:
      #Clean up temporary audio files
      for temp_file in (webm_path, wav_path):
         if os.path.exists(temp_file):
            os.remove(temp_file)

@app.route("/api/parse", methods=["POST"])
def api_parse():
   """Parse natural language text into a Linux terminal command."""
   data = request.json
   text = data.get("text", "")

   command = parse_command(text)

   return jsonify({
      "understood": True, 
      "intent": command,
      "args": "", 
      "command": command
   })

@app.route("/api/execute", methods=["POST"])
def api_execute():
   """ Execute the parsed command safely and trigger voice feedback."""
   data = request.json
   command_to_execute = data.get("intent", "")

   try:
      result = execute_command(command_to_execute)
      spoken_message = str(result)
      
      #Generate user-friendly voice feedback if command succeeded
      if not str(result).startswith("Error") and not str(result).startswith("An unexpected error"):
        if "firefox" in command_to_execute:
           spoken_message = "Opening Firefox browser."
        elif "settings" in command_to_execute or "control-center" in command_to_execute:
           spoken_message = "Opening settings."
        elif "gnome-calculator" in command_to_execute or "calculator" in command_to_execute:
           spoken_message = "Launching calculator."
        elif "ls" in command_to_execute:
           spoken_message = f"Here are the files {result}"
        elif "mkdir" in command_to_execute:
           folder_name = command_to_execute.replace("mkdir", "").strip()
           spoken_message = f"Folder {folder_name} created successfully."
        elif "touch" in command_to_execute:
           file_name = command_to_execute.replace("touch", "").strip()
           spoken_message = f"File {file_name} created successfully."
        elif "rm" in command_to_execute:
           target_name = command_to_execute.replace("rm", "").replace("-rf", "").replace("-rf", "").replace("-r", "").strip()
           spoken_message = f" Item {target_name} deleted successfully."
        elif "pwd" in command_to_execute:
           spoken_message = f"You are in {result}"
        elif "command executed successfully" in str(result):
           spoken_message = "Command executed successfully."
      # Speak response asynchronously without blocking UI
      threading.Thread(target=speak, args=(spoken_message,)).start()
      return jsonify({
         "ok": True,
         "command": command_to_execute,
         "output": spoken_message
      })
   except Exception as e:
      return jsonify({
         "ok": False,
         "command": command_to_execute,
         "output": str(e)
      })

if __name__ == "__main__":
   app.run(host="127.0.0.1", port=5000, debug=False)
