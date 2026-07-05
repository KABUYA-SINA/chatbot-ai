"""
Console interface for the chatbot.

This module provides a command-line interface
to interact with the ChatEngine.
"""

from __future__ import annotations

from chatbot.engine import ChatEngine


class ConsoleInterface:
    """
    CLI interface for chatbot interaction.
    """

    def __init__(self) -> None:
        self.engine = ChatEngine(test_mode=False)

    # ------------------------------------------------------------
    # Main loop
    # ------------------------------------------------------------

    def run(self) -> None:
        """
        Start interactive console session.
        """

        print("=" * 50)
        print("           CHATBOT AI - CONSOLE MODE")
        print("Type 'quit', 'exit' or 'q' to stop")
        print("=" * 50)

        while True:
            try:
                user_input = input("\nYou: ")

                if user_input is None:
                    continue

                user_input = user_input.strip()

                if not user_input:
                    print("Bot: Please enter a message.")
                    continue

                if user_input.lower() in ("quit", "exit", "q"):
                    print("Bot: Goodbye!")
                    break

                response = self.engine.process(user_input)

                print(f"Bot: {response}")

            except KeyboardInterrupt:
                print("\nBot: Interrupted. Goodbye!")
                break

            except EOFError:
                print("\nBot: Session closed. Goodbye!")
                break

            except Exception as e:
                print(f"Bot: Error occurred: {str(e)}")