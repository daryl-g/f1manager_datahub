# Imports
import streamlit as st


# Custom navigation component
def navigation() -> None:
    """
    Custom wrapper for Streamlit's navigation element.

    Returns:
        (None): Renders the page with the navigation component.
    """
    pages: list = [
        st.Page(
            page="pages/home.py",
            title="Home",
            icon=":material/sports_motorsports:",
            default=True,
        ),
        st.Page(
            page="pages/data_inputs.py",
            title="Data Input",
            icon=":material/edit:",
        ),
        st.Page(
            page="pages/race_data.py",
            title="Race Data",
            icon=":material/bar_chart:",
        ),
        st.Page(
            page="pages/strategy_hub.py",
            title="Strategy Hub",
            icon=":material/sports_score:",
        ),
    ]

    pg = st.navigation(pages, position="top")
    pg.run()
