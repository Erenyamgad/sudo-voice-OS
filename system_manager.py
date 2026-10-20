import subprocess
import psutil


def show_system_info():
    print("\n=== System Information ===")

    cpu_usage = psutil.cpu_percent(interval=1)
    ram_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage("/").percent

    print(f"CPU Usage: {cpu_usage}%")
    print(f"RAM Usage: {ram_usage}%")
    print(f"Disk Usage: {disk_usage}%")


def show_processes():
    print("\n=== Running Processes ===")

    result = subprocess.run(
        ["ps", "-eo", "pid,user,comm"],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        print(result.stdout)
    else:
        print("Error showing processes:")
        print(result.stderr)