from pathlib import Path
from cryptography.fernet import Fernet
import json

BASE_DIR = Path(__file__).resolve().parent

BACKUP_DIR = BASE_DIR / "backups"
BACKUP_DIR.mkdir(exist_ok=True)


# Unique folder name
def get_unique_path(base_path):
    if not base_path.exists():
        return base_path

    counter = 1

    while True:
        new_path = base_path.with_name(f"{base_path.stem}_{counter}")

        if not new_path.exists():
            return new_path

        counter += 1


# Encrypt single file
def encrypt_file(file_path, fernet):
    with file_path.open("rb") as f:
        content = f.read()

    return fernet.encrypt(content)


# Encrypt folder
def encrypt_folder(folder_path, json_file, data):

    output_root = BACKUP_DIR / "encrypted_folders" / folder_path.name
    output_root = get_unique_path(output_root)

    output_root.mkdir(parents=True, exist_ok=True)

    # one key for whole folder
    key = Fernet.generate_key()
    fernet = Fernet(key)

    for file in folder_path.rglob("*"):

        if file.is_file():

            try:
                relative_path = file.relative_to(folder_path)

                target_file = output_root / relative_path
                target_file.parent.mkdir(parents=True, exist_ok=True)

                encrypted_data = encrypt_file(file, fernet)

                output_file = target_file.with_suffix(file.suffix + ".enc")

                with output_file.open("wb") as f:
                    f.write(encrypted_data)

                print(f"Encrypted: {file.name}")

            except Exception as e:
                print(f"Failed: {file.name} -> {e}")

    # save folder key
    data[str(output_root)] = key.decode()

    with json_file.open("w") as f:
        json.dump(data, f, indent=4)

    print("\nKey saved successfully!")
    print(f"Folder backup created: {output_root}")


# Decrypt folder
def decrypt_folder(folder_path, key):

    try:
        fernet = Fernet(key.encode())

    except Exception:
        print("Invalid key format!")
        return

    output_root = BACKUP_DIR / "restored_folders" / folder_path.name
    output_root = get_unique_path(output_root)

    output_root.mkdir(parents=True, exist_ok=True)

    restored_count = 0

    for file in folder_path.rglob("*"):

        if file.is_file():

            try:
                relative_path = file.relative_to(folder_path)

                # remove .enc extension
                clean_name = file.stem

                target_file = output_root / relative_path.parent / clean_name
                target_file.parent.mkdir(parents=True, exist_ok=True)

                with file.open("rb") as f:
                    encrypted_data = f.read()

                decrypted_data = fernet.decrypt(encrypted_data)

                with target_file.open("wb") as f:
                    f.write(decrypted_data)

                print(f"Restored: {target_file.name}")

                restored_count += 1

            except Exception as e:
                print(f"Failed: {file.name} -> Wrong key or invalid file")

    print(f"\n{restored_count} file(s) restored successfully!")


# Menu
def menu():

    while True:

        try:
            choice = int(input("\n1. Encrypt\n2. Decrypt\n3. Exit\n: "))

            if choice in [1, 2, 3]:
                return choice

        except:
            pass

        print("Invalid choice!")


# Safe JSON loader
def load_json_safe(json_file):

    if json_file.exists():

        try:
            with json_file.open("r") as f:
                return json.load(f)

        except json.JSONDecodeError:
            print("[WARNING] Corrupted JSON detected. Resetting file.")
            return {}

    return {}


# Main logic
def backup_folder(folder_path):

    json_file = BACKUP_DIR / "backup_keys.json"

    data = load_json_safe(json_file)

    choice = menu()

    if choice == 1:

        encrypt_folder(folder_path, json_file, data)

    elif choice == 2:

        key = input("Enter key: ").strip()

        decrypt_folder(folder_path, key)

    else:
        return


# Runner
while True:

    user_input = input("\nEnter folder path (or 'q'): ").strip()

    if user_input.lower() == "q":
        print("Exiting...")
        break

    if not user_input:
        print("Path cannot be empty!")
        continue

    path = Path(user_input)

    if path.is_dir():

        print(f"Loaded: {path.name}")

        backup_folder(path)

    else:
        print("Invalid folder!")