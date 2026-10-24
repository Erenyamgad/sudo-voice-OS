import subprocess
import os

# Allowed commands list for security
ALLOWED_COMMANDS = ["ls", "pwd", "date", "whoami", "mkdir"]

def execute_command(command_str):
    """
    Executes the given command securely on the Linux terminal.
    """
    cmd_parts = command_str.strip().split()
    
    if not cmd_parts:
        return "Error: No command provided."
    
    base_command = cmd_parts[0]
    
    # Security check: verify if the command is allowed
    if base_command not in ALLOWED_COMMANDS:
        return f"Error: Command '{base_command}' is not allowed for security reasons."
    
    try:
        result = subprocess.run(
            cmd_parts, 
            capture_output=True, 
            text=True, 
            check=True
        )
        return result.stdout if result.stdout else "Command executed successfully with no output."
        
    except subprocess.CalledProcessError as e:
        return f"Execution error: {e.stderr}"
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"

if __name__ == "__main__":
    print("--- Testing 'pwd' execution ---")
    print(execute_command("pwd"))