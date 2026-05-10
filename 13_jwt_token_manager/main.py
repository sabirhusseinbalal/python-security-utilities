from pathlib import Path
from datetime import datetime, timedelta, timezone
import json
import string
import jwt

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)


# Menu
def menu():

    while True:

        try:
            choice = int(input(
                "\n1. Create Token\n"
                "2. Validate Token\n"
                "3. Delete Token\n"
                "4. List Tokens\n"
                "5. Exit\n: "
            ))

            if choice in [1, 2, 3, 4, 5]:
                return choice

        except ValueError:
            pass

        print("Invalid choice!")


# Load JSON safely
def load_json(file):

    if file.exists():

        try:
            with file.open("r", encoding="utf-8") as f:
                return json.load(f)

        except json.JSONDecodeError:
            print("Corrupted file reset.")
            return {}

    return {}


# clean name
def clean_name(name):

    translator = str.maketrans("", "", string.punctuation)
    return name.lower().translate(translator).strip()


# Create Token
def create_token():

    while True:

        try:
            name = input("\nToken Name: ").strip()
            if not name:
                print("Token name required")
                continue

            user = input("Subject/User: ").strip()
            if not user:
                print("User required")
                continue

            secret = input("Secret Key (min 32 chars recommended): ").strip()
            if not secret:
                print("Secret required")
                continue

            minutes = int(input("Expiry (minutes): "))

            # time (FIXED)
            issued_at = datetime.now(timezone.utc)
            expires_at = issued_at + timedelta(minutes=minutes)

            name = clean_name(name)
            user = clean_name(user)

            payload = {
                "sub": user,
                "token_name": name,
                "iat": issued_at,
                "exp": expires_at
            }

            token = jwt.encode(payload, secret, algorithm="HS256")

            print("\nToken created successfully!")

            return name, token, secret

        except ValueError:
            print("Enter valid number for expiry")

        except Exception as e:
            print(f"Error: {e}")


# Save token
def save_token(data, file, name, token, secret):

    data[name] = {
        "token": token,
        "secret": secret
    }

    with file.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    print("Saved to vault")


# Validate token
def validate_token(data):

    name = input("\nToken Name: ").strip()

    if name not in data:
        print("Token not found")
        return

    secret = input("Secret Key: ").strip()

    try:
        decoded = jwt.decode(
            data[name]["token"],
            secret,
            algorithms=["HS256"]
        )

        print("\nVALID TOKEN")
        print(decoded)

    except jwt.ExpiredSignatureError:
        print("Token expired")

    except jwt.InvalidSignatureError:
        print("Wrong secret key")

    except Exception as e:
        print(f"Error: {e}")


# Delete token
def delete_token(data, file):

    name = input("\nToken Name: ").strip()

    if name in data:

        del data[name]

        with file.open("w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

        print("Deleted")

    else:
        print("Not found")


# List tokens
def list_tokens(data):

    if not data:
        print("No tokens found")
        return

    print("\nTOKENS:")
    for k in data:
        print("-", k)


# MAIN
def main():

    file = DATA_DIR / "tokens.json"
    data = load_json(file)

    while True:

        choice = menu()

        if choice == 1:

            name, token, secret = create_token()
            save_token(data, file, name, token, secret)

        elif choice == 2:
            validate_token(data)

        elif choice == 3:
            delete_token(data, file)

        elif choice == 4:
            list_tokens(data)

        else:
            print("bye")
            break


main()