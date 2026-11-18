import subprocess
import os
# Allowed commands list for security
ALLOWED_COMMANDS = ["ls", "pwd", "date", "rm", "whoami", "mkdir", "firefox", "gnome-calculator", "gedit",
"nautilus", "gnome-terminal", "gnome-control-center", "pkill", "ps", "touch", "cat"]

def execute_command(command_str):
    """
    Executes the given command securely on the Linux terminal.
    """
    command_str = str(command_str).strip()
    if command_str.endswith("&"):
        command_str = command_str[:-1].strip()
    cmd_parts = command_str.strip().split()

    if not cmd_parts:
        return "Error: No command provided."

    base_command = cmd_parts[0]

    # Security check: verify if the command is allowed
    if base_command not in ALLOWED_COMMANDS:
        return f"Error: Command '{base_command}' is not allowed for security reasons."
    try:
        if base_command in ["firefox", "gnome-calculator", "gedit", "nautilus", "gnome-terminal", "gnome-control-center"]:
            subprocess.Popen(cmd_parts, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            return f"Executing {base_command}"
        result = subprocess.run(cmd_parts, capture_output=True, text=True, check=True)
        output = result.stdout.strip() if result.stdout else "Command executed successfully."
        return output
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"

if __name__ == "__main__":
    print("--- Testing 'pwd' execution ---")
    print(execute_command("pwd"))
