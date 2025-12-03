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
    <hr style='border-width: .10px; border-color: {palette["border-color"]}; margin-bottom: 0em;' />
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
    schedule: dict | list = (
        get_schedule(int(selected_year))
        if selected_year in ["2024", "2025"]
        else get_schedule(year=0)
    )

    with st.expander(f"{selected_year} schedule"):
        # Layout
        rows = [st.columns([0.7, 0.3], border=True, gap="small") for _ in range(25)]

        # Prefilled schedule
        if selected_year in ["2024", "2025"]:
            for i, (gp, is_sprint) in enumerate(schedule.items()):
                with rows[i][0]:
                    st.text_input(
                        label=f"Race {i+1}",
                        value=gp,
                        key=f"race_{i}",
                        disabled=True,
                    )
                with rows[i][1]:
                    st.checkbox(
                        label="Sprint",
                        value=is_sprint,
                        key=f"sprint_{i}",
                        disabled=True,
                    )

        # Custom schedule

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

    # Layout
    teamcolours_row_1 = st.columns([0.1, 0.9], border=False, gap="small")
    teamcolours_row_2 = st.columns([0.1, 0.9], border=False, gap="small")

    # Display the team colours to the user
    primary: str = teamcolours_row_1[0].color_picker(
        label="Primary colour",
        value=team_colours["primary"],
        disabled=True if selected_team != "Custom" else False,
        label_visibility="collapsed",
    )
    teamcolours_row_1[1].markdown(
        f"""{selected_team}'s primary colour: <span style="color: {primary}; font-weight: bold">{primary}</span>""",
        unsafe_allow_html=True,
    )
    secondary: str = teamcolours_row_2[0].color_picker(
        label="Secondary colour",
        value=team_colours["secondary"],
        disabled=True if selected_team != "Custom" else False,
        label_visibility="collapsed",
    )
    teamcolours_row_2[1].markdown(
        f"""{selected_team}'s secondary colour: <span style="color: {secondary if secondary != "#1a1a1a" else "#ffffff"}; font-weight: bold">{secondary}</span>""",
        unsafe_allow_html=True,
    )
