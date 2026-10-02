import re


PROMPT_INJECTION_PATTERNS = [
    r"ignore previous instructions",
    r"ignore all instructions",
    r"system prompt",
    r"reveal your prompt",
    r"developer message",
    r"bypass your rules",
    r"disregard instructions",
]


RESTRICTED_BANKING_PATTERNS = [
    "guarantee my loan",
    "guarantee loan approval",
    "guarantee approval",
    "guaranteed loan",
    "approve my loan",
    "bypass verification",
    "bypass loan verification",
    "fake documents",
    "forge documents",
]


def detect_prompt_injection(text):

    text_lower = text.lower()

    for pattern in PROMPT_INJECTION_PATTERNS:

        if re.search(pattern, text_lower):

            return {
                "blocked": True,
                "reason": "PROMPT_INJECTION"
            }

    return {
        "blocked": False,
        "reason": None
    }


def detect_restricted_request(text):

    text_lower = text.lower()

    for phrase in RESTRICTED_BANKING_PATTERNS:

        if phrase in text_lower:

            return {
                "blocked": True,
                "reason": "RESTRICTED_BANKING_REQUEST"
            }

    return {
        "blocked": False,
        "reason": None
    }


def scan_pii(text):

    patterns = {

        "email": r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b",

        "phone": r"\b(?:\+91[-\s]?)?[6-9]\d{9}\b",

        "pan": r"\b[A-Z]{5}[0-9]{4}[A-Z]\b",

    }

    detected = []

    for name, pattern in patterns.items():

        if re.search(pattern, text):

            detected.append(name)

    return {
        "contains_pii": len(detected) > 0,
        "types": detected
    }