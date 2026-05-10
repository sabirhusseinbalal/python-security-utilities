from pathlib import Path
import os
import time

BASE_DIR = Path(__file__).resolve().parent
INPUT_DIR = BASE_DIR / "input"
INPUT_DIR.mkdir(exist_ok=True)


# Secure Shredding
def shred_file(file_path):

    try:
        size = file_path.stat().st_size

        print(f"\nFile Size: {size} Bytes")
        print("\nOverwriting file...")

        # overwrite file 3 times
        for i in range(1, 4):

            random_bytes = os.urandom(size)

            with file_path.open("wb") as f:
                f.write(random_bytes)

            print(f"Pass {i} completed...")
            time.sleep(1)

        # delete file
        file_path.unlink()

        print("\nFile shredded successfully!")

    except Exception as e:
        print(f"Error: {e}")


# Runner
while True:

    user_input = input("\nEnter file path (or 'q'): ").strip()

    if user_input.lower() == "q":
        print("Exiting...")
        break

    default_file = INPUT_DIR / "story.txt"

    # default file
    if not user_input:

        path = default_file

        if path.is_file():
            print(f"No path provided — using default file: {path.name}")
        else:
            print("Default file missing!")
            continue

    else:
        path = Path(user_input)

    # validate file
    if path.is_file():

        print(f"File Loaded: {path.name}")
        shred_file(path)

    else:
        print("Invalid file or file not found.")