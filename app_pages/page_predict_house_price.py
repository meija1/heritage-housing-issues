import streamlit as st
import pandas as pd
from src.data_management import load_pkl_file
from src.machine_learning.predictive_analysis_ui import predict_housing_price


def page_predict_house_price():

    version = 'v1'
    clf_pipeline_model = load_pkl_file(
        f'outputs/ml_pipeline/predict_housing_price/{version}/clf_pipeline_model.pkl')

    sale_features = (pd.read_csv(f"outputs/ml_pipeline/predict_housing_price/{version}/X_train.csv")
                    .columns.to_list())

    st.write("### Predict House Price Interface")
    st.info(
        f"* The client is interested in house price predictions on Ames, Iowa \n"
        f"Also the client is interested in seeing correlated variables against the sale price \n"
        f"As well as predicting the house sale price from her four inherited houses")

    st.write("---")