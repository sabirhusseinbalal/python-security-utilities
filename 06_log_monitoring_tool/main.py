from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


def log_monitoring(file_path):
    fail_count = {}
    data = {}

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()

                # skip invalid lines
                if not line or "=" not in line:
                    continue

                parts = line.split("=")
                if len(parts) < 2:
                    continue

                value = parts[1].strip()

                # FILE ACCESS 
                if "FILE ACCESS" in line:
                    file_name = value

                    if "admin" in file_name:
                        print(f"[ALERT] Sensitive file accessed: {file_name}")
                    continue

                user = value

                # initialize user if not exists
                if user not in data:
                    data[user] = {"success": 0, "fail": 0, "total": 0}

                # LOGIN FAIL 
                if "LOGIN FAIL" in line:
                    data[user]["fail"] += 1
                    data[user]["total"] += 1

                    if user == "unknown":
                        print("[WARNING] Unknown user login attempt detected")
                    else:
                        print(f"[WARNING] user: {user} login attempt detected")

                    fail_count[user] = fail_count.get(user, 0) + 1

                # LOGIN SUCCESS 
                elif "LOGIN SUCCESS" in line:
                    data[user]["success"] += 1
                    data[user]["total"] += 1

        # SUMMARY
        print("\n[INFO] Scanning logs...")

        for user, attempts in fail_count.items():
            if attempts >= 3:
                print(f"[ALERT] User `{user}` blocked ({attempts} failed logins)")

        # USER ANALYSIS 
        for user, stats in data.items():
            print(f"\nUser: {user}")
            print(f"SUCCESS: {stats['success']} | FAIL: {stats['fail']}")

            if stats["fail"] > stats["success"]:
                fail_ratio = stats["fail"] / stats["total"]

                if fail_ratio >= 0.6:
                    print(f"{user} --> Suspicious activity")
                else:
                    print(f"{user} --> Maybe ok")
            else:
                print(f"{user} --> Normal")

    except Exception as e:
        print(f"Error: {e}")


# MAIN LOOP
while True:
    user_input = input("\nEnter file path (or 'q'): ").strip()

    if user_input.lower() == "q":
        print("Exiting...")
        break

    default_file = BASE_DIR / "logs" / "system.log"

    if not user_input:
        path = default_file
        if path.is_file():
            print(f"No path provided — using default file: {path.name}")
        else:
            print("Default file missing.")
            continue
    else:
        path = Path(user_input)

    if path.is_file() and path.suffix.lower() == ".log":
        print(f"File Loaded: {path.name}")
        log_monitoring(path)
    else:
        print("Invalid file or file not found.")