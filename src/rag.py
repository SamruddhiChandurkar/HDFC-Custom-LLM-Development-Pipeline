import json
import re
from pathlib import Path


KB_FILE = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "knowledge_base.json"
)


STOPWORDS = {
    "a", "an", "the",
    "is", "are", "am", "was", "were",
    "be", "been", "being",
    "what", "why", "how", "when", "where",
    "which", "who", "whom",
    "can", "could", "would", "should",
    "do", "does", "did",
    "for", "to", "of", "in", "on", "at",
    "by", "with", "from",
    "and", "or", "but",
    "about",
    "explain", "tell", "me", "please",
    "give", "information", "details"
}


# Important banking concepts.
# These help match the user's actual intent
# instead of matching random common words.
CONCEPTS = {
    "loan": {
        "loan",
        "loans",
        "personal",
        "borrowing",
        "borrow",
        "finance",
        "financing"
    },

    "eligibility": {
        "eligibility",
        "eligible",
        "qualify",
        "qualification",
        "criteria"
    },

    "credit": {
        "credit",
        "cibil",
        "score",
        "creditworthiness"
    },

    "interest": {
        "interest",
        "rate",
        "rates",
        "apr"
    },

    "emi": {
        "emi",
        "installment",
        "instalment",
        "monthly",
        "payment"
    },

    "documents": {
        "document",
        "documents",
        "proof",
        "kyc",
        "identity",
        "income"
    },

    "tenure": {
        "tenure",
        "period",
        "duration",
        "months",
        "years"
    }
}


def load_knowledge_base():

    if not KB_FILE.exists():
        return []

    with open(
        KB_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)


def tokenize(text):

    words = re.findall(
        r"[a-zA-Z0-9]+",
        str(text).lower()
    )

    return {
        word
        for word in words
        if word not in STOPWORDS
    }


def detect_concepts(text):

    words = tokenize(text)

    detected = set()

    for concept, keywords in CONCEPTS.items():

        if words.intersection(keywords):

            detected.add(concept)

    return detected


def calculate_score(query, document):

    query_words = tokenize(query)

    question_words = tokenize(
        document.get("question", "")
    )

    topic_words = tokenize(
        document.get("topic", "")
    )

    query_concepts = detect_concepts(query)

    document_concepts = (
        detect_concepts(
            document.get("question", "")
            + " "
            + document.get("topic", "")
        )
    )

    score = 0

    # Exact word matching
    question_matches = (
        query_words.intersection(
            question_words
        )
    )

    topic_matches = (
        query_words.intersection(
            topic_words
        )
    )

    # Question is much more important
    score += len(question_matches) * 5

    # Topic gets lower weight
    score += len(topic_matches) * 3

    # Concept-level matching
    concept_matches = (
        query_concepts.intersection(
            document_concepts
        )
    )

    score += len(concept_matches) * 4

    # Exact phrase bonus
    query_lower = query.lower().strip()
    question_lower = (
        document.get(
            "question",
            ""
        ).lower()
    )

    if query_lower in question_lower:

        score += 10

    return {
        "score": score,
        "matched_words": list(
            question_matches.union(
                topic_matches
            )
        ),
        "matched_concepts": list(
            concept_matches
        )
    }


def retrieve_documents(
    query,
    top_k=3,
    min_score=4
):

    documents = load_knowledge_base()

    results = []

    for document in documents:

        scoring = calculate_score(
            query,
            document
        )

        score = scoring["score"]

        # Do not return weak/irrelevant matches
        if score >= min_score:

            results.append({
                "document": document,
                "score": score,
                "matched_words": scoring[
                    "matched_words"
                ],
                "matched_concepts": scoring[
                    "matched_concepts"
                ]
            })

    results.sort(
        key=lambda item: item["score"],
        reverse=True
    )

    return results[:top_k]


def answer_question(query):

    if not query or not query.strip():

        return {
            "answer": (
                "Please enter a banking question."
            ),
            "sources": [],
            "route": "RAG",
            "confidence": "LOW"
        }

    results = retrieve_documents(
        query=query,
        top_k=3,
        min_score=4
    )

    if not results:

        return {
            "answer": (
                "I could not find sufficient "
                "information in the approved "
                "banking knowledge base for "
                "this question."
            ),
            "sources": [],
            "route": "RAG",
            "confidence": "LOW"
        }

    best = results[0]

    # Confidence based on retrieval quality
    if best["score"] >= 12:
        confidence = "HIGH"

    elif best["score"] >= 7:
        confidence = "MEDIUM"

    else:
        confidence = "LOW"

    return {
        "answer": best["document"].get(
            "answer",
            "No answer available."
        ),

        "sources": [
            {
                "id": item["document"].get(
                    "id"
                ),
                "source": item["document"].get(
                    "source"
                ),
                "topic": item["document"].get(
                    "topic"
                )
            }
            for item in results
        ],

        "route": "RAG",

        "confidence": confidence,

        "retrieval": {
            "best_score": best["score"],
            "matched_words": best[
                "matched_words"
            ],
            "matched_concepts": best[
                "matched_concepts"
            ]
        }
    }