"""
Storage backend abstraction layer.

This module defines the contract that all storage implementations
must follow (JSON, SQL, NoSQL, etc.).

It ensures that the chatbot core remains independent from
any storage technology.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any


class StorageBackend(ABC):
    """
    Abstract base class for storage implementations.

    All storage systems must implement this interface.
    """

    def __init__(self, source: Path) -> None:
        """
        Initialize storage backend.

        Parameters
        ----------
        source : Path
            Path or identifier of the storage resource.
        """
        self._source = source

    @property
    def source(self) -> Path:
        """
        Return storage source path.
        """
        return self._source

    # ------------------------------------------------------------
    # Required interface
    # ------------------------------------------------------------

    @abstractmethod
    def exists(self) -> bool:
        """
        Check if storage resource exists.
        """
        raise NotImplementedError

    @abstractmethod
    def load(self) -> dict[str, Any]:
        """
        Load and return stored data.
        """
        raise NotImplementedError

    @abstractmethod
    def save(self, data: dict[str, Any]) -> None:
        """
        Save data into storage.
        """
        raise NotImplementedError

    @abstractmethod
    def initialize(self, default_data: dict[str, Any]) -> None:
        """
        Initialize storage with default structure.
        """
        raise NotImplementedError