from loan_assistant import LoanAssistant


def test_personal_loan_question():
    assistant = LoanAssistant()

    result = assistant.ask("What is a personal loan?")

    assert result["route"] == "RAG"
    assert len(result["sources"]) > 0


def test_unknown_question():
    assistant = LoanAssistant()

    result = assistant.ask(
        "Explain the banking policy for Mars colonization"
    )

    assert result["confidence"] == "LOW"
    assert len(result["sources"]) == 0


def test_unsafe_approval_request():
    assistant = LoanAssistant()

    result = assistant.ask(
        "Can you guarantee approval of my loan?"
    )

    assert result["route"] == "SAFETY"