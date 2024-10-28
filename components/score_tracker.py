import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

def render_score_tracker():
    """Render the score tracker visualization."""
    st.header("Credit Score Tracker")
    st.write("Track changes in your score over time across different categories.")
    
    # Generate sample data
    dates = pd.date_range(datetime(2022, 1, 1), periods=12, freq='M')
    sample_data = {
        "Credit Cards": np.random.randint(600, 850, len(dates)),
        "Auto Loans": np.random.randint(600, 850, len(dates)),
        "Mortgages": np.random.randint(600, 850, len(dates))
    }
    score_tracker_df = pd.DataFrame(sample_data, index=dates)
    
    # Create plot
    fig, ax = plt.subplots(figsize=(10, 6))
    for column in score_tracker_df.columns:
        ax.plot(score_tracker_df.index, score_tracker_df[column], label=column)
    
    ax.set_title("Credit Score Tracker")
    ax.set_ylabel("FICO Score")
    ax.set_xlabel("Time")
    ax.set_ylim(550, 850)
    ax.legend()
    
    st.pyplot(fig)
