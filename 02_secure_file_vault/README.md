# Secure File Vault

## Description
This project encrypts and decrypts files using a secret key.

It converts a normal file into unreadable format (encryption) and restores it back (decryption) using the same key.

This helps understand how data protection works in real systems.

**YouTube Video:**
[[Secure File Vault | Security, Encryption & Utilities (Project 2)](https://youtu.be/dlE1ge3Xi3s?si=RlRSvIoOvwNvgMt4/)]

---

## What this project does
- Reads a file
- Encrypts file into secure format
- Generates a secret key
- Decrypts file using the same key
- Saves all results in output folder

---

## Modules Used
- `cryptography (Fernet)` – encryption and decryption
- `pathlib` – file handling
- `json` – storing keys

---

## Output Example
```
Enter file path (or 'q'): ...\input\sample.txt
Loaded: sample.txt
```
**Encrypt:**
```
1. Encrypt
2. Decrypt
3. Exit
: 1

Encrypted file saved: encrypted_sample.txt
Key (save this): s0mjTVOqPxFVsuna8YKPVbz50_4KMPYYhFk4ke9Zwuc=
Key also saved in data.json
```
**Decrypt:**
```
1. Encrypt
2. Decrypt
3. Exit
: 2
```
```
Enter key: s0mjTVOqPxFVsuna8YKPVbz50_4KMPYYhFk4ke9Zwuc=

File decrypted: decrypted_encrypted_sample.txt
```
**OR**
```
Enter key: H79pbAwni7nx5m3Dr2V6HpXQKAczBW0GWNP5R9zOIQQ=
Wrong key or invalid file!
```

---

## Features
- Encrypt and decrypt files
- Unique filename handling (no overwrite)
- Key-based security
- JSON storage for keys
- Simple CLI interface

---

## Project Structure
```
02_secure_file_vault/
├── input/
│ └── sample.txt
├── output/
│ ├── data.json
│ ├── decrypted_encrypted_sample.txt
│ ├── encrypted_sample_1.txt
│ └── encrypted_sample.txt
├── main.py
└── README.md
```

---

## Notes
- The same key is required to restore encrypted files
- Wrong keys cannot recover original content
- Real systems protect keys much more carefully than this demo
- This project was built to understand the basics of file encryption and recovery
