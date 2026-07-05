"""
Chat history system for the chatbot.

This module is responsible for saving user/bot conversations
in a persistent human readable file.
"""

from __future__ import annotations

from datetime import datetime
from pathlib import Path


class ChatHistory:
    """
    Stores chat conversations in a text file.
    """

    def __init__(self, history_file: Path) -> None:
        """
        Initialize chat history system.

        Parameters
        ----------
        history_file : Path
            File where conversations will be stored.
        """

        self.history_file = history_file
        self.history_file.parent.mkdir(parents=True, exist_ok=True)

    # ------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------

    def new_session(self) -> None:
        """
        Start a new conversation session.
        """

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with self.history_file.open("a", encoding="utf-8") as file:
            file.write("\n")
            file.write("=" * 60 + "\n")
            file.write(f"NEW SESSION : {timestamp}\n")
            file.write("=" * 60 + "\n")

    def log_user(self, message: str) -> None:
        """
        Log a user message.
        """

        self._write("USER", message)

    def log_bot(self, message: str) -> None:
        """
        Log a bot message.
        """

        self._write("BOT", message)

    # ------------------------------------------------------------
    # Internal method
    # ------------------------------------------------------------

    def _write(self, speaker: str, message: str) -> None:
        """
        Write a message into the history file.
        """

        timestamp = datetime.now().strftime("%H:%M:%S")

        with self.history_file.open("a", encoding="utf-8") as file:
            file.write(f"[{timestamp}] {speaker}: {message}\n")