# Imports
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
    "Data Input | F1M Data Hub",
    "Data Input",
    "",
)
st.html(
    f"""
    <hr style='border-width: .5px; border-color: {palette["border-color"]}; margin-bottom: 0em;' />
    """
)

# ----------------------------------------------------------------------------------

# Data form
## Set up column forms
data_col_1, data_col_2 = st.columns([0.6, 0.4], border=True)

# Column 1: Races
with data_col_1:
    st.markdown("### Race schedule")
    selected_year: str = st.selectbox(
        label="Schedule year",
        options=["2024", "2025", "Custom"],
        key="schedule_year",
    )
    schedule: dict = (
        get_schedule(int(selected_year)) if selected_year in ["2024", "2025"] else {}
    )

    with st.expander(f"{selected_year} schedule"):
        schedule_col_1, schedule_col_2 = st.columns([0.8, 0.2], border=False)
        for i in range(1, 25):
            schedule_col_1.selectbox(
                label=f"Race {i}",
                options=(
                    list(schedule.keys())[i - 1]
                    if selected_year in ["2024", "2025"]
                    else list(schedule.keys())
                ),
                disabled=True if selected_year in ["2024", "2025"] else False,
            )
            schedule_col_2.checkbox(
                label="Sprint?",
                value=(
                    list(schedule.values())[i - 1]
                    if selected_year in ["2024", "2025"]
                    else False
                ),
                help=(
                    "Check if this grand prix has a Sprint weekend" if i == 1 else None
                ),
                key=f"sprint_{i}",
                disabled=True if selected_year in ["2024", "2025"] else False,
            )

# Column 2: Team colours
with data_col_2:
    st.markdown("### Team colours")
    selected_team: str = st.selectbox(
        label="Team",
        options=list(get_team_colours("all").keys()) + ["Custom"],
        key="team_colours",
    )
    team_colours: dict = (
        get_team_colours(team=selected_team)
        if selected_team != "Custom"
        else {"primary": "#808080", "secondary": "#ffffff"}
    )

    # Display the team colours to the user
    primary: str = st.color_picker(
        label="Primary colour",
        value=team_colours["primary"],
        disabled=True if selected_team != "Custom" else False,
    )
    st.markdown(f"{selected_team}'s primary colour is **{primary}**")
    secondary: str = st.color_picker(
        label="Secondary colour",
        value=team_colours["secondary"],
        disabled=True if selected_team != "Custom" else False,
    )
    st.markdown(f"{selected_team}'s secondary colour is **{secondary}**")
