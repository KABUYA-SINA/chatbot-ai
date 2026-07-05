"""
Learning module of the chatbot.

This module handles the ingestion of new knowledge:
- validation of inputs
- duplicate checking
- normalization
- safe storage through KnowledgeBase

It is separated from the core engine to isolate learning logic.
"""

from __future__ import annotations

from chatbot.knowledge import KnowledgeBase
from chatbot.utils import normalize_text


class LearningEngine:
    """
    Responsible for adding new knowledge safely into the system.
    """

    def __init__(self, knowledge: KnowledgeBase) -> None:
        """
        Initialize learning engine.

        Parameters
        ----------
        knowledge : KnowledgeBase
            Shared memory system.
        """
        self.knowledge = knowledge

    # ------------------------------------------------------------
    # PUBLIC API
    # ------------------------------------------------------------

    def learn_question(
        self,
        lang: str,
        question: str,
        answer: str
    ) -> bool:
        """
        Add a new question/answer pair to the knowledge base.

        Returns True if learning succeeded, False otherwise.
        """

        question = normalize_text(question)
        answer = normalize_text(answer)

        existing = self.knowledge.get_questions(lang)

        # --------------------------------------------------------
        # Duplicate detection
        # --------------------------------------------------------

        for q in existing:
            if normalize_text(q["question"]) == question:
                return False

        # --------------------------------------------------------
        # Validation
        # --------------------------------------------------------

        if not self._is_valid(question, answer):
            return False

        self.knowledge.add_question(
            lang=lang,
            question=question,
            answer=answer
        )

        return True

    # ------------------------------------------------------------
    # Validation logic
    # ------------------------------------------------------------

    def _is_valid(self, question: str, answer: str) -> bool:
        """
        Validate learning input before storing it.
        """

        if not question or not answer:
            return False

        if len(question.strip()) < 2:
            return False

        if len(answer.strip()) < 1:
            return False

        if question == answer:
            return False

        return True