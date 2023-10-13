import plotly.express as px
import numpy as np
import streamlit as st
from src.data_management import load_house_price_records

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("darkgrid")

def page_house_price_study():
    
    df = load_house_price_records()

    vars_to_study = ['1stFlrSF', 'GarageArea',
                     'GarageYrBlt', 'GrLivArea', 'OverallQual',
                     'TotalBsmtSF', 'YearBuilt']


    st.write("### House Price Study")
    st.info(
        f"* The client is interested in understanding the correlation between \n"
        f"sale price and houses attributes and which attributes affect sale price. \n"
        f"We will show data visualisations of the correlated variables against \n"
        f"the sale price to show that.")

    if st.checkbox("Inspect House Price Dataset"):
        st.write(
            f"* The dataset has {df.shape[0]} rows and {df.shape[1]} columns, "
            f"find below the first 10 rows.")

        st.write(df.head(10))

    st.write("---")

    st.write(
        f"* A correlation study was conducted in the notebook to better understand how "
        f"the variables are correlated to Sale Price. \n"
        f"The model gave us the most correlated variables, which are:")
    st.subheader(vars_to_study)

def spearman_analysis(df):
    corr_spearman = df.corr(method='spearman')['SalePrice'].sort_values(
        key=abs, ascending=False)[1:].head(10)


def pearson_analysis(df):
    corr_pearson = df.corr(method='pearson')['SalePrice'].sort_values(
        key=abs, ascending=False)[1:].head(10)

