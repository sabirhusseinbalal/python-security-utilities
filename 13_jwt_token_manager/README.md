# JWT Token Manager

## Description
This project creates and validates JWT tokens using a secret key.

Each token contains user information, issue time, and expiry time.

The system checks whether the token is still valid, expired, or signed with the wrong secret key.

This helps understand how authentication tokens work in backend systems and APIs.

---

## What this project does
- Creates JWT tokens
- Adds expiry time to tokens
- Verifies token signatures
- Detects expired tokens
- Deletes saved tokens
- Lists stored tokens
- Stores token data in JSON

---

## Modules Used
- `jwt (PyJWT)` → token creation and verification
- `datetime` → expiry handling
- `json` → token storage
- `pathlib` → file handling
- `string` → cleaning token names

---

## Output Example
**Create Token**
```
1. Create Token
2. Validate Token
3. Delete Token
4. List Tokens
5. Exit
: 1

Token Name: github_token
Subject/User: sabir
Secret Key: mysecretkey1234567890123456
Expiry (minutes): 30

Token created successfully!
Saved to vault
```
**Validate Token**
```
: 2

Token Name: githubtoken
Secret Key: mysecretkey1234567890123456

VALID TOKEN

{
    'sub': 'sabir',
    'token_name': 'githubtoken',
    'iat': 1778324711,
    'exp': 1778326511
}
```
**Wrong Secret**
```
Wrong secret key
```
**Expired Token**
```
Token expired
```
---

## Features
- JWT token generation
- Expiry time validation
- Signature verification
- Wrong key detection
- Token deletion system
- JSON token storage
- Simple CLI menu

---

## Project Structure
```
13_jwt_token_manager/
├── data/
│   └── tokens.json
├── main.py
└── README.md
```

---

## Notes
- This is an educational authentication project.
- Tokens become invalid automatically after expiry.
- Secret keys are required for verification.
- Built for learning JWT flow and token validation basics.
