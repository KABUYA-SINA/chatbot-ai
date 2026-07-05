"""
JSON storage implementation for the chatbot.

This module handles:
- reading and writing JSON data
- file initialization
- basic corruption safety
- structure validation

It is the default storage backend.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict

from .base import StorageBackend


class JsonStorage(StorageBackend):
    """
    JSON-based storage backend.
    """

    def __init__(self, source: Path) -> None:
        super().__init__(source)

    # ------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------

    def _read_file(self) -> Dict[str, Any]:
        """
        Safely read JSON file.

        Returns empty dict if file is missing or corrupted.
        """
        try:
            with self.source.open("r", encoding="utf-8") as f:
                return json.load(f)

        except FileNotFoundError:
            return {}

        except json.JSONDecodeError:
            # corrupted file fallback
            return {}

    def _write_file(self, data: Dict[str, Any]) -> None:
        """
        Write JSON data using atomic replacement strategy.
        """
        temp_file = self.source.with_suffix(".tmp")

        with temp_file.open("w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        temp_file.replace(self.source)

    # ------------------------------------------------------------
    # StorageBackend implementation
    # ------------------------------------------------------------

    def exists(self) -> bool:
        """
        Check if storage file exists.
        """
        return self.source.exists()

    def load(self) -> Dict[str, Any]:
        """
        Load data from storage.

        If file does not exist, create it with default structure.
        """
        if not self.exists():
            default_data = self._default_structure()
            self.initialize(default_data)
            return default_data

        data = self._read_file()

        return self._ensure_structure(data)

    def save(self, data: Dict[str, Any]) -> None:
        """
        Save data into JSON file.
        """
        if not isinstance(data, dict):
            raise TypeError("Storage data must be a dictionary")

        self._write_file(data)

    def initialize(self, default_data: Dict[str, Any]) -> None:
        """
        Create storage file with initial structure.
        """
        if not self.source.parent.exists():
            self.source.parent.mkdir(parents=True, exist_ok=True)

        self._write_file(default_data)

    # ------------------------------------------------------------
    # Validation
    # ------------------------------------------------------------

    def _ensure_structure(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Ensure required keys exist in stored data.
        """
        defaults = self._default_structure()

        for key, value in defaults.items():
            if key not in data:
                data[key] = value

        return data

    def _default_structure(self) -> Dict[str, Any]:
        """
        Default chatbot memory structure.
        """

        return {
            "metadata": {
                "version": "1.0.0",
                "last_updated": "",
                "created_at": ""
            },
            "languages": {
                "fr": {
                    "questions": [],
                    "facts": [],
                    "rules": [],
                    "learned_patterns": [],
                    "user_feedback": []
                },
                "en": {
                    "questions": [],
                    "facts": [],
                    "rules": [],
                    "learned_patterns": [],
                    "user_feedback": []
                }
            },
            "statistics": {
                "questions": 0,
                "facts": 0,
                "rules": 0,
                "feedback": 0
            }
        }