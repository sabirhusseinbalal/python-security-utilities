# Secure Notes CLI

## Description
This project is a simple encrypted notes manager built with Python.

Users can create, view, and delete private notes securely using encryption keys.

Each note is encrypted before saving, so the original content cannot be read directly from the file.

**YouTube Video:**
[[Secure Notes CLI | Security, Encryption & Utilities (Project 9)](https://youtu.be/in1SKRNaV_s?si=-dIlK2ZP2SyjECXk/)]

---

## What this project does
- Creates encrypted notes
- Stores notes securely as .enc files
- Generates a unique encryption key for every note
- Allows viewing notes only with the correct key
- Deletes notes securely
- Stores keys in a local JSON file
- Handles missing or corrupted files safely

---

## Modules Used
- `pathlib – file` and folder handling
- `cryptography.fernet` – encryption and decryption
- `json` – password/key storage
- `string` – title cleaning

---

## Output Example
```
1. Create Note
2. View Note
3. Delete Note
4. Exit
: 1

Enter note title: rise
Enter note content: Rise with Purpose.

Encrypted Note Created: rise.txt.enc
Key (save this): FRENPhqZajg5pNdAw3oIQTD-JhNcgIytgn_F3ZaVt-Q=
Key saved in: password.json

1. Create Note
2. View Note
3. Delete Note
4. Exit
: 2

Enter note filename: rise.txt.enc
Enter key: FRENPhqZajg5pNdAw3oIQTD-JhNcgIytgn_F3ZaVt-Q=

----- rise.txt.enc -----
Rise with Purpose.
-------------------

1. Create Note
2. View Note
3. Delete Note
4. Exit
: 3

Enter note filename: rise.txt.enc
Enter key: FRENPhqZajg5pNdAw3oIQTD-JhNcgIytgn_F3ZaVt-Q=
Note deleted successfully: rise.txt.enc

1. Create Note
2. View Note
3. Delete Note
4. Exit
: 4
Exiting...
```

---

## Features
- Encrypted note storage
- Unique key generation per note
- Safe JSON loading system
- Missing file cleanup handling
- Filename sanitization
- Simple CLI menu system
- Secure note viewing and deletion

---

## Project Structure
```
09_secure_notes_cli/
├── data/
│   └── password.json
├── notes/
│   └── rise.txt.enc
├── main.py
└── README.md
```

---

## Notes
- Each note uses its own encryption key
- Notes can only be viewed with the correct key
- Missing files are cleaned automatically from saved records
- Built to practice secure storage, encryption, and file management basics
