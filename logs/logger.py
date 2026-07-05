"""
Central logging system for the chatbot.

This module provides a lightweight logger used across:
- ChatEngine
- Storage layer
- Learning system

It ensures consistent logging format without external dependencies.
"""

from __future__ import annotations

import logging
from pathlib import Path


class Logger:
    """
    Simple wrapper around Python logging module.

    Provides a consistent logging interface for the project.
    """

    def __init__(self, name: str = "chatbot", log_file: Path | None = None) -> None:
        """
        Initialize logger.

        Parameters
        ----------
        name : str
            Logger name.
        log_file : Path | None
            Optional file path for persistent logs.
        """

        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)

        # Avoid duplicate handlers
        if not self.logger.handlers:

            formatter = logging.Formatter(
                "[%(asctime)s] [%(levelname)s] %(message)s"
            )

            # Console handler
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(formatter)
            self.logger.addHandler(console_handler)

            # File handler (-> optional)
            if log_file is not None:
                log_file.parent.mkdir(parents=True, exist_ok=True)

                file_handler = logging.FileHandler(log_file, encoding="utf-8")
                file_handler.setFormatter(formatter)
                self.logger.addHandler(file_handler)

    # ------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------

    def info(self, message: str) -> None:
        self.logger.info(message)

    def warning(self, message: str) -> None:
        self.logger.warning(message)

    def error(self, message: str) -> None:
        self.logger.error(message)

    def debug(self, message: str) -> None:
        self.logger.debug(message)