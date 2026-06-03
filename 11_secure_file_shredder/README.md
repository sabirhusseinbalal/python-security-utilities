# Secure File Shredder

## Description
This project securely deletes files by overwriting their content before removing them.

Instead of deleting files normally, the program rewrites the file multiple times using random data and then permanently removes it.

This helps understand how secure deletion works in cybersecurity systems.

**YouTube Video:**
[[Secure File Shredder | Security, Encryption & Utilities (Project 11)](https://youtu.be/h_j2ffodntM?si=Rc1q2lATEwjEBVg1/)]

---

## What this project does
- Loads a file
- Reads file size
- Overwrites file data using random bytes
- Performs multiple overwrite passes
- Deletes the file permanently
- Simulates basic secure shredding behavior

---

## Modules Used
- `pathlib` → file handling
- `os` → random byte generation
- `time` → delay simulation

---

## Output Example
```
Enter file path (or 'q'): 
No path provided — using default file: story.txt
File Loaded: story.txt

File Size: 0 Bytes

Overwriting file...
Pass 1 completed...
Pass 2 completed...
Pass 3 completed...

File shredded successfully!
```

---

## Features
- Multi-pass overwrite system
- Random byte shredding
- Permanent file deletion
- Default file support
- Simple CLI interface
- Beginner-friendly logic

---

## Project Structure
```
11_secure_file_shredder/
├── input/
│   └── story.txt
├── main.py
└── README.md
```

---

## Notes
- Normal deletion does not always remove real file data.
- Overwriting makes file recovery much harder.
- Modern SSD storage behaves differently internally.
- Built for learning secure deletion and file handling basics.
