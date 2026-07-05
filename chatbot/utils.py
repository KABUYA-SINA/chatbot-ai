"""
Global text normalization utilities.

This module provides a shared function used across:
- matching
- learning
- storage consistency

It ensures that all text follows a uniform format before processing.
"""

import re
import unicodedata


def normalize_text(text: str) -> str:
    """
    Normalize input text for consistent processing.

    Steps:
    - lowercase conversion
    - trim spaces
    - remove accents
    - remove punctuation
    - normalize whitespace
    """

    if not text:
        return ""

    text = text.lower().strip()

    # Normalize unicode characters (é -> e, etc.)
    text = unicodedata.normalize("NFD", text)
    text = "".join(
        c for c in text
        if unicodedata.category(c) != "Mn"
    )

    # Replace punctuation with spaces (keep letters and numbers)
    text = re.sub(r"[^\w\s]", " ", text)

    # Normalize multiple spaces into one
    text = re.sub(r"\s+", " ", text).strip()

    return text