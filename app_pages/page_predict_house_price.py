import streamlit as st
import pandas as pd
from src.data_management import (
    load_pkl_file, load_house_price_records, load_inherited_house__records)
from src.machine_learning.predictive_analysis_ui import predict_house_price


def page_predict_house_price():

    version = 'v2'
    clf_pipeline_model = load_pkl_file(
        f'outputs/ml_pipeline/predict_housing_price/{version}/clf_pipeline_model.pkl')

    sale_features = (pd.read_csv(f"outputs/ml_pipeline/predict_housing_price/{version}/X_train.csv")
                     .columns.to_list())

    st.write("### Predict House Price Interface")
    st.info(
        f"The client is interested in house price predictions on Ames, Iowa \n\n"
        f"Also the client is interested in seeing correlated variables against the sale price \n\n"
        f"As well as predicting the house sale price from her four inherited houses")

    st.write("---")

    X_live = DrawInputsWidgets()

    if st.button("Run House Price Analysis"):
        house_price_prediction = predict_house_price(
            X_live, sale_features, clf_pipeline_model)

        if house_price_prediction == 1:
            predict_tenure(X_live, sale_features,
                           clf_pipeline_model)


def DrawInputsWidgets():

    df = load_house_price_records()
    percentageMin, percentageMax = 0.4, 2.0

    col1, col2, col3, col4 = st.beta_columns(4)
    col5, col6, col7, col8 = st.beta_columns(4)

    X_live = pd.DataFrame([], index=[0])

    with col1:
        feature = "OverallQual"
        st_widget = st.number_input(
            label=feature,
            min_value=1,
            max_value=10,
            value=int(df[feature].median())
        )
    X_live[feature] = st_widget

    with col2:
        feature = "TotalBsmtSF"
        st_widget = st.number_input(
            label=feature,
            min_value=int(df[feature].min()*percentageMin),
            max_value=int(df[feature].max()*percentageMax),
            value=int(df[feature].median())
        )
    X_live[feature] = st_widget

    with col3:
        feature = "GarageArea"
        st_widget = st.number_input(
            label=feature,
            min_value=int(df[feature].min()*percentageMin),
            max_value=int(df[feature].max()*percentageMax),
            value=int(df[feature].median())
        )
    X_live[feature] = st_widget

    with col4:
        feature = "2ndFlrSF"
        st_widget = st.number_input(
            label=feature,
            min_value=int(df[feature].min()*percentageMin),
            max_value=int(df[feature].max()*percentageMax),
            value=int(df[feature].median())

        )
    X_live[feature] = st_widget

    return X_live
