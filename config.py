"""
Application configuration.

This module centralizes project paths and global settings used
across the chatbot application.
"""

from pathlib import Path

# ---------------------------------------------------------------------
# Project directories
# ---------------------------------------------------------------------

ROOT_DIR = Path(__file__).resolve().parent

DATA_DIR = ROOT_DIR / "data"

LOG_DIR = ROOT_DIR / "logs"

# ---------------------------------------------------------------------
# Knowledge base
# ---------------------------------------------------------------------

KNOWLEDGE_BASE_FILE = DATA_DIR / "knowledge_base.json"

# ---------------------------------------------------------------------
# Matching configuration
# ---------------------------------------------------------------------

MATCH_THRESHOLD = 0.70

# ---------------------------------------------------------------------
# Chat history
# ---------------------------------------------------------------------

CHAT_HISTORY_FILE = LOG_DIR / "chat_history.txt"

# ---------------------------------------------------------------------
# Language configuration
# ---------------------------------------------------------------------

SUPPORTED_LANGUAGES = [
    "fr",
    "en",
    "es",
    "de",
    "it",
    "pt",
]

DEFAULT_LANGUAGE = "en"