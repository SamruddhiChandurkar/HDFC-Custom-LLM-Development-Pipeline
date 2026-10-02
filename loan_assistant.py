from decimal import Decimal, InvalidOperation

from src.rag import answer_question
from src.audit_log import log_event
from src.agent import BankingAgent


class LoanAssistant:

    def __init__(self):

        self.agent = BankingAgent()

    def calculate_emi(
        self,
        principal,
        annual_rate,
        months
    ):

        try:

            p = Decimal(str(principal))
            annual = Decimal(str(annual_rate))
            n = int(months)

            if p <= 0:
                raise ValueError(
                    "Invalid loan inputs"
                )

            if annual < 0:
                raise ValueError(
                    "Invalid loan inputs"
                )

            if n <= 0:
                raise ValueError(
                    "Invalid loan inputs"
                )

            monthly_rate = (
                annual / Decimal("1200")
            )

            if monthly_rate == 0:

                emi = p / n

            else:

                factor = (
                    (1 + monthly_rate)
                    ** n
                )

                emi = (
                    p
                    * monthly_rate
                    * factor
                    / (factor - 1)
                )

            return round(
                float(emi),
                2
            )

        except (
            InvalidOperation,
            ValueError
        ):

            raise ValueError(
                "Please provide valid EMI inputs"
            )

    def ask(self, question):

        return self.agent.ask(
            question
        )