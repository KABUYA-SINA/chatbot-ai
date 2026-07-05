"""
Central storage manager for the chatbot system.

This class acts as a single entry point for all storage operations.
It hides the underlying backend implementation (JSON, SQL, etc.)
from the rest of the application.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, Optional

from .json_storage import JsonStorage
from .base import StorageBackend


class StorageManager:
    """
    Unified interface for storage operations.

    The chatbot engine interacts ONLY with this class.
    """

    def __init__(self, source: Path, backend: str = "json") -> None:
        """
        Initialize storage manager.

        Parameters
        ----------
        source : Path
            Path to storage file or resource.
        backend : str
            Storage backend type (default: json).
        """

        self._backend_name = backend.lower()
        self._backend: StorageBackend = self._create_backend(source)

    # ------------------------------------------------------------
    # Backend factory
    # ------------------------------------------------------------

    def _create_backend(self, source: Path) -> StorageBackend:
        """
        Instantiate the correct storage backend.
        """

        if self._backend_name == "json":
            return JsonStorage(source)

        raise ValueError(f"Unsupported storage backend: {self._backend_name}")

    # ------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------

    def load(self) -> Dict[str, Any]:
        """
        Load data from storage.
        """
        return self._backend.load()

    def save(self, data: Dict[str, Any]) -> None:
        """
        Save data into storage.
        """
        self._backend.save(data)

    def exists(self) -> bool:
        """
        Check if storage exists.
        """
        return self._backend.exists()

    def initialize(self, default_data: Optional[Dict[str, Any]] = None) -> None:
        """
        Initialize storage safely.

        If no default data is provided, use backend defaults.
        """

        if default_data is None:
            # fallback: rely on backend default structure safely
            default_data = self._get_default_structure()

        self._backend.initialize(default_data)

    # ------------------------------------------------------------
    # Safe abstraction helper
    # ------------------------------------------------------------

    def _get_default_structure(self) -> Dict[str, Any]:
        """
        Retrieve default structure safely from backend if possible.
        """

        # Avoid direct access to private backend methods
        if hasattr(self._backend, "_default_structure"):
            # controlled internal fallback
            return self._backend._default_structure()

        return {
            "metadata": {},
            "languages": {},
            "statistics": {}
        }