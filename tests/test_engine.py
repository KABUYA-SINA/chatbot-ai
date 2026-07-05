"""
Unit tests for ChatEngine.

Goals:
- ensure stability
- ensure deterministic behavior in test mode
- avoid interactive learning blocking tests
- validate matching + response structure
"""

from chatbot.engine import ChatEngine


# ------------------------------------------------------------
# 1. ENGINE STABILITY
# ------------------------------------------------------------

def test_engine_stability():
    """
    Engine must never crash regardless of input.
    """

    engine = ChatEngine(test_mode=True)

    inputs = [
        "hello",
        "salut",
        "????",
        "",
        "random text 123",
        "👋👋👋"
    ]

    for msg in inputs:
        response = engine.process(msg)

        assert isinstance(response, str)
        assert response is not None


# ------------------------------------------------------------
# 2. UNKNOWN INPUT SAFE MODE
# ------------------------------------------------------------

def test_unknown_input_safe_mode():
    """
    Unknown input must NOT trigger interactive learning.
    """

    engine = ChatEngine(test_mode=True)

    response = engine.process("this_is_totally_unknown_999999")

    assert response == "TEST_MODE_NO_LEARNING"


# ------------------------------------------------------------
# 3. MATCHING BEHAVIOR
# ------------------------------------------------------------

def test_matching_behavior():
    """
    If knowledge exists, engine should return a valid answer.
    """

    engine = ChatEngine(test_mode=True)

    # Inject controlled knowledge
    engine.knowledge.add_question("en", "hello", "Hi there!")

    response = engine.process("hello")

    assert isinstance(response, str)
    assert len(response) > 0

    normalized = response.lower()

    # flexible validation - format output
    assert (
        "hi" in normalized
        or "hello" in normalized
        or "there" in normalized
    )


# ------------------------------------------------------------
# 4. RESPONSE CONSISTENCY
# ------------------------------------------------------------

def test_response_consistency():
    """
    Same input should always return consistent output type.
    """

    engine = ChatEngine(test_mode=True)

    r1 = engine.process("hello")
    r2 = engine.process("hello")

    assert isinstance(r1, str)
    assert isinstance(r2, str)


# ------------------------------------------------------------
# 5. EMPTY INPUT HANDLING
# ------------------------------------------------------------

def test_empty_input():
    """
    Empty input must be safely handled.
    """

    engine = ChatEngine(test_mode=True)

    response = engine.process("")

    assert isinstance(response, str)
    assert response != None