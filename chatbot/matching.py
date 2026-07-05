"""
Question matching module.

This module is responsible for finding the closest known question
to a user input using similarity scoring.

Current implementation uses difflib.SequenceMatcher for lightweight
fuzzy matching.
"""

from __future__ import annotations

from difflib import SequenceMatcher
from chatbot.utils import normalize_text
from config import MATCH_THRESHOLD


class QuestionMatcher:
    """
    Finds the best matching question based on similarity score.
    """

    def __init__(self, threshold: float = MATCH_THRESHOLD) -> None:
        """
        Initialize matcher.

        Parameters
        ----------
        threshold : float
            Minimum similarity score required to accept a match.
        """
        self.threshold = threshold

    # ------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------

    def find_best_match(
        self,
        user_input: str,
        questions: list[str]
    ) -> str | None:
        """
        Return the closest matching question or None if no match.
        """

        if not user_input or not questions:
            return None

        user_input = normalize_text(user_input)

        best_score = 0.0
        best_match = None

        for q in questions:
            normalized_q = normalize_text(q)

            score = SequenceMatcher(
                None,
                user_input,
                normalized_q
            ).ratio()

            if score > best_score:
                best_score = score
                best_match = q

        if best_score >= self.threshold:
            return best_match

        return None