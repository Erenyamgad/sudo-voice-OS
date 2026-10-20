import subprocess
from pathlib import Path

FILES_DIR = Path(__file__).parent / "files"


def list_files():
    result = subprocess.run(
        ["ls", str(FILES_DIR)],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        print("Files in the files folder:")
        print(result.stdout)
    else:
        print("Error listing files:")
        print(result.stderr)


def create_file(filename):
    if not filename or Path(filename).name != filename or filename in {".", ".."}:
        print("Invalid file name.")
        return

    file_path = FILES_DIR / filename

    try:
        with file_path.open("x", encoding="utf-8"):
            pass
        print(f"File '{filename}' created successfully in files folder.")

    except FileExistsError:
        print(f"File '{filename}' already exists.")

    except OSError as error:
        print(f"Error creating file: {error}")


def create_folder(folder_name):
    if not folder_name or Path(folder_name).name != folder_name or folder_name in {".", ".."}:
        print("Invalid folder name.")
        return

    folder_path = FILES_DIR / folder_name

    try:
        folder_path.mkdir()
        print(f"Folder '{folder_name}' created successfully.")

    except FileExistsError:
        print(f"Folder '{folder_name}' already exists.")

    except OSError as error:
        print(f"Error creating folder: {error}")


def rename_file(old_name, new_name):
    if (
        not old_name
        or not new_name
        or Path(old_name).name != old_name
        or Path(new_name).name != new_name
        or old_name in {".", ".."}
        or new_name in {".", ".."}
    ):
        print("Invalid file name.")
        return

    old_path = FILES_DIR / old_name
    new_path = FILES_DIR / new_name

    if not old_path.is_file():
        print(f"File '{old_name}' does not exist.")
        return

    if new_path.exists():
        print(f"'{new_name}' already exists.")
        return

    try:
        old_path.rename(new_path)
        print(f"File renamed from '{old_name}' to '{new_name}'.")

    except OSError as error:
        print(f"Error renaming file: {error}")


def delete_file(filename):
    if not filename or Path(filename).name != filename or filename in {".", ".."}:
        print("Invalid file name.")
        return

    file_path = FILES_DIR / filename

    if not file_path.is_file():
        print(f"File '{filename}' does not exist.")
        return

    confirmation = input(
        f"Are you sure you want to delete '{filename}'? (yes/no): "
    )

    if confirmation.lower() != "yes":
        print("Deletion cancelled.")
        return

    try:
        file_path.unlink()
        print(f"File '{filename}' deleted successfully.")

    except OSError as error:
        print(f"Error deleting file: {error}")