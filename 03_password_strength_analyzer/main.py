def main():
    while True:
        try:
            # Enter password
            password = input("\nEnter password (or 'q'): ").strip()


            # Quit
            if password.lower() == "q":
                print("Exiting...")
                break

            # If empty
            if not password:
                print("Password cannot be empty!")
                continue

            score = 0

            # Checks
            has_upper = any(char.isupper() for char in password)
            has_lower = any(char.islower() for char in password)
            has_digit = any(char.isdigit() for char in password)
            special_chars = set('!@#$%^&*()_+{}:"<>?[];\'\\,./`~')
            has_special = any(char in special_chars for char in password)

            # Length check (important)
            if len(password) >= 8:
                print("Length: OK")
                score += 1
            else:
                print("Length: Too short (min 8)")

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

            # Final decision
            if len(password) < 8:
                print("\nWeak Password (too short)")
            else:
                if score <= 2:
                    print("\nWeak Password")
                elif score <= 4:
                    print("\nMedium Password")
                else:
                    print("\nStrong Password")

        except Exception as e:
            print(f"Error: {e}")


main()