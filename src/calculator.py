from decimal import Decimal, InvalidOperation


def calculate_emi(principal, annual_rate, months):

    try:
        p = Decimal(str(principal))
        annual = Decimal(str(annual_rate))
        n = int(months)

        if p <= 0:
            raise ValueError("Principal must be greater than zero.")

        if annual < 0:
            raise ValueError("Interest rate cannot be negative.")

        if n <= 0:
            raise ValueError("Loan tenure must be greater than zero.")

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

        return {
            "principal": float(p),
            "annual_rate": float(annual),
            "months": n,
            "emi": round(float(emi), 2)
        }

    except (InvalidOperation, ValueError, TypeError):

        raise ValueError(
            "Please provide valid EMI inputs."
        )