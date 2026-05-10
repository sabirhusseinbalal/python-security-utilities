from pathlib import Path
from cryptography.fernet import Fernet
import json
import string

BASE_DIR = Path(__file__).resolve().parent

NOTES_DIR = BASE_DIR / "notes"
NOTES_DIR.mkdir(exist_ok=True)

DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)


# Menu
def menu():

    while True:

        try:
            choice = int(input(
                "\n1. Create Note\n2. View Note\n3. Delete Note\n4. Exit\n: "
            ))

            if choice in [1, 2, 3, 4]:
                return choice

        except:
            pass

        print("Invalid choice!")


# Safe JSON Loader
def load_json_safe(json_file):

    if json_file.exists():

        try:
            with json_file.open("r", encoding="utf-8") as f:
                return json.load(f)

        except json.JSONDecodeError:
            print("[WARNING] Corrupted JSON detected. Resetting file.")
            return {}

    return {}


# Clean title
def clean_title(title):

    translator = str.maketrans('', '', string.punctuation)

    return title.lower().translate(translator).strip()


# Create Note
def create_note():

    while True:

        try:
            title = input("\nEnter note title: ").strip()

            if not title:
                print("Title cannot be empty!")
                continue

            content = input(f"Enter note content: ").strip()

            if not content:
                print("Content cannot be empty!")
                continue

            title = clean_title(title)

            key = Fernet.generate_key()
            fernet = Fernet(key)

            encrypted_data = fernet.encrypt(content.encode())

            output_file = NOTES_DIR / f"{title}.txt.enc"

            counter = 1

            while output_file.exists():
                output_file = NOTES_DIR / f"{title}_{counter}.txt.enc"
                counter += 1

            with output_file.open("wb") as f:
                f.write(encrypted_data)

            clean_name = output_file.name

            print(f"\nEncrypted Note Created: {clean_name}")
            print(f"Key (save this): {key.decode()}")

            return clean_name, key.decode()

        except Exception as e:
            print(f"Error: {e}")


# View Note
def view_note(data, json_file):

    title = input("\nEnter note filename: ").strip()

    if not title:
        print("Title cannot be empty!")
        return

    if title not in data:
        print("Note not found!")
        return

    user_key = input("Enter key: ").strip()

    if not user_key:
        print("Key cannot be empty!")
        return

    if user_key != data[title]:
        print("Wrong key!")
        return

    file_path = NOTES_DIR / title

    if not file_path.exists():
        print("File does not exist anymore!")
        del data[title]

        with json_file.open("w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        return

    try:
        fernet = Fernet(user_key.encode())

        with file_path.open("rb") as f:
            encrypted_data = f.read()

        decrypted = fernet.decrypt(encrypted_data)

        print(f"\n----- {title} -----")
        print(decrypted.decode())
        print("-------------------")

    except Exception:
        print("Failed to decrypt note!")


# Delete Note
def delete_note(data, json_file):

    title = input("\nEnter note filename: ").strip()

    if not title:
        print("Title cannot be empty!")
        return

    if title not in data:
        print("Note not found!")
        return

    user_key = input("Enter key: ").strip()

    if not user_key:
        print("Key cannot be empty!")
        return

    if user_key != data[title]:
        print("Wrong key!")
        return

    file_path = NOTES_DIR / title

    if not file_path.exists():
        print("File already missing!")

        # remove broken json record
        del data[title]

        with json_file.open("w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

        return

    try:
        file_path.unlink()

        # remove password entry
        del data[title]

        with json_file.open("w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

        print(f"Note deleted successfully: {title}")

    except Exception as e:
        print(f"Delete failed: {e}")


# Main Logic
def main():

    json_file = DATA_DIR / "password.json"

    data = load_json_safe(json_file)

    while True:

        choice = menu()

        # Create
        if choice == 1:

            name, key = create_note()

            data[name] = key

            with json_file.open("w", encoding="utf-8") as f:
                json.dump(data, f, indent=4)

            print(f"Key saved in: {json_file.name}")

        # View
        elif choice == 2:

            view_note(data, json_file)

        # Delete
        elif choice == 3:

            delete_note(data, json_file)

        # Exit
        else:

            print("Exiting...")
            break


main()