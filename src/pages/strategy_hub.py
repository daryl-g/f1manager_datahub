# Pit stop timing + strategy hub

# Imports
import pandas as pd
import streamlit as st

# Custom modules
from styles import Styles
from components import title_header
from utils import get_team_colours, get_schedule

# Get colour palette
styles: Styles = Styles()
styles.set_style()
palette: dict = styles.get_style()

# Set up page
title_header(
    "Strategy Hub | F1M Data Hub",
    "Strategy Hub",
    "",
)
st.html(
    f"""
    <hr style='border-width: .10px; border-color: {palette["border-color"]}; margin-bottom: 0em;' />
    """
)

# ----------------------------------------------------------------------------------
