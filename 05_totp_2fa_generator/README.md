# TOTP 2FA Generator

## Description
This project simulates a simple 2-Factor Authentication (2FA) system using OTP (One-Time Password).

Each user gets a secret key, and based on that key, a new OTP is generated every ~30 seconds.

The user must enter the correct OTP to log in.

This helps understand how apps like Google Authenticator or Microsoft Authenticator work.

**YouTube Video:**
[[TOTP 2FA Generator | Security, Encryption & Utilities (Project 5)](https://youtu.be/ahbKEijnTT4?si=cgrqrLYe4Mx5s20M/)]

---

## What this project does
- Creates a new user with a secret key
- Generates time-based OTP (auto changes every ~30 seconds)
- Verifies login using OTP
- Allows only 3 attempts
- Stores user data in JSON file

---

## Modules Used
- `pyotp` – OTP generation and verification
- `json` – storing user data
- `pathlib` – file handling

---

## Output Example
**New User**
```
Enter Username (or 'q'): sabirhusseinbalal

New user created!
Secret (save this): TPOS3ORWZICPOBDFC4KQIGH3TPH7NSQM
Current OTP: 389470
Data saved in users.json
```
**Login (Correct OTP)**
```
Enter Username (or 'q'): sabirhusseinbalal

Current OTP: 423054

Enter OTP: 423054

Login Successful!
```
**Wrong / Expired OTP**
```
Current OTP: 389470

Enter OTP: 38590
Wrong or expired OTP
Attempts left: 2

Enter OTP: 384970
Wrong or expired OTP
Attempts left: 1

Enter OTP: 38590
Wrong or expired OTP
Attempts left: 0
You lost all 3 attempts.
```
---


## Features
- Time-based OTP (changes automatically every ~30 sec)
- Secret key per user
- 3 attempt limit
- Clear message for wrong or expired OTP
- JSON storage for users
- Simple CLI system

---

## Project Structure
```
05_totp_2fa_generator/
├── data/
│   └── users.json
├── main.py
└── README.md
```

---

## Notes
- OTP codes change automatically after short time intervals
- The secret key is the core of the authentication system
- Real authenticator apps use the same basic concept
- Built to explore how time-based login security works
