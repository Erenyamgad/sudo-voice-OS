"""
Intent Parser & Command Mapper - Sudo Voice OS
Updated for Week 4: Maps natural spoken language to the 20 core File, App & System commands.
Compatible with Ereny's main.py and Mahmoud's file_app_manager.py.
"""

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


def parse_command(spoken_text: str) -> str:
    """
    Translates spoken text into executable Python function calls for main.py.
    Covers the 20 core File & Application Management commands plus system info.
    """
    spoken_text = spoken_text.lower().strip()
    words = spoken_text.split()

    # 1. Create Folder (CMD_01)
    if "make directory" in spoken_text or "create folder" in spoken_text or "new folder" in spoken_text:
        folder_name = words[-1] if len(words) > 2 else "new_folder"
        return f"create_folder('{folder_name}')"

    # 2. Remove Folder (CMD_02)
    elif "delete folder" in spoken_text or "remove directory" in spoken_text or "remove folder" in spoken_text:
        folder_name = words[-1] if len(words) > 2 else "new_folder"
        return f"remove_folder('{folder_name}')"

    # 3. List Files (CMD_03)
    elif "list files" in spoken_text or "show files" in spoken_text or "what files are here" in spoken_text:
        return "list_files()"

    # 4. Create File (CMD_04)
    elif "create file" in spoken_text or "make file" in spoken_text or "new file" in spoken_text or "touch file" in spoken_text:
        file_name = words[-1] if len(words) > 2 else "new_file.txt"
        return f"create_file('{file_name}')"

    # 5. Delete File (CMD_05)
    elif "delete file" in spoken_text or "remove file" in spoken_text or "erase file" in spoken_text:
        file_name = words[-1] if len(words) > 2 else ""
        return f"delete_file('{file_name}')"

    # 6. Rename File/Folder (CMD_06) - e.g. "rename file old.txt to new.txt"
    elif "rename" in spoken_text:
        if "to" in words:
            to_idx = words.index("to")
            old_name = words[to_idx - 1] if to_idx > 0 else "old_item"
            new_name = words[to_idx + 1] if to_idx + 1 < len(words) else "new_item"
            return f"rename_item('{old_name}', '{new_name}')"
        elif len(words) >= 3:
            return f"rename_item('{words[-2]}', '{words[-1]}')"

    # 7. Copy File (CMD_07) - e.g. "copy file a.txt to b.txt"
    elif "copy file" in spoken_text or "duplicate file" in spoken_text:
        if "to" in words:
            to_idx = words.index("to")
            src = words[to_idx - 1]
            dst = words[to_idx + 1] if to_idx + 1 < len(words) else "copy_" + src
            return f"copy_file('{src}', '{dst}')"

    # 8. Move File (CMD_08) - e.g. "move file a.txt to folder"
    elif "move file" in spoken_text or "transfer file" in spoken_text:
        if "to" in words:
            to_idx = words.index("to")
            src = words[to_idx - 1]
            dst = words[to_idx + 1] if to_idx + 1 < len(words) else "."
            return f"move_file('{src}', '{dst}')"

    # 9. Read File (CMD_09)
    elif "read file" in spoken_text or "show file content" in spoken_text or "cat file" in spoken_text:
        file_name = words[-1] if len(words) > 2 else ""
        return f"read_file('{file_name}')"

    # 10. Search Files (CMD_10)
    elif "find file" in spoken_text or "search file" in spoken_text or "locate file" in spoken_text:
        query = words[-1] if len(words) > 2 else ""
        return f"search_files('{query}')"

    # 11. Current Directory (CMD_11)
    elif "current directory" in spoken_text or "where am i" in spoken_text or "print working directory" in spoken_text:
        return "get_current_directory()"

    # 12. File Info / Size (CMD_12)
    elif "file size" in spoken_text or "file info" in spoken_text or "file details" in spoken_text:
        file_name = words[-1] if len(words) > 2 else ""
        return f"get_file_info('{file_name}')"

    # 13. Open Browser (CMD_13)
    elif "open browser" in spoken_text or "launch browser" in spoken_text or "open firefox" in spoken_text:
        return "open_application('firefox')"

    # 14. Open Text Editor (CMD_14)
    elif "open text editor" in spoken_text or "open editor" in spoken_text or "launch gedit" in spoken_text or "open notepad" in spoken_text:
        return "open_application('gedit')"

    # 15. Open Calculator (CMD_15)
    elif "open calculator" in spoken_text or "launch calculator" in spoken_text or "start calculator" in spoken_text:
        return "open_application('gnome-calculator')"

    # 16. Open File Manager (CMD_16)
    elif "open file manager" in spoken_text or "open files" in spoken_text or "open nautilus" in spoken_text:
        return "open_application('nautilus')"

    # 17. Open Terminal (CMD_17)
    elif "open terminal" in spoken_text or "launch terminal" in spoken_text or "new terminal" in spoken_text:
        return "open_application('gnome-terminal')"

    # 18. Open Settings (CMD_18)
    elif "open settings" in spoken_text or "system settings" in spoken_text or "control center" in spoken_text:
        return "open_application('gnome-control-center')"

    # 19. Close Application (CMD_19)
    elif "close " in spoken_text or "kill app" in spoken_text:
        app_target = words[-1] if len(words) > 1 else ""
        return f"close_application('{app_target}')"

    # 20. List Running Applications (CMD_20)
    elif "running applications" in spoken_text or "list running apps" in spoken_text or "what apps are open" in spoken_text:
        return "list_running_apps()"

    # System Info (from Ereny's initial main.py)
    elif "system info" in spoken_text or "system status" in spoken_text:
        return "show_system_info()"

    else:
        return f"print('Intent not recognized for: {spoken_text}')"


if __name__ == "__main__":
    if len(sys.argv) > 1:
        text_input = " ".join(sys.argv[1:])
        print(f"Parsed Command: {parse_command(text_input)}")
    else:
        print("Please provide text to parse.")