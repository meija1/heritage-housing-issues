import streamlit as st
import pandas as pd
from src.data_management import (
    load_pkl_file, load_house_price_records, load_inherited_house_records)
from src.machine_learning.predictive_analysis_ui import predict_house_price


def page_inherited_houses():

    version = 'v2'
    clf_pipeline_model = load_pkl_file(
        f'outputs/ml_pipeline/predict_housing_price/{version}/clf_pipeline_model.pkl')

    sale_features = (pd.read_csv(f"outputs/ml_pipeline/predict_housing_price/{version}/X_train.csv")
                     .columns.to_list())

    st.write("### Predict Inherited House Price")
    st.info(f"Client is interested in predicting the house sale price from her four inherited houses")

    st.write("This is the data for the 4 inherited houses provided by the customer")

    house_data = load_inherited_house_records()
    house_data = house_data.filter(sale_features)
    inherited_price_prediction = clf_pipeline_model.predict(house_data)
    st.write(house_data)

    if st.button("Run Inherited House Price Analysis"):
        
        st.write("The sale price for inherited houses is: \n")
        st.write(inherited_price_prediction, "These houses go in order respectively")

