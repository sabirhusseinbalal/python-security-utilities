from pathlib import Path
from cryptography.fernet import Fernet
import json
import string

BASE_DIR = Path(__file__).resolve().parent

VAULT_DIR = BASE_DIR / "vault"
VAULT_DIR.mkdir(exist_ok=True)

DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)


# Menu
def menu():

    while True:

        try:
            choice = int(input(
                "\n1. Save API Key\n"
                "2. View API Key\n"
                "3. Delete API Key\n"
                "4. List Services\n"
                "5. Exit\n: "
            ))

            if choice in [1, 2, 3, 4, 5]:
                return choice

        except ValueError:
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


# Clean Service Name
def clean_name(name):

    translator = str.maketrans('', '', string.punctuation)

    return name.lower().translate(translator).strip()


# Save API Key
def save_api_key():

    while True:

        try:
            service = input("\nEnter Service Name: ").strip()

            if not service:
                print("Service name cannot be empty!")
                continue

            api_key = input("Enter API Key: ").strip()

            if not api_key:
                print("API Key cannot be empty!")
                continue

            service = clean_name(service)

            key = Fernet.generate_key()
            fernet = Fernet(key)

            encrypted_data = fernet.encrypt(api_key.encode())

            output_file = VAULT_DIR / f"{service}.key.enc"

            counter = 1

            while output_file.exists():
                output_file = VAULT_DIR / f"{service}_{counter}.key.enc"
                counter += 1

            with output_file.open("wb") as f:
                f.write(encrypted_data)

            print(f"\nEncrypted API Key saved: {output_file.name}")
            print(f"Key Code (save this): {key.decode()}")

            return output_file.name, key.decode()

        except Exception as e:
            print(f"Error: {e}")


# View API Key
def view_api_key(data, json_file):

    service = input("\nEnter Service Name: ").strip()

    if not service:
        print("Service name cannot be empty!")
        return

    service = clean_name(service)

    filename = f"{service}.key.enc"

    if filename not in data:
        print("Service not found!")
        return

    user_key = input("Enter Key Code: ").strip()

    if not user_key:
        print("Key code cannot be empty!")
        return

    if user_key != data[filename]["key"]:
        print("Wrong key!")
        return

    file_path = VAULT_DIR / filename

    if not file_path.exists():

        print("Encrypted file missing!")

        del data[filename]

        with json_file.open("w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

        return

    try:
        fernet = Fernet(user_key.encode())

        with file_path.open("rb") as f:
            encrypted_data = f.read()

        decrypted = fernet.decrypt(encrypted_data)

        print("\n-------------------")
        print(f"Service : {service}")
        print(f"API Key : {decrypted.decode()}")
        print("-------------------")

    except Exception:
        print("Failed to decrypt API key!")


# Delete API Key
def delete_api_key(data, json_file):

    service = input("\nEnter Service Name: ").strip()

    if not service:
        print("Service name cannot be empty!")
        return

    service = clean_name(service)

    filename = f"{service}.key.enc"

    if filename not in data:
        print("Service not found!")
        return

    user_key = input("Enter Key Code: ").strip()

    if not user_key:
        print("Key code cannot be empty!")
        return

    if user_key != data[filename]["key"]:
        print("Wrong key!")
        return

    file_path = VAULT_DIR / filename

    if not file_path.exists():

        print("Encrypted file already missing!")

        del data[filename]

        with json_file.open("w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

        return

    try:
        file_path.unlink()

        del data[filename]

        with json_file.open("w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

        print(f"Deleted: {filename}")

    except Exception as e:
        print(f"Delete failed: {e}")


# List Services
def list_services(data):

    if not data:
        print("No services saved!")
        return

    print("\nSaved Services:")
    print("-------------------")

    for filename in data:

        service_name = (
            filename
            .replace(".key.enc", "")
        )

        print(f"- {service_name}")

    print("-------------------")


# Main Logic
def main():

    json_file = DATA_DIR / "vault_keys.json"

    data = load_json_safe(json_file)

    while True:

        choice = menu()

        # Save
        if choice == 1:

            filename, key = save_api_key()

            data[filename] = {
                "key": key
            }

            with json_file.open("w", encoding="utf-8") as f:
                json.dump(data, f, indent=4)

            print(f"Vault updated: {json_file.name}")

        # View
        elif choice == 2:

            view_api_key(data, json_file)

        # Delete
        elif choice == 3:

            delete_api_key(data, json_file)

        # List
        elif choice == 4:

            list_services(data)

        # Exit
        else:

            print("Exiting...")
            break


main()