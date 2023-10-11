import streamlit as st


def page_hypothesis():

    st.write("### Project Hypothesis and Validation")

    st.success(
        f"Overall Quality of the house is the strongest correlation to the Sale Price.\n"
        f"There is a steady, slow increase of Sale Price as the years increase.\n"
        f"Also usually a larger square feet and area means the value goes up\n\n"
        f"**Correlation Study**\n\n"
        f"The study showed that the most strongest correlation to the house price was \n"
        f"Overall Quality (OverallQual) 1st Floor squarefootage (1stFlrSF) \n"
        f"Garage Area(GarageArea) Groundlevel Living area(GrLivArea) \n"
        f"Garage Area (GarageArea) Total Basement Area(TotalBsmtSF) \n"
        f"Year Built(YearBuilt). The correlation study and house price study \n"
        f"supports that."
    )
