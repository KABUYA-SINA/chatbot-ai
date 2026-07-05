"""
Simple language detection module.

This module identifies the language of a user input using lightweight
heuristics. It routes queries to the appropriate dataset.

Supported languages:
- fr (French)
- en (English)
- es (Spanish)
- de (German)
- it (Italian)
- pt (Portuguese)

This implementation is rule-based and does not rely on ML models.
"""

from __future__ import annotations

import re
from typing import Dict


class LanguageDetector:
    """
    Detect language using keyword-based heuristics.
    """

    def __init__(self) -> None:
        """
        Initialize language keyword patterns.
        """

        self._patterns: Dict[str, list[str]] = {
            "fr": [
                "bonjour", "salut", "merci", "comment", "pourquoi",
                "je", "tu", "nous", "vous", "est", "sont"
            ],
            "en": [
                "hello", "hi", "thanks", "what", "why",
                "i", "you", "we", "are", "is"
            ],
            "es": [
                "hola", "gracias", "como", "por que", "yo",
                "tu", "nosotros", "es", "son"
            ],
            "de": [
                "hallo", "danke", "wie", "warum", "ich",
                "du", "wir", "ist", "sind"
            ],
            "it": [
                "ciao", "grazie", "come", "perché", "io",
                "tu", "noi", "è", "sono"
            ],
            "pt": [
                "olá", "obrigado", "como", "por que", "eu",
                "você", "nós", "é", "são"
            ],
        }

    # ------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------

    def detect(self, text: str) -> str:
        """
        Detect language from input text.

        Returns language code (fr, en, es, de, it, pt).
        """

        if not text:
            return "en"

        text = text.lower()

        scores: Dict[str, int] = {lang: 0 for lang in self._patterns}

        for lang, words in self._patterns.items():
            for word in words:
                if re.search(rf"\b{re.escape(word)}\b", text):
                    scores[lang] += 1

        best_language = max(scores, key=scores.get)

        if scores[best_language] == 0:
            return "en"

        return best_language