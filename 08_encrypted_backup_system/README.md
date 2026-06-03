# Encrypted Backup System

## Description
This project creates encrypted backups of folders and restores them using a secret encryption key.

It simulates a simple secure backup system used to protect files from unauthorized access.

**YouTube Video:**
[[Encrypted Backup System) | Security, Encryption & Utilities (Project 8)](https://youtu.be/-S07rfbcV_M?si=NDSLb3oY4F2SCCHN/)]

---

## What this project does
- Encrypts all files inside a folder
- Preserves folder structure
- Creates secure encrypted backups
- Restores encrypted backups using a key
- Uses one encryption key for the whole folder
- Stores backup keys in a JSON file

---

## Modules Used
- `pathlib` – file and folder handling
- `json` – storing backup keys
- `cryptography.fernet` – encryption and decryption

---

## Output Example
**Encrypt Example**
```
Enter folder path (or 'q'): D:\Rise
Loaded: Rise

1. Encrypt
2. Decrypt
3. Exit
: 1

Encrypted: coding_journey.txt
Encrypted: motivation.txt
Encrypted: ideas.txt
Encrypted: backup.js
Encrypted: hello.py
Encrypted: index.html
Encrypted: style.css
Encrypted: logo.txt
Encrypted: empty.txt

Key saved successfully!
Folder backup created:
backups/encrypted_folders/Rise
```
**Decrypt Example**
```
Enter folder path (or 'q'):
backups/encrypted_folders/Rise

Loaded: Rise

1. Encrypt
2. Decrypt
3. Exit
: 2

Enter key:
dg7wFAuFp7GwXBqlRCDRjar-vPBRMfG6_TxJA6YfxXk=

Restored: coding_journey.txt
Restored: motivation.txt
Restored: ideas.txt
Restored: backup.js
Restored: hello.py
Restored: index.html
Restored: style.css
Restored: logo.txt
Restored: empty.txt

9 file(s) restored successfully!
```

---

## Features
- Folder encryption system
- Folder restoration system
- Preserves nested folder structure
- Automatic .enc encrypted file extension
- Unique backup folder generation
- JSON key storage
- Wrong key detection
- CLI menu system

---

## Project Structure
```
08_encrypted_backup_system/
├── backups/
│   ├── encrypted_folders/
│   ├── restored_folders/
│   └── backup_keys.json
├── main.py
└── README.md
```

---

## Notes
- Empty folders are skipped during backup
- One encryption key protects the entire backup folder
- Real backup systems usually add compression, metadata, and recovery options
- Built to understand folder encryption and restoration logic step by step
