import streamlit as st

def display_score(score):
    """Display the calculated FICO score."""
    st.header("Calculated FICO Score")
    st.metric("Your FICO Score:", score)
    
    # Add score range indicator
    if score >= 800:
        st.success("Exceptional Credit Score")
    elif score >= 740:
        st.success("Very Good Credit Score")
    elif score >= 670:
        st.info("Good Credit Score")
    elif score >= 580:
        st.warning("Fair Credit Score")
    else:
        st.error("Poor Credit Score")
