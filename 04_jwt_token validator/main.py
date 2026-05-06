import jwt
import datetime
import warnings

# Hide annoying warnings (clean output)
warnings.filterwarnings("ignore")


SECRET = "mysecret123" # Default Key


# Decode Token
def decode_token(token):
    try:
        return jwt.decode(token, options={"verify_signature": False})
    except:
        print("Invalid token format")
        return None

# Verify Token
def verify_token(token):
    try:
        jwt.decode(token, SECRET, algorithms=["HS256"])
        return True

    except jwt.ExpiredSignatureError:
        print("Token expired")
    except jwt.InvalidSignatureError:
        print("Invalid signature or wrong secret")
    except:
        print("Verification failed")

    return False

# Check expiry
def check_expiry(payload):
    if "exp" not in payload:
        print("⚠ No expiry found")
        return

    current_time = int(datetime.datetime.now(datetime.UTC).timestamp())

    if current_time > payload["exp"]:
        print("Status: EXPIRED")
    else:
        print("Status: VALID")

# Print Data
def print_payload(payload):
    print("\n--- Payload ---")
    for k, v in payload.items():
        print(f"{k}: {v}")

# Loop
def main():
    while True:
        token = input("\nEnter token (or 'q'): ").strip()

        if token.lower() == "q":
            print("Exiting...")
            break

        if not token:
            print("Token cannot be empty!")
            continue

        # 1. Decode
        payload = decode_token(token)
        if not payload:
            continue

        print_payload(payload)

        # 2. Expiry check
        check_expiry(payload)

        # 3. Verify
        print("\n--- Verification ---")
        if verify_token(token):
            print("Token Verified")
        else:
            print("Token NOT Verified")


main()