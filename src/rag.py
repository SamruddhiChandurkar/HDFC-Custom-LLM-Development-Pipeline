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
    "explain", "tell", "me", "please"
}


def load_knowledge_base():
    with open(KB_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def tokenize(text):
    words = re.findall(r"[a-zA-Z0-9]+", text.lower())

    return {
        word
        for word in words
        if word not in STOPWORDS
    }


def retrieve_documents(query, top_k=3):
    documents = load_knowledge_base()

    query_words = tokenize(query)

    results = []

    for doc in documents:

        # Only use topic + question for relevance.
        # Do NOT use the answer text for matching.
        searchable_text = (
            doc["topic"] + " " +
            doc["question"]
        )

        doc_words = tokenize(searchable_text)

        matched_words = query_words.intersection(doc_words)

        score = len(matched_words)

        if score > 0:
            results.append({
                "document": doc,
                "score": score,
                "matched_words": matched_words
            })

    results.sort(
        key=lambda item: item["score"],
        reverse=True
    )

    return results[:top_k]


def answer_question(query):
    results = retrieve_documents(query)

    if not results:
        return {
            "answer": (
                "I could not find sufficient information "
                "in the approved demo knowledge base. "
                "Please refer to an authorized representative."
            ),
            "sources": [],
            "confidence": "LOW"
        }

    best = results[0]["document"]

    return {
        "answer": best["answer"],
        "sources": [
            {
                "id": item["document"]["id"],
                "source": item["document"]["source"],
                "topic": item["document"]["topic"]
            }
            for item in results
        ],
        "confidence": "MATCH_FOUND"
    }