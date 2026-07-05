# 🤖 Chatbot — Learning System

![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-API-green.svg)
![Status](<https://img.shields.io/badge/status-learning%20bot-orange.svg>)
![License](<https://img.shields.io/badge/license-open%20source-lightgrey.svg>)

A modular Python chatbot system designed with a clean architecture.
The bot can answer questions, learn from users, and store knowledge persistently.

---

# 📌 Overview

This project is a **self-learning chatbot system** built in Python.

It is designed to demonstrate :

- modular architecture
- separation of concerns
- extensible AI-like behavior
- persistent knowledge storage

---

# ⚙️ Features

- Self-learning system (user teaches the bot)
- Fuzzy matching for question retrieval
- Multi-language support (FR / EN / ES / DE / IT / PT)
- JSON-based persistent memory
- FastAPI REST API
- Console interface mode
- Modular architecture (engine / storage / rules / learning)
- Logging system for debugging
- Unit tests included

---

# Architecture

```
chatbot-ai/
│
├── app.py
├── config.py
├── README.md
├── requirements.txt
│
├── chatbot/
│   ├── engine.py
│   ├── learning.py
│   ├── matching.py
│   ├── language.py
│   ├── knowledge.py
│   ├── rules.py
│   ├── models.py
│   ├── exceptions.py
│   └── utils.py
│
├── interfaces/
│   ├── console.py
│   └── api.py
│
├── storage/
│   ├── base.py
│   ├── json_storage.py
│   └── manager.py
│
├── data/
│   └── knowledge_base.json
│
├── logs/
│   ├── __init__.py     
│   ├── logger.py   
│   └── chat_history.py 
│
├── tests/
│   └── test_engine.py
```

---

# Installation

## 1. Clone repository

```bash
git clone https://github.com/KABUYA-SINA/chatbot-ai.git
cd chatbot-ai
```

## 2. Create virtual environment

```bash
python -m venv venv
```

Activate:

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

# Run the project

## Console mode

```bash
python app.py
```

## API mode

```bash
uvicorn interfaces.api:app --reload
```

Then open:

```
http://127.0.0.1:8000/
```

---

# API Usage

## POST /chat

### Request

```json
{
  "message": "hello"
}
```

### Response

```json
{
  "response": "Hello !"
}
```

---

# How it works

1. User sends a message
2. Language is detected
3. Matching system finds closest question
4. If found → returns answer
5. If not found → learning mode starts
6. User teaches the bot
7. Knowledge is saved in JSON storage

---

# Core Modules

## 🔹 ChatEngine

Orchestrates the full chatbot pipeline.

## 🔹 LearningEngine

Handles new knowledge ingestion safely.

## 🔹 QuestionMatcher

Finds best matching question using similarity scoring.

## 🔹 KnowledgeBase

Central memory system for all stored data.

## 🔹 RuleEngine

Applies post-processing rules to responses.

## 🔹 StorageManager

Abstract layer for data persistence.

---

# Limitations

- No deep learning model (rule-based system)
- Limited NLP understanding
- Simple keyword-based language detection
- Basic similarity matching (SequenceMatcher)

---

# Future Improvements

- Embeddings-based semantic search
- SQLite/PostgreSQL storage backend
- Web chat UI (React /  Vue / Angular)
- Authentication system
- Conversation memory (context awareness)
- Improved NLP pipeline (spaCy / transformers)

---

# Tests

Run tests:

```bash
pytest
```

---

# 👨‍💻 Author

GitHub: [github.com/KABUYA-SINA](https://github.com/KABUYA-SINA)
Project : Educational chatbot system for learning architecture & AI fundamentals

---

# 📜 License

This project is open-source and available for educational use.

---

# Notes

This project is intentionally built without heavy AI frameworks to demonstrate :

- system design
- modular architecture
- extensibility principles
- clean backend engineering
