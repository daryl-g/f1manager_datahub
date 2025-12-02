# Utility functions

# Imports
import pandas as pd
import streamlit as st
import matplotlib.font_manager as fm  # Import fonts

from PIL import Image


def load_csv(
    file_path: str,
    display: bool = True,
):
    """
    Load a CSV file, return its content as a DataFrame, and display on the app.

    Args:
        file_path (str): Name of the worksheet on the Google Sheet file.
        display (bool, optional): Whether to display the DataFrame in the app. Defaults to True.

    Returns:
        (pd.DataFrame)
            DataFrame containing the CSV file content.
    """

    # Load the CSV file
    with st.spinner("Grabbing data...Remember to hydrate while waiting!"):
        df = pd.read_csv(file_path, delimiter=",", encoding="utf-8")

    # Display the DataFrame in the app
    if display:
        df = st.data_editor(
            df, use_container_width=True, hide_index=True, num_rows="dynamic"
        )

    # Return the DataFrame
    return df


# Team colours and app colour palettes
import streamlit as st


def display_markdown(file_path: str):
    """
    Load and display a markdown file in the app.

    Args:
        file_path (str): Path to the markdown file.
    """

    # Load the markdown file
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
        file.close()  # Gracefully close the markdown file

    # Display the content in the app
    st.markdown(content)


@st.cache_resource
def import_fonts(
    which: str = "roboto",
    weight: str = "regular",
) -> fm.FontProperties | list[fm.FontProperties, fm.FontProperties, fm.FontProperties]:
    """
    This function imports the Roboto Regular and/or Roboto Bold fonts from the same folder as this code.

    Args:
        which (str): Which font to import? Options are "f1" and "roboto". Default is "roboto".
        weight (str): Single font weight ('regular', 'light', 'bold'). Use 'all' to get all fonts.

    Returns:
        Single font properties or tuple containing the fonts.
    """
    # Inputs checking
    if which.lower() not in ["f1", "roboto"]:
        raise ValueError("Unknown font type. Please choose between 'f1' or 'roboto'.")

    # Import the fonts from the same folder as this code
    robotoRegular = fm.FontProperties(fname="src/assets/fonts/Roboto-Regular.ttf")
    robotoLight = fm.FontProperties(fname="src/assets/fonts/Roboto-Light.ttf")
    robotoBold = fm.FontProperties(fname="src/assets/fonts/Roboto-Bold.ttf")

    f1Regular = fm.FontProperties(fname="src/assets/fonts/Formula1-Regular.ttf")
    f1Wide = fm.FontProperties(fname="src/assets/fonts/Formula1-Wide.ttf")
    f1Bold = fm.FontProperties(fname="src/assets/fonts/Formula1-Bold.ttf")

    if which == "roboto":
        if weight == "all":
            return robotoRegular, robotoLight, robotoBold
        elif weight == "regular":
            return robotoRegular
        elif weight == "light":
            return robotoLight
        elif weight == "bold":
            return robotoBold
        else:
            raise ValueError(
                "Unknown font weight. Please choose from 'regular', 'light', 'bold', or 'all' to get all fonts."
            )
    elif which == "f1":
        if weight == "all":
            return f1Regular, f1Wide, f1Bold
        elif weight == "regular":
            return f1Regular
        elif weight == "wide":
            return f1Wide
        elif weight == "bold":
            return f1Bold
        else:
            raise ValueError(
                "Unknown font weight. Please choose from 'regular', 'wide', 'bold', or 'all' to get all fonts."
            )


@st.cache_resource
def plotly_config() -> dict:
    """
    Just a quick function to get the configurations for the Plotly plot.

    Returns:
        dict: Dictionary with Plotly plot configs.
    """
    return {
        "scrollZoom": False,
        "responsiveness": True,
        "doubleClick": "reset+autosize",
        "displayModeBar": False,
    }
