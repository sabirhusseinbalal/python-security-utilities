# Port Scanner (Educational)

## Description
This tool scans a target domain or IP address and checks which ports are open or closed.

It simulates how basic network reconnaissance works in cybersecurity.

**YouTube Video:**
[[Port Scanner (Educational) | Security, Encryption & Utilities (Project 7)](https://youtu.be/pqapWsdnFcY?si=grRzPncuiI03gr9K/)]

---

## What this project does
- Takes a website or IP address as input
- Extracts the domain and resolves it to an IP
- Scans a predefined list of ports
- Checks whether each port is open or closed using TCP connection
- Displays scan results in real time

---

## Modules Used
- `socket` – for network connection and port scanning

---

## Output Example
```
Enter URL (or 'q'): google.com

Scanning google.com (142.250.202.174)...

[CLOSED] Port 75
[CLOSED] Port 76
[CLOSED] Port 77
[CLOSED] Port 78
[CLOSED] Port 79
[OPEN] Port 80
[CLOSED] Port 81
[OPEN] Port 443
[CLOSED] Port 22
[CLOSED] Port 3306
Scan Complete!

Enter URL (or 'q'): 
```

---

## Features
- Domain to IP resolution
- TCP port connectivity check
- Handles invalid domains safely
- Timeout support for faster scanning
- Simple CLI-based interface

---

## Project Structure
```
07_port_scanner_educational/
├── main.py
└── README.md
```

---

## Notes
- Open ports can reveal exposed services on a system
- Firewalls may hide or block scan results
- Ethical scanning should only be done on authorized systems
- Built to learn how basic network reconnaissance works
