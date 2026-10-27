"""
File & Application Management Module - Sudo Voice OS
Author: Mahmoud Hisham (352401058)
Week 4: Core File & Application Operations + JSON Command Mapping Integration
"""

import os
import shutil
import subprocess
import json
from pathlib import Path

# Path to the JSON command mapping file
COMMANDS_JSON_PATH = Path(__file__).parent / "commands.json"

# Whitelisted Linux desktop applications
APP_ALIASES = {
    "browser": "firefox",
    "firefox": "firefox",
    "text editor": "gedit",
    "editor": "gedit",
    "gedit": "gedit",
    "notepad": "gedit",
    "calculator": "gnome-calculator",
    "gnome-calculator": "gnome-calculator",
    "file manager": "nautilus",
    "files": "nautilus",
    "nautilus": "nautilus",
    "terminal": "gnome-terminal",
    "gnome-terminal": "gnome-terminal",
    "settings": "gnome-control-center",
    "gnome-control-center": "gnome-control-center",
}

# Protected paths that cannot be deleted
PROTECTED_PATHS = {"/", "/home", "/root", "/etc", "/usr", "/var", "/bin", "/sbin", "."}


def load_commands_config():
    """Loads the 20 core command definitions from commands.json."""
    if COMMANDS_JSON_PATH.exists():
        with open(COMMANDS_JSON_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"commands": []}


def _is_safe_path(target_path: str) -> bool:
    """Prevents accidental deletion or modification of critical system directories."""
    resolved = str(Path(target_path).resolve())
    return resolved not in PROTECTED_PATHS and target_path.strip() not in PROTECTED_PATHS


# ==========================================
# 1. FILE MANAGEMENT FUNCTIONS (Commands 1-12)
# ==========================================

def create_folder(folder_name: str) -> str:
    """CMD_01: Creates a new folder (matches main.py signature)."""
    try:
        os.makedirs(folder_name, exist_ok=True)
        msg = f"[+] Folder '{folder_name}' created successfully!"
        print(msg)
        return msg
    except Exception as e:
        msg = f"[-] Error creating folder '{folder_name}': {e}"
        print(msg)
        return msg


def remove_folder(folder_name: str) -> str:
    """CMD_02: Removes an empty directory safely."""
    if not _is_safe_path(folder_name):
        msg = f"[-] Security Error: Cannot remove protected path '{folder_name}'."
        print(msg)
        return msg
    try:
        os.rmdir(folder_name)
        msg = f"[+] Folder '{folder_name}' removed successfully!"
        print(msg)
        return msg
    except Exception as e:
        msg = f"[-] Error removing folder '{folder_name}': {e}"
        print(msg)
        return msg


def list_files(path: str = ".") -> str:
    """CMD_03: Lists all files and folders in the target directory (matches main.py signature)."""
    try:
        files = os.listdir(path)
        print(f"[*] Directory Files & Folders ({path}):")
        for f in files:
            print(f"   - {f}")
        return f"Found {len(files)} items in '{path}'."
    except Exception as e:
        msg = f"[-] Error listing files in '{path}': {e}"
        print(msg)
        return msg


def create_file(file_name: str) -> str:
    """CMD_04: Creates a new empty file."""
    try:
        Path(file_name).touch(exist_ok=True)
        msg = f"[+] File '{file_name}' created successfully!"
        print(msg)
        return msg
    except Exception as e:
        msg = f"[-] Error creating file '{file_name}': {e}"
        print(msg)
        return msg


def delete_file(file_name: str) -> str:
    """CMD_05: Deletes a specific file safely."""
    if not _is_safe_path(file_name):
        msg = f"[-] Security Error: Cannot delete protected path '{file_name}'."
        print(msg)
        return msg
    try:
        if os.path.isfile(file_name):
            os.remove(file_name)
            msg = f"[+] File '{file_name}' deleted successfully!"
        else:
            msg = f"[-] File '{file_name}' not found."
        print(msg)
        return msg
    except Exception as e:
        msg = f"[-] Error deleting file '{file_name}': {e}"
        print(msg)
        return msg


def rename_item(old_name: str, new_name: str) -> str:
    """CMD_06: Renames a file or folder."""
    try:
        os.rename(old_name, new_name)
        msg = f"[+] Renamed '{old_name}' to '{new_name}' successfully!"
        print(msg)
        return msg
    except Exception as e:
        msg = f"[-] Error renaming '{old_name}' to '{new_name}': {e}"
        print(msg)
        return msg


