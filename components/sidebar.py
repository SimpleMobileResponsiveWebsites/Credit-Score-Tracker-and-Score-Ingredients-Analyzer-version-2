import streamlit as st

def render_sidebar():
    """Render sidebar with credit factor inputs."""
    st.sidebar.header("Credit Score Components")
    
    factors = {
        "payment_history": st.sidebar.slider("Payment History (35%)", 0, 100, 90),
        "amount_of_debt": st.sidebar.slider("Amount of Debt (30%)", 0, 100, 50),
        "credit_history_length": st.sidebar.slider("Length of Credit History (15%)", 0, 100, 40),
        "new_credit_amount": st.sidebar.slider("Amount of New Credit (10%)", 0, 100, 20),
        "credit_mix": st.sidebar.slider("Credit Mix (10%)", 0, 100, 30)
    }
    
    return factors
