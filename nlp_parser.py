"""
Intent Parser & Command Mapper - Sudo Voice OS
Updated for Week 4: Maps natural spoken language to the 20 core File, App & System commands.
Compatible with Ereny's main.py and Mahmoud's file_app_manager.py.
"""
from thefuzz import fuzz
import sys
import json
from pathlib import Path

COMMANDS_JSON_PATH = Path(__file__).parent / "commands.json"


def load_commands_json():
    """Loads the 20 core commands from commands.json if available."""
    if COMMANDS_JSON_PATH.exists():
        with open(COMMANDS_JSON_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"commands": []}

def is_match(keywords, text):
    for word in keywords:
        if word in text:
           return True
        if fuzz.ratio(word, text) >= 90:
           return True
    return False

def parse_command(spoken_text: str) -> str:
    """
    Translates spoken text into executable Python function calls for main.py.
    Covers the 20 core File & Application Management commands plus system info.
    """
    spoken_text = spoken_text.lower().strip()
    words = spoken_text.split()

    # 1. Create Folder (CMD_01)
    if is_match(["make directory", "create folder", "new folder"], spoken_text):
        folder_name = words[-1] if len(words) > 2 else "new_folder"
        return f"mkdir {folder_name}"

    # 2. Remove Folder (CMD_02)
    elif is_match([ "delete folder", "remove directory", "remove folder"], spoken_text):
        folder_name = words[-1] if len(words) > 2 else "new_folder"
        return f"rm -r {folder_name}"

    # 3. List Files (CMD_03)
    elif is_match(["list files", "show files", "what files are here"], spoken_text):
        return "ls"

    # 4. Create File (CMD_04)
    elif is_match(["create file", "make file", "new file", "touch file"], spoken_text):
        file_name = words[-1] if len(words) > 2 else "new_file.txt"
        return f"touch {file_name}"

    # 5. Delete File (CMD_05)
    elif is_match(["delete file", "remove file", "erase file"], spoken_text):
        file_name = words[-1] if len(words) > 2 else ""
        if not file_name:
          return "echo 'Error: Please specify a file name to delete.'"
        return f"rm {file_name}"

    # 6. Rename File/Folder (CMD_06) - e.g. "rename file old.txt to new.txt"
    elif is_match(["rename"], spoken_text):
        if "to" in words:
            to_idx = words.index("to")
            old_name = words[to_idx - 1] if to_idx > 0 else "old_item"
            new_name = words[to_idx + 1] if to_idx + 1 < len(words) else "new_item"
            return f"mv {old_name} {new_name}"
        elif len(words) >= 3:
            return f"mv {words[-2]} {words[-1]}"

    # 7. Copy File (CMD_07) - e.g. "copy file a.txt to b.txt"
    elif is_match(["copy file", "duplicate file"], spoken_text):
        if "to" in words:
            to_idx = words.index("to")
            src = words[to_idx - 1]
            dst = words[to_idx + 1] if to_idx + 1 < len(words) else "copy_" + src
            return f"cp {src} {dst}"

    # 8. Move File (CMD_08) - e.g. "move file a.txt to folder"
    elif is_match(["move file", "transfer file"], spoken_text):
        if "to" in words:
            to_idx = words.index("to")
            src = words[to_idx - 1]
            dst = words[to_idx + 1] if to_idx + 1 < len(words) else "."
            return f"mv {src} {dst}"

    # 9. Read File (CMD_09)
    elif is_match(["read file", "show file content", "cat file"], spoken_text):
        file_name = words[-1] if len(words) > 2 else ""
        if not file_name:
          return "echo 'Error: Please specify a file name to read'"
        return f"cat {file_name}"

    # 10. Search Files (CMD_10)
    elif is_match(["find file", "search file", "locate file"], spoken_text):
        query = words[-1] if len(words) > 2 else ""
        return f"find . -name {query}"

    # 11. Current Directory (CMD_11)
    elif is_match(["current directory", "where am i", "print working directory"], spoken_text):
        return "pwd"

    # 12. File Info / Size (CMD_12)
    elif is_match(["file size", "file info", "file details"], spoken_text):
        file_name = words[-1] if len(words) > 2 else ""
        return f"ls -l {file_name}"

    # 13. Open Browser (CMD_13)
    elif is_match(["open browser", "launch browser", "open firefox"], spoken_text):
        return "firefox &"

    # 14. Open Text Editor (CMD_14)
    elif is_match(["open text editor", "open editor", "launch gedit", "open notepad"], spoken_text):
        return "gedit &"

    # 15. Open Calculator (CMD_15)
    elif is_match(["open calculator", "launch calculator", "start calculator"], spoken_text):
        return "gnome-calculator &"

    # 16. Open File Manager (CMD_16)
    elif is_match(["open file manager", "open files", "open nautilus"], spoken_text):
        return "nautilus &"

    # 17. Open Terminal (CMD_17)
    elif is_match(["open terminal", "launch terminal",  "new terminal"], spoken_text):
        return "gnome-terminal &"

    # 18. Open Settings (CMD_18)
    elif is_match(["open settings", "system settings", "control center"], spoken_text):
        return "gnome-control-center &"

    # 19. Close Application (CMD_19)
    elif is_match(["close ", "kill app"], spoken_text):
        app_target = words[-1] if len(words) > 1 else ""
        return f"pkill {app_target}"

    # 20. List Running Applications (CMD_20)
    elif is_match(["running applications", "list running apps", "what apps are open", "running"], spoken_text):
        return "ps"

    # System Info (from Ereny's initial main.py)
    elif is_match(["system info", "system status"], spoken_text):
        return "uname -a"

    else:
        return f"print('Intent not recognized for: {spoken_text}')"


if __name__ == "__main__":
    if len(sys.argv) > 1:
        text_input = " ".join(sys.argv[1:])
        print(f"Parsed Command: {parse_command(text_input)}")
    else:
        print("Please provide text to parse.")
