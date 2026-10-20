from file_manager import (
    list_files,
    create_file,
    create_folder,
    rename_file,
    delete_file,
)

from system_manager import (
    show_system_info,
    show_processes,
)

from app_manager import (
    open_application,
    close_application,
)


if __name__ == "__main__":
    while True:
        print("\n=== Voice Linux Project ===")
        print("1. List files")
        print("2. Create file")
        print("3. Create folder")
        print("4. Rename file")
        print("5. Delete file")
        print("6. Show System Information")
        print("7. Show Running Processes")
        print("8. Open Application")
        print("9. Close Application")
        print("10. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            list_files()

        elif choice == "2":
            filename = input("Enter the file name: ")
            create_file(filename)

        elif choice == "3":
            folder_name = input("Enter the folder name: ")
            create_folder(folder_name)

        elif choice == "4":
            old_name = input("Enter the file name to rename: ")
            new_name = input("Enter the new file name: ")
            rename_file(old_name, new_name)

        elif choice == "5":
            filename = input("Enter the file name to delete: ")
            delete_file(filename)

        elif choice == "6":
            show_system_info()

        elif choice == "7":
            show_processes()

        elif choice == "8":
            open_application()

        elif choice == "9":
            close_application()

        elif choice == "10":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice.")