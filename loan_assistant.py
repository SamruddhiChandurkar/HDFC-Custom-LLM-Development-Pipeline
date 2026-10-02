from decimal import Decimal, InvalidOperation

from src.rag import answer_question
from src.audit_log import log_event


class LoanAssistant:

    def calculate_emi(self, principal, annual_rate, months):

        try:
            p = Decimal(str(principal))
            annual = Decimal(str(annual_rate))
            n = int(months)

            if p <= 0 or annual < 0 or n <= 0:
                raise ValueError("Invalid loan inputs")

            monthly_rate = annual / Decimal("1200")

            if monthly_rate == 0:
                emi = p / n
            else:
                factor = (1 + monthly_rate) ** n

                emi = (
                    p
                    * monthly_rate
                    * factor
                    / (factor - 1)
                )

            return round(float(emi), 2)

        except (InvalidOperation, ValueError):

            raise ValueError(
                "Please provide valid EMI inputs"
            )


    def ask(self, question):

        text = question.lower().strip()


        # ==================================================
        # SAFETY / RESTRICTED REQUESTS
        # ==================================================

        restricted_terms = [
            "guarantee approval",
            "approve my loan",
            "guaranteed loan",
            "bypass verification",
            "guarantee my loan",
            "guarantee a loan",
            "bypass loan verification",
            "bypass verification process"
        ]


        if any(
            term in text
            for term in restricted_terms
        ):

            log_event(
                dataset_id="KNOWLEDGE_BASE",
                action="SAFETY_BLOCK",
                details="Restricted loan approval request blocked"
            )

            return {
                "answer": (
                    "I cannot guarantee or bypass loan approval. "
                    "Loan decisions require authorized assessment."
                ),
                "sources": [],
                "route": "SAFETY",
                "confidence": "HIGH"
            }


        # ==================================================
        # RAG / KNOWLEDGE RETRIEVAL
        # ==================================================

        result = answer_question(question)


        # Safely read retrieval information
        sources = result.get("sources", [])


        # ==================================================
        # UNKNOWN / LOW CONFIDENCE QUESTION
        # ==================================================

        if not sources:

            log_event(
                dataset_id="KNOWLEDGE_BASE",
                action="ASSISTANT_UNKNOWN_QUERY",
                details=f"No relevant knowledge found for query: {question}"
            )

            return {
                "answer": (
                    "I could not find relevant information "
                    "for this question in the available banking "
                    "knowledge base."
                ),
                "sources": [],
                "route": "RAG",
                "confidence": "LOW"
            }


        # ==================================================
        # SUCCESSFUL KNOWLEDGE RETRIEVAL
        # ==================================================

        log_event(
            dataset_id="KNOWLEDGE_BASE",
            action="ASSISTANT_QUERY",
            details="Query routed through knowledge retrieval"
        )


        return {
            **result,
            "route": "RAG",
            "confidence": "MATCH_FOUND"
        }