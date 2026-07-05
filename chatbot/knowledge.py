"""
Central knowledge manager of the chatbot.

This module is the single source of truth for all stored data :
- questions & answers
- facts
- rules
- learned patterns
- user feedback

It communicates only with the storage layer via StorageManager.
"""

from __future__ import annotations

from typing import Any, Dict, List

from config import KNOWLEDGE_BASE_FILE
from storage.manager import StorageManager


class KnowledgeBase:
    """
    Central access point for chatbot memory.
    """

    def __init__(self) -> None:
        """
        Initialize knowledge base using StorageManager.
        """
        self.storage = StorageManager(KNOWLEDGE_BASE_FILE, backend="json")
        self.data: Dict[str, Any] = self.storage.load()

    # ------------------------------------------------------------
    # Core access
    # ------------------------------------------------------------

    def reload(self) -> None:
        """
        Reload data from storage.
        """
        self.data = self.storage.load()

    def save(self) -> None:
        """
        Persist current state into storage.
        """
        self.storage.save(self.data)

    # ------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------

    def _get_lang_block(self, lang: str) -> Dict[str, Any]:
        """
        Get or create language block safely.
        """

        languages = self.data.get("languages", {})

        if lang not in languages:
            languages[lang] = {
                "questions": [],
                "facts": [],
                "rules": [],
                "learned_patterns": [],
                "user_feedback": []
            }

        return languages[lang]
    
    # ------------------------------------------------------------
    # Questions
    # ------------------------------------------------------------

    def get_questions(self, lang: str) -> List[Dict[str, str]]:
        """
        Return all questions for a given language.
        """
        return self._get_lang_block(lang).get("questions", [])

    def add_question(self, lang: str, question: str, answer: str) -> None:
        """
        Add a new question/answer pair to the knowledge base.
        """
        block = self._get_lang_block(lang)

        block["questions"].append({
            "question": question,
            "answer": answer
        })

        self.save()

    # ------------------------------------------------------------
    # Facts
    # ------------------------------------------------------------

    def add_fact(self, lang: str, fact: str) -> None:
        """
        Store a fact for a specific language.
        """
        block = self._get_lang_block(lang)
        block["facts"].append(fact)
        self.save()

    def get_facts(self, lang: str) -> List[str]:
        """
        Return stored facts.
        """
        return self._get_lang_block(lang).get("facts", [])

    # ------------------------------------------------------------
    # Rules
    # ------------------------------------------------------------

    def add_rule(self, lang: str, rule: str) -> None:
        """
        Store a rule that influences chatbot behavior.
        """
        block = self._get_lang_block(lang)
        block["rules"].append(rule)
        self.save()

    def get_rules(self, lang: str) -> List[str]:
        """
        Return rules for a language.
        """
        return self._get_lang_block(lang).get("rules", [])

    # ------------------------------------------------------------
    # Learned patterns
    # ------------------------------------------------------------

    def add_pattern(self, lang: str, pattern: str) -> None:
        """
        Store a learned pattern from user interactions.
        """
        block = self._get_lang_block(lang)
        block["learned_patterns"].append(pattern)
        self.save()

    def get_patterns(self, lang: str) -> List[str]:
        """
        Return learned patterns.
        """
        return self._get_lang_block(lang).get("learned_patterns", [])

    # ------------------------------------------------------------
    # User feedback
    # ------------------------------------------------------------

    def add_feedback(self, lang: str, feedback: str) -> None:
        """
        Store user feedback.
        """
        block = self._get_lang_block(lang)
        block["user_feedback"].append(feedback)
        self.save()

    def get_feedback(self, lang: str) -> List[str]:
        """
        Return stored feedback.
        """
        return self._get_lang_block(lang).get("user_feedback", [])