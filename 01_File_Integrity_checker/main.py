from pathlib import Path
import hashlib
import json

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)

# Data load
def load_json_safe(json_file):
    if json_file.exists():
        try:
            with json_file.open("r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            print("[WARNING] Corrupted JSON detected. Resetting file.")
            return {}
    return {}

# Main Logic
def generate_hash(file_path):
    json_file = DATA_DIR / "data.json"

    data = load_json_safe(json_file)

    try:

        # Read file in binary mode
        with file_path.open("rb") as f:
            content = f.read()

        # Create identifiers
        file_id = hashlib.sha256(str(file_path.resolve()).encode()).hexdigest()
        file_hash = hashlib.sha256(content).hexdigest()

        print(f"File ID: {file_id}")
        print(f"Hash: {file_hash}")

        # Check existing data
        if file_id in data:
            if data[file_id] == file_hash:
                print("No changes detected")
            else:
                print("File content changed!")
        else:
            print("New file detected — saving hash")

        # Update and save
        data[file_id] = file_hash

        with json_file.open("w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

        print(f"\nData saved in {json_file.name}")

    except Exception as e:
        print(f"Error: {e}")


while True:
    user_input = input("\nEnter file path (or 'q'): ").strip()

    if user_input.lower() == "q":
        print("Exiting...")
        break

    default_file = BASE_DIR / "input" / "sample.txt"

    if not user_input:
        path = default_file
        if path.is_file():
            print(f"No path provided — using default file: {default_file.name}")
        else:
            print("No path provided and default file is missing.")
            continue
    else:
        path = Path(user_input)

    if path.is_file():
        print(f"File Loaded: {path.name}")
        generate_hash(path)
    else:
        print("Invalid file or file not found.")
