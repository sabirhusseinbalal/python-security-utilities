# File Integrity Checker (SHA256)

## Description
This project checks whether a file has been changed or not using hashing.

It generates a hash value for a file and compares it with previously saved data.

If the file content changes even slightly, the hash will change completely.

This helps understand how file integrity works in real-world systems.

---

## What this project does
- Reads a file
- Generates a hash (fingerprint)
- Stores hash in JSON file
- Compares current vs previous hash
- Detects if file is modified

---

## Modules Used
- `hashlib` – for generating hash
- `json` – for storing data
- `pathlib` – for file handling

---

## Output Example
```
Enter full file path (or 'q' to quit):

No path provided — using default file: sample.txt
File Loaded: sample.txt
File ID: e4b8979c58f189d5fdc4610e544418673cc6fde4c4853b57c3a70400dc67b562
Hash: def3330d41ebaad336348d1224a7a9d5eb049311224a58f4d547e179902e0e42
```
```
No changes detected
```
**OR**
```
File content changed!
```
**OR**
```
New file detected — saving hash
```
```
Data saved in data.json

Enter full file path (or 'q' to quit): q

Exiting...
```

---

## Features
- Checks file integrity using hashing
- Detects even small changes in file
- Stores data in JSON file
- Simple command-line interaction
- Uses default file if no path is given

---

## Project Structure
```
01_file_integrity_checker/
├── input/
│ └── sample.txt
├── data/
│ └── data.json
├── main.py
└── README.md
```

---

## Notes
- Even one changed character creates a completely different hash
- Hashing is widely used for integrity checking and malware detection
- Real systems often compare hashes to detect tampering
- Built step-by-step to understand how trust and verification work in security
