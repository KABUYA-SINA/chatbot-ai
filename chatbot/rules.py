"""
Rule engine for chatbot responses.

This module applies post-processing rules to chatbot outputs.
It ensures that responses follow basic formatting and safety rules.
"""

from __future__ import annotations


class RuleEngine:
    """
    Applies simple transformation rules to chatbot responses.
    """

    def __init__(self) -> None:
        """
        Initialize rule pipeline.
        """
        self.rules = [
            self._no_empty_response,
            self._format_response
        ]

    # ------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------

    def apply(self, response: str) -> str:
        """
        Apply all rules sequentially to a response.
        """

        for rule in self.rules:
            response = rule(response)

        return response

    # ------------------------------------------------------------
    # Rules
    # ------------------------------------------------------------

    def _no_empty_response(self, response: str) -> str:
        """
        Ensure chatbot never returns an empty response.
        """

        if not response or response.strip() == "":
            return "I don't have an answer yet."

        return response

    def _format_response(self, response: str) -> str:
        """
        Clean whitespace from response.
        """

        return response.strip()