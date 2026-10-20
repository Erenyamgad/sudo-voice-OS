import subprocess


def open_application():
    print("\n=== Open Application ===")
    print("1. Firefox")

    choice = input("Choose an application to open: ")

    if choice == "1":
        try:
            subprocess.Popen(["firefox"])
            print("Firefox opening requested.")
        except OSError as error:
            print(f"Error opening Firefox: {error}")
    else:
        print("Invalid choice.")


def close_application():
    print("\n=== Close Application ===")
    print("1. Firefox")

    choice = input("Choose an application to close: ")

    if choice == "1":
        confirmation = input(
            "Are you sure you want to close Firefox? (yes/no): "
        )

        if confirmation.lower() != "yes":
            print("Closing cancelled.")
            return

        result = subprocess.run(
            ["pkill", "-TERM", "-x", "firefox"],
            capture_output=True,
            text=True
        )

        if result.returncode == 0:
            print("Firefox closed successfully.")
        else:
            print("Firefox is not running.")
    else:
        print("Invalid choice.")