def copy_file(source: str, destination: str) -> str:
    """CMD_07: Copies a file from source to destination."""
    try:
        shutil.copy2(source, destination)
        msg = f"[+] Copied '{source}' to '{destination}' successfully!"
        print(msg)
        return msg
    except Exception as e:
        msg = f"[-] Error copying '{source}' to '{destination}': {e}"
        print(msg)
        return msg


def move_file(source: str, destination: str) -> str:
    """CMD_08: Moves a file or folder to a new location."""
    try:
        shutil.move(source, destination)
        msg = f"[+] Moved '{source}' to '{destination}' successfully!"
        print(msg)
        return msg
    except Exception as e:
        msg = f"[-] Error moving '{source}' to '{destination}': {e}"
        print(msg)
        return msg


def read_file(file_name: str) -> str:
    """CMD_09: Reads and prints the contents of a text file."""
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            content = f.read()
        print(f"[*] Content of '{file_name}':\n{content}")
        return content
    except Exception as e:
        msg = f"[-] Error reading file '{file_name}': {e}"
        print(msg)
        return msg


def search_files(query: str, search_path: str = ".") -> str:
    """CMD_10: Searches for files matching the query string."""
    try:
        matches = []
        for root, dirs, files in os.walk(search_path):
            for item in files + dirs:
                if query.lower() in item.lower():
                    matches.append(os.path.join(root, item))
        print(f"[*] Search results for '{query}':")
        for m in matches:
            print(f"   - {m}")
        return f"Found {len(matches)} match(es) for '{query}'."
    except Exception as e:
        msg = f"[-] Error searching for '{query}': {e}"
        print(msg)
        return msg


def get_current_directory() -> str:
    """CMD_11: Prints and returns the current working directory."""
    cwd = os.getcwd()
    print(f"[*] Current Working Directory: {cwd}")
    return cwd


def get_file_info(file_name: str) -> str:
    """CMD_12: Displays size and modification details of a file."""
    try:
        stats = os.stat(file_name)
        info = f"[*] File: {file_name} | Size: {stats.st_size} bytes"
        print(info)
        return info
    except Exception as e:
        msg = f"[-] Error getting info for '{file_name}': {e}"
        print(msg)
        return msg


# =================================================
# 2. APPLICATION MANAGEMENT FUNCTIONS (Commands 13-20)
# =================================================

def open_application(app_name: str) -> str:
    """CMD_13 to CMD_18: Launches a whitelisted Linux desktop application."""
    key = app_name.lower().strip()
    binary = APP_ALIASES.get(key)

    if not binary:
        msg = f"[-] Application '{app_name}' is not in the allowed applications list."
        print(msg)
        return msg

    try:
        subprocess.Popen(
            [binary],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            start_new_session=True
        )
        msg = f"[+] Application '{binary}' launched successfully!"
        print(msg)
        return msg
    except FileNotFoundError:
        msg = f"[-] Application '{binary}' is not installed on this system."
        print(msg)
        return msg
    except Exception as e:
        msg = f"[-] Error launching '{binary}': {e}"
        print(msg)
        return msg


def close_application(app_name: str) -> str:
    """CMD_19: Closes a running application safely by name."""
    key = app_name.lower().strip()
    binary = APP_ALIASES.get(key, key)

    if binary not in APP_ALIASES.values():
        msg = f"[-] Cannot close '{app_name}': Not a managed user application."
        print(msg)
        return msg

    try:
        subprocess.run(["pkill", "-f", binary], check=False)
        msg = f"[+] Sent close signal to '{binary}'."
        print(msg)
        return msg
    except Exception as e:
        msg = f"[-] Error closing '{binary}': {e}"
        print(msg)
        return msg


def list_running_apps() -> str:
    """CMD_20: Lists currently running managed applications."""
    try:
        result = subprocess.run(
            ["ps", "-e", "-o", "comm="],
            capture_output=True,
            text=True,
            check=True
        )
        running_procs = set(result.stdout.splitlines())
        managed_binaries = set(APP_ALIASES.values())
        active_apps = sorted(running_procs.intersection(managed_binaries))

        print("[*] Active Managed Applications:")
        if active_apps:
            for app in active_apps:
                print(f"   - {app}")
            return f"Active applications: {', '.join(active_apps)}"
        else:
            print("   (No managed GUI applications currently running)")
            return "No managed GUI applications currently running."
    except Exception as e:
        msg = f"[-] Error listing running applications: {e}"
        print(msg)
        return msg


if __name__ == "__main__":
    print("=== Testing File & Application Manager (Week 4) ===")
    config = load_commands_config()
    print(f"[*] Loaded {len(config.get('commands', []))} core commands from commands.json")
    get_current_directory()
    list_files(".")