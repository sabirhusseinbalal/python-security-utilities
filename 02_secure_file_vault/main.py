from pathlib import Path
from cryptography.fernet import Fernet
import json
import shutil

BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "output"
OUTPUT_DIR.mkdir(exist_ok=True)

# Unique Path
def get_unique_path(base_path):
    if not base_path.exists():
        return base_path

    counter = 1

    while True:
        new_path = base_path.with_name(
            f"{base_path.stem}_{counter}{base_path.suffix}"
        )
        if not new_path.exists():
            return new_path
        counter += 1

# Encrypt
def encrypt_file(input_path):
    key = Fernet.generate_key()
    fernet = Fernet(key)

    with input_path.open("rb") as f:
        content = f.read()

    encrypted = fernet.encrypt(content)

    base_output = OUTPUT_DIR / f"encrypted_{input_path.name}"
    output_file = get_unique_path(base_output)  

    with output_file.open("wb") as f:
        f.write(encrypted)

    print(f"\nEncrypted file saved: {output_file.name}")
    print(f"Key (save this): {key.decode()}")

    return output_file.name, key.decode()


# Decrypt
def decrypt_file(input_path, key):
    try:
        fernet = Fernet(key.encode())

        with input_path.open("rb") as f:
            encrypted_data = f.read()

        decrypted = fernet.decrypt(encrypted_data)

        base_output = OUTPUT_DIR / f"decrypted_{input_path.name}"
        output_file = get_unique_path(base_output)

        with output_file.open("wb") as f:
            f.write(decrypted)

        print(f"\nFile decrypted: {output_file.name}")
        return True

    except Exception:
        print("Wrong key or invalid file!")
        return False


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


# Main Logic 
def secure_file(file_path):
    json_file = OUTPUT_DIR / "data.json"

    # load data
    if json_file.exists():
        with json_file.open("r") as f:
            data = json.load(f)
    else:
        data = {}

    choice = menu()

    if choice == 1:
        name, key = encrypt_file(file_path)

        data[name] = key

        with json_file.open("w") as f:
            json.dump(data, f, indent=4)

        print("Key also saved in data.json")

    elif choice == 2:
        key = input("Enter key: ").strip()

        decrypt_file(file_path, key)

    else:
        return


# Loop
while True:
    user_input = input("\nEnter file path (or 'q'): ").strip()

    if user_input.lower() == "q":
        print("Exiting...")
        break

    path = Path(user_input)

    if path.is_file():
        print(f"Loaded: {path.name}")
        secure_file(path)
    else:
        print("Invalid file or file not found.")
