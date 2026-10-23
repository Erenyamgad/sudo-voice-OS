import sys

def parse_command(spoken_text):
  spoken_text = spoken_text.lower().strip()

  if "make directory" in spoken_text or "create folder" in spoken_text:
    parts = spoken_text.split()
    folder_name = parts[-1] if len(parts) > 0 else "new_folder"
    return f"create_folder('{folder_name}')"

  elif "list files" in spoken_text or "show files" in spoken_text:
    return "list_files()"

  elif "system info" in spoken_text or "system status" in spoken_text:
    return "show_system_info()"

  else:
    return f"print('Intent not recognized for: {spoken_text}')"

if __name__ == "__main__":
  if len(sys.argv) > 1:
    text_input = " ".join(sys.argv[1:])
    print(f"Parsed Command: {parse_command(text_input)}")
  else:
    print("Please provide text to pasre.")

