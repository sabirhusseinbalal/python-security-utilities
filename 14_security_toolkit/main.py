from pathlib import Path
import hashlib
import json
import socket
from datetime import datetime, UTC
import ssl
import pyotp
import jwt


BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)

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


# Menu
def menu():

    while True:

        try:
            choice = int(input(
                "\n1. Hash File\n"
                "2. Check Password Strength\n"
                "3. Scan Ports\n"
                "4. Check SSL\n"
                "5. Generate OTP\n"
                "6. Validate JWT\n"
                "7. Exit\n: "
            ))

            if choice in [1, 2, 3, 4, 5, 6, 7]:
                return choice

        except ValueError:
            pass

        print("Invalid choice!")


# Extract domain
def extract_domain(url):

    if not url.startswith("http"):
        url = "https://" + url

    return url.replace("https://", "").replace("http://", "").split("/")[0]


# 1. Hash File
def hash_file():

    json_file = DATA_DIR / "hashes.json"

    data = load_json_safe(json_file)

    while True:

        try:
            user_input = input("\nEnter file path (or 'q' for back): ").strip()

            if not user_input:
                print("Path cannot be empty!")
                continue

            if user_input.lower() == "q":
                print("Going Back...")
                break

            file_path = Path(user_input)

            if not file_path.is_file():
                print("Invalid file or file not found.")
                continue

            with file_path.open("rb") as f:
                content = f.read()

            file_id = hashlib.sha256(
                str(file_path.resolve()).encode()
            ).hexdigest()

            file_hash = hashlib.sha256(content).hexdigest()

            print(f"\nFile ID: {file_id}")
            print(f"Hash: {file_hash}")

            if file_id in data:

                if data[file_id] == file_hash:
                    print("No changes detected")

                else:
                    print("File content changed!")

            else:
                print("New file detected — saving hash")

            data[file_id] = file_hash

            with json_file.open("w", encoding="utf-8") as f:
                json.dump(data, f, indent=4)

            print(f"Data saved in {json_file.name}")

        except Exception as e:
            print(f"Error: {e}")


# 2. Password Strength
def check_password_strength():

    special_chars = set('!@#$%^&*()_+{}:"<>?[];\'\\,./`~')

    while True:

        try:
            password = input("\nEnter password (or 'q' for back): ").strip()

            if not password:
                print("Password cannot be empty!")
                continue

            if password.lower() == "q":
                print("Going Back...")
                break

            score = 0

            has_upper = any(c.isupper() for c in password)
            has_lower = any(c.islower() for c in password)
            has_digit = any(c.isdigit() for c in password)
            has_special = any(c in special_chars for c in password)

            if len(password) >= 8:
                print("Length: OK")
                score += 1
            else:
                print("Length: Too short")

            if has_upper:
                print("Uppercase: OK")
                score += 1
            else:
                print("Uppercase: Missing")

            if has_lower:
                print("Lowercase: OK")
                score += 1
            else:
                print("Lowercase: Missing")

            if has_digit:
                print("Number: OK")
                score += 1
            else:
                print("Number: Missing")

            if has_special:
                print("Special Char: OK")
                score += 1
            else:
                print("Special Char: Missing")

            print(f"\nScore: {score}/5")

            if len(password) < 8:
                print("Weak Password")

            elif score <= 2:
                print("Weak Password")

            elif score <= 4:
                print("Medium Password")

            else:
                print("Strong Password")

        except Exception as e:
            print(f"Error: {e}")


# 3. Port Scanner
def scan_ports():

    ports = [75, 76, 77, 78, 79, 80, 81, 443, 22, 3306]

    while True:

        url = input("\nEnter URL (or 'q' for back): ").strip()

        if not url:
            print("URL cannot be empty!")
            continue

        if url.lower() == "q":
            print("Going Back...")
            break

        domain = extract_domain(url)

        try:
            ip = socket.gethostbyname(domain)

            print(f"\nScanning {domain} ({ip})...\n")

            for port in ports:

                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

                s.settimeout(1)

                try:
                    s.connect((ip, port))
                    print(f"[OPEN] Port {port}")

                except:
                    print(f"[CLOSED] Port {port}")

                finally:
                    s.close()

            print("\nScan Complete!")

        except socket.gaierror:
            print("Unable to resolve domain.")

        except Exception as e:
            print(f"Error: {e}")


