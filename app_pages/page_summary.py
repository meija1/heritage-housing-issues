import streamlit as st
import pandas as pd


def page_summary():

    st.write("Project Summary")

    st.info(
        f"The objective of this project is to help the custumoer \n"
        f"to understand and maximize property value as well as \n"
        f"predict the house price in Ames, Iowa by data input and \n"
        f"recieve potential selling price of the inhereted properties. \n\n"
        f"**Project Dataset**\n\n"
        f"The data used for this project is provided by the client \n"
        f"which can be found on \n"
        f"[Kaggle](https://www.kaggle.com/datasets/codeinstitute/housing-prices-data).\n"
        f"The Mchine Learning model has been trained on this data. \n"
        f"The dataset represents a house prices in Ames, Iowa conisting of \n"
        f"nearly 1500 properties and 23 variables decribing the house, \n"
        f"such as GarageArea, KitchenQual, LotArea, OverallQual and more. \n\n"
        f"**Project Terms & Jargon **\n\n"
        f" * A ** customer ** is a person who consumes your service or product.\n"
        f" * A ** house, property ** is referred here as a thing or things belonging to someone.\n"
        f" * A ** sale price ** is price at which the house or property is being sold.\n"
        f" * A ** variable, attribute ** is house distinctive feature or aspect."
    )

    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/meija1/heritage-housing-issues).")

    st.success(
        f"The project has 2 business requirements:\n"
        f"* 1 The client is interested in discovering how the house attributes \n"
        f"correlate with the sale price. Therefore, the client expects data \n"
        f"visualisations of the correlated variables against the sale price to show that.\n"
        f"* 2 The client is interested in predicting the house sale price from her \n"
        f"four inherited houses and any other house in Ames, Iowa."
    )
