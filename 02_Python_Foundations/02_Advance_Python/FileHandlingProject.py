from pathlib import Path

BASE_PATH = Path.cwd()


def list_files_and_folders():
    items = list(BASE_PATH.rglob('*'))
    if not items:
        print("No files or folders found.")
        return
    for i, item in enumerate(items, start=1):
        print(f"{i} : {item}")


def create_file():
    try:
        list_files_and_folders()
        name = input("Enter file name: ").strip()
        p = BASE_PATH / name

        if p.exists():
            print("File already exists.")
            return

        data = input("Enter content to write: ")
        p.write_text(data)
        print("File created successfully.")

    except Exception as err:
        print(f"Error: {err}")


def read_file():
    try:
        name = input("Enter file name to read: ").strip()
        p = BASE_PATH / name

        if not p.exists() or not p.is_file():
            print("File does not exist.")
            return

        print("\n--- File Content ---")
        print(p.read_text())
        print("--------------------")

    except Exception as err:
        print(f"Error: {err}")


def update_file():
    try:
        name = input("Enter file name to update: ").strip()
        p = BASE_PATH / name

        if not p.exists() or not p.is_file():
            print("File does not exist.")
            return

        data = input("Enter new content (will overwrite): ")
        p.write_text(data)
        print("File updated successfully.")

    except Exception as err:
        print(f"Error: {err}")


def delete_file():
    try:
        name = input("Enter file name to delete: ").strip()
        p = BASE_PATH / name

        if not p.exists() or not p.is_file():
            print("File does not exist.")
            return

        p.unlink()
        print("File deleted successfully.")

    except Exception as err:
        print(f"Error: {err}")


# -------- MAIN MENU --------
print("Press 1 for creating a file")
print("Press 2 for reading a file")
print("Press 3 for updating a file")
print("Press 4 for deleting a file")

choice = int(input("Select your response: "))

if choice == 1:
    create_file()
elif choice == 2:
    read_file()
elif choice == 3:
    update_file()
elif choice == 4:
    delete_file()
else:
    print("Invalid choice.")
