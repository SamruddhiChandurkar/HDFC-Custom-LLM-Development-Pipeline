from src.pdf_rag import PDFPolicyRAG
from src.llm_client import LLMClient


class PDFPolicyAssistant:

    def __init__(self):

        self.rag = PDFPolicyRAG()

        try:

            self.llm = LLMClient()

        except Exception:

            self.llm = None

    def ask(
        self,
        question
    ):

        results = self.rag.search(
            question,
            top_k=5
        )

        if not results:

            return {
                "answer": (
                    "I could not find this information "
                    "in the uploaded policy documents."
                ),
                "sources": [],
                "confidence": "LOW"
            }

        context_parts = []

        for item in results:

            context_parts.append(
                (
                    f"Document: {item['filename']}\n"
                    f"Page: {item['page']}\n"
                    f"Content: {item['text']}"
                )
            )

        context = "\n\n".join(
            context_parts
        )

        if self.llm is None:

            return {
                "answer": results[0]["text"],
                "sources": results,
                "confidence": "MEDIUM"
            }

        system_prompt = """
You are an enterprise banking policy assistant.

Answer ONLY from the supplied policy context.

Rules:

1. Never invent policy.
2. Never assume missing information.
3. If the answer is not present in the uploaded
   documents, clearly say that it was not found.
4. Mention the relevant document and page.
5. Give a concise professional answer.
6. Treat uploaded documents as the current policy
   source for this conversation.
"""

        user_prompt = f"""
POLICY CONTEXT:

{context}

USER QUESTION:

{question}

Provide a grounded answer.

At the end mention the relevant policy document
and page number.
"""

        try:

            answer = self.llm.generate(
                system_prompt,
                user_prompt,
                temperature=0.1
            )

        except Exception:

            answer = results[0]["text"]

        sources = [

            {
                "document":
                    item["filename"],

                "page":
                    item["page"],

                "score":
                    item["score"]
            }

            for item in results
        ]

        return {
            "answer": answer,
            "sources": sources,
            "confidence": "HIGH"
        }