# API Key Vault Manager

## Description
This project securely stores API keys using encryption.

Each API key is encrypted and saved into a separate file, while the encryption key is stored inside a JSON vault file.

This simulates a very basic version of how secret managers and credential storage systems work.

**YouTube Video:**
[[API Key Vault Manager | Security, Encryption & Utilities (Project 10)](https://youtu.be/5sca2SM_Gzo?si=veJdsj8NZ3aZrgmt/)]

---

## What this project does
- Saves API keys securely using encryption
- Encrypts every API key before storing it
- Lets users view saved API keys using the correct key code
- Deletes API keys securely
- Lists all saved services
- Stores encrypted files separately from vault metadata

---

## Modules Used
- `pathlib` → file and folder handling
- `cryptography.fernet` → encryption and decryption
- `json` → storing vault metadata
- `string` → cleaning service names

---

## Output Example
```
1. Save API Key
2. View API Key
3. Delete API Key
4. List Services
5. Exit
: 1

Enter Service Name: OpenAI
Enter API Key: sk-openai-demo-123456789

Encrypted API Key saved: openai_1.key.enc
Key Code (save this): Sx9tmLx40VPRnR-UrP2BTDG_JDQ1_J3Z8bnrRfA79VM=
Vault updated: vault_keys.json
```
```
: 2

Enter Service Name: github
Enter Key Code: OZO_msLyVgtSsX7Lp_sHn9dzFg7xNRISNzpObDpmPRc=

-------------------
Service : github
API Key : ghp_demoGithubKey_987654
-------------------

```

---

## Features
- Secure API key encryption
- Separate encrypted vault files
- Unique filename handling
- Service listing system
- Wrong key protection
- Corrupted JSON handling
- Missing file cleanup support
- Beginner-friendly CLI menu system

---

## Project Structure
```
10_api_key_vault_manager/
├── data/
│   └── vault_keys.json
├── vault/
│   └── github.key.enc
|   └── openai.key.enc
├── main.py
└── README.md
```

---

## Notes
- This is an educational cybersecurity project.
- This project stores keys locally.
- Real systems never expose secret keys directly like this.
- Built for learning encryption, file handling, and secure storage basics.
