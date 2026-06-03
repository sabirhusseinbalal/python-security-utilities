# JWT Token Validator

## Description
This project is a simple JWT (JSON Web Token) analyzer built in Python.

It helps understand how JWT tokens work internally by:

- Decoding token data
- Checking expiration time
- Verifying token signature using a secret key

This is a learning project to understand authentication concepts used in real-world backend systems.

**YouTube Video:**
[[JWT Token Validator | Security, Encryption & Utilities (Project 4)](https://youtu.be/tmD1xNusmss?si=CGwJVOqt21I-3RDN/)]

---

## What this project does
- Takes a JWT token as input
- Decodes payload without verification
- Shows user data inside token
- Checks if token is expired
- Verifies token using secret key
- Shows final status (valid / expired / invalid)

---

## Modules Used
- `jwt (pyjwt)` – token decoding & verification
- `datetime` – time & expiry checking

---

## Output Example
```
Enter token (or 'q'): eyJhb...

--- Payload ---
user: sabirhusseinbalal
name: Sabir Hussain
iat: 1777980102
exp: 1778066740
```
```
Status: VALID

--- Verification ---
Token Verified
```
**OR**
```
Status: EXPIRED

--- Verification ---
Invalid signature or wrong secret
Token NOT Verified
```
---


## Concepts Learned
- What JWT token is
- Header, Payload, Signature structure
- Why decoding is different from verification
- Role of secret key in security
- Expiration handling (exp)
- Basic authentication logic

---

## Project Structure
```
04_jwt_token_validator/
├── main.py
└── README.md
```

---

## Notes
- JWT payload data is readable even without the secret key
- Verification is what proves whether a token is trusted
- Expired tokens should never be accepted
- Built to understand how authentication works behind modern web apps
