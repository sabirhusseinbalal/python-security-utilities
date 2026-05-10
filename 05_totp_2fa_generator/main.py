from pathlib import Path
import json
import pyotp

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)


def handle_user(user, data):
    # Existing User 
    if user in data:
        secret = data[user]["secret"]

        totp = pyotp.TOTP(secret)


        # show current OTP (for learning)
        print(f"\nCurrent OTP: {totp.now()}")

        attempts = 3

        while attempts > 0:
            code = input("\nEnter OTP: ").strip()

            if totp.verify(code):
                print("\nLogin Successful!")
                return False  # no need to save
            else:
                print("Wrong or expired OTP")

            attempts -= 1
            
            print(f"Attempts left: {attempts}")

        print("You lost all 3 attempts.")
        return False

    # New User 
    else:
        secret = pyotp.random_base32()

        data[user] = {
            "secret": secret
        }

        print("\nNew user created!")
        print(f"Secret (save this): {secret}")

        totp = pyotp.TOTP(secret)
        print(f"Current OTP: {totp.now()}")

        return True  # need to save
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

# Main Loop 
while True:
    user = input("\nEnter Username (or 'q'): ").strip()

    if user.lower() == "q":
        print("Exiting...")
        break

    if not user:
        print("Username cannot be empty!")
        continue

    json_file = DATA_DIR / "users.json"

    data = load_json_safe(json_file)

    try:
        should_save = handle_user(user, data)

        if should_save:
            with json_file.open("w") as f:
                json.dump(data, f, indent=4)

            print(f"Data saved in {json_file.name}")

    except Exception as e:
        print(f"Error: {e}")