"""
Application entry point.

This module starts the chatbot in console mode by initializing
the console interface and launching the interaction loop.
"""

from __future__ import annotations

from interfaces.console import ConsoleInterface


def main() -> None:
    """
    Start the chatbot application.
    """
    app = ConsoleInterface()
    app.run()


if __name__ == "__main__":
    main()