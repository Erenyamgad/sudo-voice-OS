def parse_command(text_command):
  text = text_command.lower().strip()

  if "open brower" in text :
    return  "Executing: firefox"
  elif "shutdown" in text :
    return "Executing: shutdown now"
  elif "list files" in text:
   return "Executing: ls -la"
  else:
    return f"command received: '{text_command}'"

if __name__ == "__main__":
 test_input = "open browser"
 print(f"Input: {test_input}")
 print(f"Output: {parse_command(test_input)}")
