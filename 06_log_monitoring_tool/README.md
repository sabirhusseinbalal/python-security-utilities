# Log Monitoring Tool (Security Basics)

## Description
This project reads system log files and detects suspicious activities like failed login attempts and sensitive file access.

It simulates a basic security monitoring system similar to how real SOC (Security Operations Center) tools analyze logs.

**YouTube Video:**
[[Log Monitoring Tool (Security Basics) | Security, Encryption & Utilities (Project 6)](https://youtu.be/H3wAetw375c?si=CJ1fW28PRg_hAW7t/)]

---

## What this project does
- Reads .log files line by line
- Detects:
   - Login failures
   - Login success
   - Sensitive file access (like admin files)
- Tracks user behavior (fail/success counts)
- Flags suspicious users

---

## Modules Used
- `pathlib` – file handling

---

## Input Format (log file example)
```
LOGIN SUCCESS user=sabir
LOGIN FAIL user=ali
LOGIN FAIL user=ali
LOGIN FAIL user=ali
LOGIN SUCCESS user=admin
FILE ACCESS file=admin_panel.py
LOGIN FAIL user=unknown
LOGIN FAIL user=unknown
LOGIN FAIL user=unknown
```

---

## Output Example
```
Enter file path (or 'q'): 
No path provided — using default file: system.log
File Loaded: system.log

[WARNING] user: ali login attempt detected
[WARNING] user: ali login attempt detected
[WARNING] user: ali login attempt detected

[ALERT] Sensitive file accessed: admin_panel.py
[WARNING] Unknown user login attempt detected
[WARNING] Unknown user login attempt detected
[WARNING] Unknown user login attempt detected


[INFO] Scanning logs...

[ALERT] User `ali` blocked (3 failed logins)
[ALERT] User `unknown` blocked (3 failed logins)

User: sabir
SUCCESS: 1 | FAIL: 0
sabir --> Normal

User: ali
SUCCESS: 0 | FAIL: 3
ali --> Suspicious activity

User: admin
SUCCESS: 1 | FAIL: 0
admin --> Normal

User: unknown
SUCCESS: 0 | FAIL: 3
unknown --> Suspicious activity
```

---


## Features
- User-based tracking system
- Failed login detection system
- Sensitive file access detection
- Suspicious behavior analysis
- Simple CLI interface

---

## Project Structure
```
06_log_monitoring_tool/
├── logs/
│   └── system.log
├── main.py
└── README.md
```

---

## Notes
- Security teams often monitor logs to detect suspicious behavior
- Repeated failures can indicate brute-force attempts
- Real monitoring systems use much more advanced detection rules
- Built to understand the basics of security event analysis
