# SSL Expiry Monitor

## Description
This project checks SSL certificates of websites and monitors their expiry dates.

It connects securely to a domain, reads SSL certificate information, and shows whether the certificate is still valid or close to expiring.

This helps understand how HTTPS security and certificate monitoring work in real systems.

**YouTube Video:**
[[SSL Expiry Monitor | Security, Encryption & Utilities (Project 12)](https://youtu.be/itsWb6skvlk?si=kzaDheIEE5BpihPN/)]

---

## What this project does
- Connects to a website securely
- Reads SSL certificate information
- Extracts certificate issuer details
- Checks certificate expiry date
- Calculates remaining valid days
- Detects expired or expiring certificates

---

## Modules Used
- `ssl` → secure SSL connection
- `socket` → network connection
- `datetime` → expiry date calculation

---

## Output Example
```
Enter URL (or 'q'): https://google.com

Scanning google.com (142.250.186.238)...

Checking SSL certificate...

Domain: google.com
countryName: US
organizationName: Google Trust Services
commonName: WR2
Valid From : Apr 20 08:35:05 2026 GMT
Expiry Date: Jul 13 08:35:04 2026 GMT
Days Left  : 64
Certificate Status: VALID
```

---

## Features
- SSL certificate scanning
- Domain to IP resolution
- Expiry date monitoring
- Expiring-soon warning system
- Secure HTTPS connection
- Simple CLI interface

---

## Project Structure
```
12_ssl_expiry_monitor/
├── main.py
└── README.md
```

---

## Notes
- HTTPS websites use SSL certificates for secure communication.
- Expired certificates can trigger browser security warnings.
- Real systems monitor certificates automatically before expiry.
- Built for learning networking, SSL, and security monitoring basics.
