"""Form validation helpers."""

import re


EMAIL_PATTERN = re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")
MOBILE_PATTERN = re.compile(r"^[6-9]\d{9}$")


def validate_name(name: str) -> tuple[bool, str]:
    cleaned = (name or "").strip()
    if len(cleaned) < 2:
        return False, "Please enter your full name (at least 2 characters)."
    if not re.match(r"^[A-Za-z][A-Za-z\s.'-]{1,79}$", cleaned):
        return False, "Name should contain letters only."
    return True, ""


def validate_mobile(mobile: str) -> tuple[bool, str]:
    cleaned = re.sub(r"[\s\-()]", "", (mobile or "").strip())
    if cleaned.startswith("+91"):
        cleaned = cleaned[3:]
    elif cleaned.startswith("91") and len(cleaned) == 12:
        cleaned = cleaned[2:]
    if not MOBILE_PATTERN.match(cleaned):
        return False, "Enter a valid 10-digit Indian mobile number."
    return True, cleaned


def validate_email(email: str, required: bool = False) -> tuple[bool, str]:
    cleaned = (email or "").strip()
    if not cleaned:
        if required:
            return False, "Email is required."
        return True, ""
    if not EMAIL_PATTERN.match(cleaned):
        return False, "Enter a valid email address."
    return True, cleaned
