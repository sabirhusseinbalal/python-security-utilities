# Security Toolkit

## Description
This project combines multiple beginner cybersecurity tools into one simple command-line toolkit.

It includes file hashing, password checking, port scanning, SSL certificate checking, OTP generation, and JWT inspection.

This project was built step-by-step to understand how different security tools work together in real systems.

**YouTube Video:**
[[Security Toolkit | Security, Encryption & Utilities (Project 14)](https://youtu.be/5Q_28Utuxp0?si=cV-djcKRQYn5teo1/)]

---

## What this project does
- Checks file integrity using SHA256 hashing
- Analyzes password strength
- Scans common ports on a website
- Checks SSL certificate expiry
- Generates and verifies OTP codes
- Reads and validates JWT tokens

---

## Modules Used
- `pathlib` → file and folder handling
- `hashlib` → file hashing
- `json` → storing data
- `socket` → network connection and port scanning
- `ssl` → SSL certificate inspection
- `datetime` → date and expiry handling
- `pyotp` → OTP generation
- `jwt` → JWT token decoding and verification

---

## Output Example
```
1. Hash File
2. Check Password Strength
3. Scan Ports
4. Check SSL
5. Generate OTP
6. Validate JWT
7. Exit
: 3

Enter URL (or 'q' for back): www.google.com

Scanning www.google.com (142.251.150.119)...

[OPEN] Port 80
[OPEN] Port 443

Scan Complete!
```
```
Enter password (or 'q' for back): S4b!r@123

Length: OK
Uppercase: OK
Lowercase: OK
Number: OK
Special Char: OK

Score: 5/5
Strong Password
```
```
Enter Username (or 'q' for back): sabir

New user created!
Secret: 5JZKBVDOQHEWDHO7NGBG2RSWV2L7MRMV

Current OTP: 392023
Enter OTP: 392023

Login Successful!
```

---

## Features
- Multi-tool security utility
- SHA256 file integrity checking
- Password strength scoring
- Basic port scanning
- SSL expiry monitoring
- OTP login simulation
- JWT payload inspection
- Beginner-friendly CLI system

---

## Project Structure
```
14_security_toolkit/
├── data/
│   ├── hashes.json
│   └── users.json
├── main.py
└── README.md
```

---

## Notes
- This is an educational cybersecurity project.
- Built for learning security, encryption, and networking basics.
- JWT payload reading without verification is only safe for inspection/debugging.
- Real systems always verify JWT signatures before trusting token data.
- Large files should be hashed in chunks to avoid high memory usage.
- Timezone-aware datetime handling is safer in real-world systems.
