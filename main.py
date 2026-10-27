"""
Main Entry Point - Sudo Voice OS
Updated to integrate Mahmoud Hisham's file_app_manager.py with Ereny's nlp_parser.py.
"""

import sys
import platform
from nlp_parser import parse_command
from file_app_manager import (
    create_folder,
    remove_folder,
    list_files,
    create_file,
    delete_file,
    rename_item,
    copy_file,
    move_file,
    read_file,
    search_files,
    get_current_directory,
    get_file_info,
    open_application,
    close_application,
    list_running_apps,
)


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