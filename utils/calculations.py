def calculate_fico_score(payment_history, amount_of_debt, credit_history_length, new_credit_amount, credit_mix):
    """Calculate FICO score based on components."""
    score = (
        payment_history * 0.35 +
        amount_of_debt * 0.30 +
        credit_history_length * 0.15 +
        new_credit_amount * 0.10 +
        credit_mix * 0.10
    )
    return min(850, int(score * 8.5))  # Scale score to 850 max
