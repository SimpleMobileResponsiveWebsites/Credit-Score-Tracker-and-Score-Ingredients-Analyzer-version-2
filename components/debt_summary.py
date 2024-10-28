import streamlit as st
import pandas as pd

def render_debt_summary():
    """Render the debt summary section."""
    st.header("Debt Summary")
    st.write("Enter current balances for the following debt categories:")
    
    debts = {
        "Credit Cards": st.number_input("Credit Card Debt", min_value=0, value=5000, step=100),
        "Real Estate": st.number_input("Real Estate Loans", min_value=0, value=150000, step=1000),
        "Student Loans": st.number_input("Student Loans", min_value=0, value=20000, step=500),
        "Personal Loans": st.number_input("Personal Loans", min_value=0, value=3000, step=100),
        "Collections": st.number_input("Collections", min_value=0, value=500, step=50)
    }
    
    debt_df = pd.DataFrame({
        "Type": list(debts.keys()),
        "Amount": list(debts.values())
    })
    
    st.table(debt_df)
