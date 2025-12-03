# Utility functions related to F1

# Imports
import pandas as pd
import streamlit as st


@st.cache_resource
def get_team_colours(
    team: str,
) -> dict[str, dict[str, str]] | dict[str, str]:
    """
    Get the primary and secondary colours for a given F1 team.

    Args:
        team (str): The three-letter name of the F1 team, or 'all' for all teams.

    Returns:
        (dict[str, str]): A dictionary containing the primary and secondary colours.
    """
    team_colours = {
        "Alpine": {"primary": "#0078c9", "secondary": "#ff87bc"},
        "Aston Martin": {"primary": "#00665e", "secondary": "#cedc00"},
        "Ferrari": {"primary": "#ed1c24", "secondary": "#1a1a1a"},
        "Haas": {"primary": "#ffffff", "secondary": "#d6001c"},
        "McLaren": {"primary": "#ff8000", "secondary": "#1a1a1a"},
        "Mercedes": {"primary": "#00f5d2", "secondary": "#1a1a1a"},
        "Racing Bulls": {"primary": "#1434cb", "secondary": "#ffffff"},
        "Red Bull": {"primary": "#1e4a98", "secondary": "#3566cc"},
        "Sauber": {"primary": "#52e252", "secondary": "#1a1a1a"},
        "Williams": {"primary": "#0000ff", "secondary": "#ffffff"},
    }

    # Check if team is valid
    if team not in team_colours.keys() and team != "all":
        raise ValueError(f"Invalid team name: {team}")

    if team == "all":
        return team_colours
    else:
        return team_colours.get(team, {"primary": "#808080", "secondary": "#ffffff"})


@st.cache_resource
def get_schedule(year: int) -> dict | list:
    """
    Get previous F1 race schedules.

    Args:
        year (int): Specific F1 season. Currently only supports 2024 and 2025.

    Returns:
        (dict): Information about previous F1 season's race schedule.
    """
    # Input checking
    if year not in [0, 2024, 2025]:
        raise ValueError(
            "The app only currently supports schedule for 2024 and 2025 or 0 for custom cause I'm too lazy."
        )

    grand_prixes: list[str] = [
        "Australia",
        "China",
        "Japan",
        "Bahrain",
        "Saudi Arabia",
        "Miami",
        "Imola/Emilia-Romagna",
        "Monaco",
        "Spain",
        "Canada",
        "Austria",
        "Great Britain",
        "Belgium",
        "Hungary",
        "Netherlands",
        "Italy",
        "Azerbaijan",
        "Singapore",
        "United States",
        "Mexico",
        "Brazil",
        "Las Vegas",
        "Qatar",
        "Abu Dhabi",
    ]

    # Boolean value represents Sprint weekend
    if year == 2024:
        return {
            # Bahrain GP
            grand_prixes[3]: False,
            # Saudi Arabia GP
            grand_prixes[4]: False,
            # Australian GP
            grand_prixes[0]: False,
            # Japanese GP
            grand_prixes[2]: False,
            # Chinese GP
            grand_prixes[1]: True,
            # Miami GP
            grand_prixes[5]: True,
            # Imola GP
            grand_prixes[6]: False,
            # Monaco GP
            grand_prixes[7]: False,
            # Canadian GP
            grand_prixes[9]: False,
            # Spanish GP
            grand_prixes[8]: False,
            # Austrian GP
            grand_prixes[10]: False,
            # British GP
            grand_prixes[11]: False,
            # Hungarian GP
            grand_prixes[13]: False,
            # Belgian GP
            grand_prixes[12]: True,
            # Dutch GP
            grand_prixes[14]: False,
            # Italian GP
            grand_prixes[15]: False,
            # Azerbaijan GP
            grand_prixes[16]: False,
            # Singapore GP
            grand_prixes[17]: False,
            # United States GP
            grand_prixes[18]: True,
            # Mexico GP
            grand_prixes[19]: False,
            # Brazilian GP
            grand_prixes[20]: True,
            # Las Vegas GP
            grand_prixes[21]: False,
            # Qatar GP
            grand_prixes[22]: True,
            # Abu Dhabi GP
            grand_prixes[23]: False,
        }
    elif year == 2025:
        schedule_2025: dict = {}

        for race in grand_prixes:
            if race in [
                "China",
                "Miami",
                "Belgium",
                "United States",
                "Brazil",
                "Qatar",
            ]:
                schedule_2025[race] = True
            else:
                schedule_2025[race] = False

        return schedule_2025
    elif year == 0:
        return grand_prixes
