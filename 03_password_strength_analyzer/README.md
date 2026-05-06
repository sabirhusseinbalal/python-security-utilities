# Password Strength Analyzer

## Description
This project checks how strong a password is based on simple rules.

It analyzes the password and tells whether it is weak, medium, or strong.

This helps understand basic password security used in real systems.

---

## What this project does
- Takes password input from user
- Checks for:
  - Minimum length
  - Uppercase letters
  - Lowercase letters
  - Numbers
  - Special characters
- Calculates a score
- Shows password strength

---

## Modules Used
- Built-in Python functions (`any`, `len`, `str methods`)

---

## Output Example
```
Enter password (or 'q'): sabir-loser
Length: OK
Uppercase: Missing
Lowercase: OK
Number: Missing
Special Char: Missing

Score: 2/5

Weak Password

Enter password (or 'q'): Abc123!@
Length: OK
Uppercase: OK
Lowercase: OK
Number: OK
Special Char: OK

Score: 5/5

Strong Password

Enter password (or 'q'): q
Exiting...
```

---

## Features
- Simple password strength checking
- Clear rule-based validation
- Score system (0–5)
- Real-time feedback
- Easy CLI interaction

---

## Project Structure
```
03_password_strength_analyzer/
├── main.py
└── README.md
```

---

## Notes
- Password must be at least 8 characters
- Missing rules reduce strength
- This is a learning project, not full security validation
