import sys
import os
import platform
from nlp_parser import parse_command

def create_folder(folder_name):
  import os
  os.makedirs(folder_name, exist_ok=True)
  print(f"[+] Folder '{folder_name}' created successfully!")

def list_files():
  files = os.listdir('.')
  print("[*] Current Directory Files & Folders:")
  for f in files:
    print(f"   -{f}")

def show_system_info():
  print(f"[*] System: {platform.system()} {platform.release()}")
  print(f"[*] Machine: {platform.machine()}")
  print(f"[*] Python Version: {platform.python_version()}")


def main():
  if len(sys.argv) > 1:
    user_input = " ".join(sys.argv[1:])
    print(f"[*] User Input: {user_input}")

    command_to_execute = parse_command(user_input)
    print(f"[*] Executing: {command_to_execute}")

    exec(command_to_execute)
  else:
    print("Please provide a command for the Sudo Voice OS.")

if __name__ == "__main__":
  main()