# 4. SSL Checker
def check_ssl():

    while True:

        url = input("\nEnter URL (or 'q' for back): ").strip()

        if not url:
            print("URL cannot be empty!")
            continue

        if url.lower() == "q":
            print("Going Back...")
            break

        domain = extract_domain(url)

        try:
            context = ssl.create_default_context()

            ip = socket.gethostbyname(domain)

            print(f"\nScanning {domain} ({ip})...")

            with socket.create_connection((domain, 443)) as sock:

                with context.wrap_socket(sock, server_hostname=domain) as ssock:

                    cert = ssock.getpeercert()

            expiry_date = datetime.strptime(
                cert["notAfter"],
                "%b %d %H:%M:%S %Y %Z"
            )

            days_left = (expiry_date - datetime.now()).days

            print(f"\nDomain: {domain}")

            for field in cert["issuer"]:

                key, value = field[0]

                print(f"{key}: {value}")

            print(f"Valid From : {cert['notBefore']}")
            print(f"Expiry Date: {cert['notAfter']}")
            print(f"Days Left  : {days_left}")

            if days_left <= 0:
                print("Certificate Status: EXPIRED")

            elif days_left <= 30:
                print("Certificate Status: EXPIRING SOON")

            else:
                print("Certificate Status: VALID")

        except socket.gaierror:
            print("Unable to resolve domain.")

        except ssl.SSLError:
            print("SSL certificate error.")

        except Exception as e:
            print(f"Error: {e}")


# 5. Generate OTP
def generate_otp():

    json_file = DATA_DIR / "users.json"

    data = load_json_safe(json_file)

    while True:

        user = input("\nEnter Username (or 'q' for back): ").strip()

        if not user:
            print("Username cannot be empty!")
            continue

        if user.lower() == "q":
            print("Going Back...")
            break

        try:

            if user not in data:

                secret = pyotp.random_base32()

                data[user] = {
                    "secret": secret
                }

                with json_file.open("w", encoding="utf-8") as f:
                    json.dump(data, f, indent=4)

                print("\nNew user created!")
                print(f"Secret: {secret}")

            secret = data[user]["secret"]

            totp = pyotp.TOTP(secret)

            print(f"\nCurrent OTP: {totp.now()}")

            code = input("Enter OTP: ").strip()

            if totp.verify(code):
                print("Login Successful!")

            else:
                print("Wrong or expired OTP")

        except Exception as e:
            print(f"Error: {e}")


# 6. Validate JWT
def validate_jwt():

    while True:

        token = input("\nEnter token (or 'q' for back): ").strip()

        if not token:
            print("Token cannot be empty!")
            continue

        if token.lower() == "q":
            print("Going Back...")
            break

        try:
            payload = jwt.decode(
                token,
                options={"verify_signature": False}
            )

            print("\n--- Payload ---")

            for k, v in payload.items():
                print(f"{k}: {v}")

        except Exception:
            print("Invalid token format")
            continue

        print("\n--- Status ---")

        if "exp" in payload:

            current_time = int(datetime.now(UTC).timestamp())

            if current_time > payload["exp"]:
                print("Token Status: EXPIRED")

            else:
                print("Token Status: VALID")

        else:
            print("No expiry found")

        secret = input("\nEnter Secret Key: ").strip()

        try:
            jwt.decode(
                token,
                secret,
                algorithms=["HS256"]
            )

            print("Token Verified")

        except jwt.ExpiredSignatureError:
            print("Token expired")

        except jwt.InvalidSignatureError:
            print("Wrong secret key")

        except Exception:
            print("Verification failed")


# Main
def main():

    while True:

        choice = menu()

        if choice == 1:
            hash_file()

        elif choice == 2:
            check_password_strength()

        elif choice == 3:
            scan_ports()

        elif choice == 4:
            check_ssl()

        elif choice == 5:
            generate_otp()

        elif choice == 6:
            validate_jwt()

        else:
            print("Exiting...")
            break


main()