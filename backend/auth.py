"""Registration and authentication helpers for the WUA cafeteria prototype."""
from __future__ import annotations
import hashlib, hmac, os, re

_EMAIL = re.compile(r"^[^\s@]+@[^\s@]+\.[^\s@]+$")
_USERS: dict[str, dict[str, str]] = {}

def hash_password(password: str, salt: bytes | None = None) -> str:
    """Return a salted PBKDF2-SHA256 digest; the encoded value stores salt and digest."""
    salt = salt or os.urandom(16)
    digest = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, 240_000)
    return f"{salt.hex()}${digest.hex()}"

def _verify(password: str, encoded: str) -> bool:
    try:
        salt_hex, expected = encoded.split("$", 1)
        actual = hashlib.pbkdf2_hmac("sha256", password.encode(), bytes.fromhex(salt_hex), 240_000).hex()
        return hmac.compare_digest(actual, expected)
    except (ValueError, TypeError):
        return False

def register_user(name: str, email: str, student_id: str, password: str) -> dict[str, str]:
    """Validate and register a unique campus user; never return the password hash."""
    name, email, student_id = name.strip(), email.strip().lower(), student_id.strip()
    if not name or not student_id or len(password) < 8:
        raise ValueError("Name and student ID are required; password must be at least 8 characters")
    if not _EMAIL.fullmatch(email):
        raise ValueError("A valid email address is required")
    if email in _USERS:
        raise ValueError("An account with this email already exists")
    _USERS[email] = {"name": name, "email": email, "student_id": student_id, "password_hash": hash_password(password)}
    return {k: _USERS[email][k] for k in ("name", "email", "student_id")}

def login_user(email: str, password: str) -> dict[str, str] | None:
    """Return the safe user profile on success, otherwise None."""
    user = _USERS.get(email.strip().lower())
    if not user or not _verify(password, user["password_hash"]):
        return None
    return {k: user[k] for k in ("name", "email", "student_id")}