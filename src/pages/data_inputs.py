# Inputting relevant F1 data

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

    # Allow the user to choose the schedule and retain it in the session storage
    if "selected_year" not in st.session_state:
        st.session_state.selected_year = "2024"
    selected_year: str = st.selectbox(
        label="Schedule year",
        options=["2024", "2025"],  # , "Custom"],
        index=["2024", "2025"].index(st.session_state.selected_year),
        key="schedule_year",
    )
    st.session_state.selected_year = selected_year

    with st.expander(
        f"{selected_year} schedule", expanded=True, icon=":material/event:"
    ):
        # Layout
        rows: list = [
            st.columns([0.7, 0.3], border=True, gap="small") for _ in range(25)
        ]
        # Prefilled schedule (assuming that `schedule` is a prefilled dict)
        if selected_year in ["2024", "2025"]:
            # Get the schedule
            schedule: dict = get_schedule(int(selected_year))
            # Fill in the schedule
            for i, (gp, is_sprint) in enumerate(schedule.items()):
                with rows[i][0]:
                    st.text_input(
                        label=f"Race {i+1}",
                        value=gp,
                        disabled=True,
                    )
                with rows[i][1]:
                    if is_sprint:
                        st.html("<br />")
                        st.markdown("- [x] Sprint")

        # Custom schedule (assuming that `schedule` is just a list of grand prixes)
        # else:
        #     selected_races: dict = {}  # Structure: grand_prix (str) - is_sprint (bool)

        #     # Initialise it in the app's session storage if it doesn't exist
        #     if "selected_races" not in st.session_state:
        #         st.session_state.selected_races = selected_races
        #     else:
        #         selected_races = st.session_state.selected_races

        #     # Button to clear custom schedule
        #     clear_schedule: bool = st.button(
        #         label="Clear",
        #         on_click=(lambda: st.session_state.update({"selected_races": {}})),
        #     )
        #     if clear_schedule:
        #         selected_races = {}

        #     # Check if the user has already prefilled a dict of races or not
        #     if (len(selected_races) == 24) and ("" not in selected_races.keys()):
        #         for i, (gp, is_sprint) in enumerate(selected_races.items()):
        #             with rows[i][0]:
        #                 st.text_input(
        #                     label=f"Race {i+1}",
        #                     value=gp,
        #                 )
        #             with rows[i][1]:
        #                 st.checkbox(
        #                     label="Sprint",
        #                     value=is_sprint,
        #                     key=f"custom_sprint_{i}",
        #                 )
        #     # If there is no prefilled custom schedule
        #     else:
        #         # Get all grand prix locations
        #         grand_prixes: list[str] = get_schedule(0)
        #         # Loop through the options
        #         for i in range(24):
        #             # Declare empty variables
        #             single_race: str = ""
        #             single_sprint: bool = False

        #             # Create empty widgets
        #             with rows[i][0]:
        #                 single_race = st.selectbox(
        #                     label=f"Race {i + 1}",
        #                     options=[""] + grand_prixes,
        #                     index=0,
        #                     placeholder="Select a GP...",
        #                 )
        #                 # If there is no race selected
        #                 if single_race == "":
        #                     # Display a warning
        #                     st.warning(
        #                         f"No race is selected for race {i + 1}! Please choose a race from the dropdown."
        #                     )
        #                 # Check if the race is already in the list
        #                 elif single_race in selected_races.keys():
        #                     # Check if the race is in the same or different position
        #                     race_position: int = 0
        #                     try:
        #                         race_position = list(selected_races.keys()).index(
        #                             single_race
        #                         )
        #                     except ValueError:
        #                         race_position = 0

        #                     if i == race_position + 1:
        #                         # Display a warning
        #                         st.warning(
        #                             f"{single_race} GP is already selected for race {race_position + 1}. Please select another race for race {i + 1}!"
        #                         )
        #                         # Reset the selectbox
        #                         single_race = ""
        #             with rows[i][1]:
        #                 single_sprint = st.checkbox(
        #                     label="Sprint",
        #                     value=single_sprint,
        #                     key=f"custom_sprint_{i}",
        #                 )

        #             # Add it to the prefilled list
        #             if single_race != "":
        #                 selected_races[single_race] = single_sprint

        #         # Write the custom schedule into the session storage
        #         st.session_state.selected_races = selected_races


# Column 2: Team colours
with data_col_2:
    st.markdown("### Team colours")
    team_selections: list = list(get_team_colours("all").keys()) + ["Custom"]

    if "selected_team" not in st.session_state:
        st.session_state.selected_team = team_selections[0]
    selected_team: str = st.selectbox(
        label="Team",
        options=team_selections,
        index=team_selections.index(st.session_state.selected_team),
        key="team_selected",
    )
    st.session_state.selected_team = selected_team

    if "team_colours" not in st.session_state:
        st.session_state.team_colours = {}
    team_colours: dict = (
        get_team_colours(team=selected_team)
        if selected_team != "Custom"
        else (
            st.session_state.team_colours
            if "team_colours" in st.session_state
            else {"primary": "#808080", "secondary": "#ffffff"}
        )
    )
    st.session_state.team_colours = team_colours

    # Layout
    teamcolours_row_1 = st.columns([0.09, 0.91], border=False, gap="small")
    teamcolours_row_2 = st.columns([0.09, 0.91], border=False, gap="small")

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

    # Check to see if it is necessary to save the new team colours
    temp_colours: dict = {"primary": primary, "secondary": secondary}
    if temp_colours != team_colours:
        st.session_state.team_colours = temp_colours
