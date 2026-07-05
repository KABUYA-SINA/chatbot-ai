"""
Custom exceptions used throughout the chatbot application.

Defining project-specific exceptions makes error handling clearer
and allows different modules to communicate failures consistently.
"""


class ChatbotError(Exception):
    """
    Base exception for all chatbot-related errors.
    """

    pass


class StorageError(ChatbotError):
    """
    Raised when a storage operation fails.
    """

    pass


class KnowledgeError(ChatbotError):
    """
    Raised when an operation on the knowledge base fails.
    """

    pass


class LanguageDetectionError(ChatbotError):
    """
    Raised when language detection cannot be completed.
    """

    pass


class MatchingError(ChatbotError):
    """
    Raised when the matching process encounters an error.
    """

    pass