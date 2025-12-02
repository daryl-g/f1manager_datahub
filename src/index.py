## Main entry point of the dashboard

# Imports
import streamlit as st

# Set default theme
if "theme" not in st.session_state:
    st.session_state.theme = "dark"

# Custom modules
from components import navigation

# Setup navigation
navigation()

st.set_page_config(
    page_icon=":sports_motorsports:",
    layout="wide",
)
