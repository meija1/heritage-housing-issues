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

    df_eda = df.filter(vars_to_study + ['SalePrice'])

    if st.checkbox("Spearman Analysis"):
        spearman_analysis(df_eda)

    if st.checkbox("Pearson Analysis"):
        pearson_analysis(df_eda)

    st.write(
        f"* OverallQual has the strongest correlation\n"
        f"* GrLivArea comes second in both analysis\n"
        f"* YearBuilt is higher in spearman than in pearson\n"
        f"* GarageArea is higher in pearson than in spearman\n"
        f"* TotalBsmtSF is slightly lower in spearman than in pearson\n"
        f"* GarageYrBlt is the lowest in pearson\n"
        f"* 1stFlrSF is the lowest in spearman"
    )

    st.write("---")

    st.write("Sale Price comparison on most correlated variables")

    if st.checkbox("Sale Price Analysis"):
        sale_level_per_variable(df_eda)

    
def sale_level_per_variable(df_eda):
    target_var = 'SalePrice'

    for col in df_eda.drop([target_var], axis=1).columns.to_list():
        if df_eda[col].dtype == 'object':
            plot_categorical(df_eda, col, target_var)
        else:
            plot_numerical(df_eda, col, target_var)


def plot_categorical(df, col, target_var):
    fig, axes = plt.subplots(figsize=(12, 5))
    sns.countplot(data=df, x=col, hue=target_var,
                  order=df[col].value_counts().index)
    plt.xticks(rotation=90)
    plt.title(f"{col}", fontsize=20, y=1.05)
    st.pyplot(fig)


def plot_numerical(df, col, target_var):
    fig, axes = plt.subplots(figsize=(8, 5))
    plt.scatter(data=df, x=col, y='SalePrice', alpha=0.5)
    plt.title(f"{col}", fontsize=20, y=1.05)
    st.pyplot(fig)


def spearman_analysis(df):
    corr_spearman = df.corr(method='spearman')['SalePrice'].sort_values(
        key=abs, ascending=False)[1:].head(10)
    fig, axes = plt.subplots(figsize=(8, 4))
    axes = plt.bar(x=corr_spearman[:7].index, height=corr_spearman, width=0.5)
    plt.title("Spearman Analysis", fontsize=10, y=1.05)
    st.pyplot(fig)


def pearson_analysis(df):
    corr_pearson = df.corr(method='pearson')['SalePrice'].sort_values(
        key=abs, ascending=False)[1:].head(10)
    fig, axes = plt.subplots(figsize=(8, 4))
    axes = plt.bar(x=corr_pearson[:7].index, height=corr_pearson, width=0.5)
    plt.title("Pearson Analysis", fontsize=10, y=1.05)
    st.pyplot(fig)

