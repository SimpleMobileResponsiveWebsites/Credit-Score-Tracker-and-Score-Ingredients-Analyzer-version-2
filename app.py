import streamlit as st
from components.sidebar import render_sidebar
from components.score_display import display_score
from components.debt_summary import render_debt_summary
from components.score_tracker import render_score_tracker
from components.insights import render_insights
from utils.calculations import calculate_fico_score

def main():
    st.title("Credit Score Tracker and Score Ingredients Analyzer")
    
    # Get credit factors from sidebar
    credit_factors = render_sidebar()
    
    # Calculate and display current score
    current_score = calculate_fico_score(**credit_factors)
    display_score(current_score)
    
    # Render other components
    render_debt_summary()
    render_score_tracker()
    render_insights()

if __name__ == "__main__":
    main()
