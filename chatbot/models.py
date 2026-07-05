"""
Data models for the chatbot system.

These models provide a structured representation of
core entities used across the application.
"""

from dataclasses import dataclass


@dataclass
class QuestionModel:
    """
    Represents a question/answer pair stored in the knowledge base.
    """

    question: str
    answer: str
    lang: str = "en"


@dataclass
class FactModel:
    """
    Represents a stored fact.
    """

    fact: str
    lang: str = "en"


@dataclass
class RuleModel:
    """
    Represents a rule applied to chatbot responses.
    """

    rule: str