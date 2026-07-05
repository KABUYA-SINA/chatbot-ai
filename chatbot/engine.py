"""
Core chatbot engine.

This module coordinates the different components of the chatbot.
It manages the conversation flow without implementing the business
logic of individual modules.
"""

from __future__ import annotations

from chatbot.knowledge import KnowledgeBase
from chatbot.language import LanguageDetector
from chatbot.learning import LearningEngine
from chatbot.matching import QuestionMatcher
from chatbot.rules import RuleEngine
from logs.logger import Logger
from logs.chat_history import ChatHistory
from config import CHAT_HISTORY_FILE


class ChatEngine:
    """
    Central coordinator of the chatbot.
    """

    def __init__(self, test_mode: bool = False) -> None:
        """
        Initialize all chatbot components.

        Parameters
        ----------
        test_mode : bool, optional
            Disable interactive learning during automated tests.
        """

        self.language_detector = LanguageDetector()
        self.matcher = QuestionMatcher()
        self.knowledge = KnowledgeBase()
        self.learning = LearningEngine(self.knowledge)
        self.rules = RuleEngine()
        self.logger = Logger()
        self.history = ChatHistory(CHAT_HISTORY_FILE)
        self.history.new_session()
        self.test_mode = test_mode

    # -----------------------------------------------------------------
    # Main processing
    # -----------------------------------------------------------------

    def process(self, user_input: str) -> str:
        """
        Process a user message and return a chatbot response.
        """

        if not user_input or not user_input.strip():
            return "Please enter a message."

        self.history.log_user(user_input)

        lang = self.language_detector.detect(user_input)

        questions = self.knowledge.get_questions(lang)
        question_texts = [q["question"] for q in questions]

        best_match = self.matcher.find_best_match(
            user_input,
            question_texts,
        )

        if best_match:
            response = self._get_answer(questions, best_match)
            response = self.rules.apply(response)

            self.logger.info(f"Matched question: {best_match}")
            self.history.log_bot(response)

            return response

        response = self._handle_learning(lang, user_input)
        self.history.log_bot(response)
        return response

    # -----------------------------------------------------------------
    # Internal helpers
    # -----------------------------------------------------------------

    def _get_answer(
        self,
        questions: list[dict[str, str]],
        best_match: str,
    ) -> str:
        """
        Return the answer associated with a matched question.
        """

        for q in questions:
            if q["question"] == best_match:
                return q["answer"]

        return "I found a match but no answer was linked."

    def _handle_learning(self, lang: str, user_input: str) -> str:
        """
        Handle unknown questions through the learning system.
        """

        self.logger.warning("Unknown input. Switching to learning mode.")

        if self.test_mode:
            return "TEST_MODE_NO_LEARNING"

        print("Bot: I don't know this yet. Teach me!")

        answer = input("Your answer: ").strip()

        if not answer:
            return "Learning skipped."

        success = self.learning.learn_question(
            lang=lang,
            question=user_input,
            answer=answer,
        )

        if success:
            self.logger.info("New knowledge learned successfully")
            return "Got it. I learned something new !"

        return "I couldn't learn this input."