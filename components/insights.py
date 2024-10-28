import streamlit as st

def render_insights():
    """Render credit score insights and recommendations."""
    st.header("Insights")
    
    insights = {
        "Payment History (35%)": "The most significant factor. Ensure all payments are on time.",
        "Amount of Debt (30%)": "Keep debt levels low relative to your credit limits.",
        "Credit History Length (15%)": "Older accounts contribute positively.",
        "Amount of New Credit (10%)": "Avoid opening multiple new accounts in a short time.",
        "Credit Mix (10%)": "A variety of credit types (e.g., cards, loans) can improve scores."
    }
    
    for factor, description in insights.items():
        st.markdown(f"- **{factor}**: {description}")
