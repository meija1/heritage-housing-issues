from src.machine_learning.regression_evaluation import regression_performance
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.data_management import load_pkl_file


def page_ml_model():

    version = 'v2'

    clf_pipeline_model = load_pkl_file(
        f'outputs/ml_pipeline/predict_housing_price/{version}/clf_pipeline_model.pkl')

    feature_importance = plt.imread(f"outputs/ml_pipeline/predict_housing_price/{version}/features_importance.png")

    X_train = pd.read_csv(f"outputs/ml_pipeline/predict_housing_price/{version}/X_train.csv")

    X_test = pd.read_csv(f"outputs/ml_pipeline/predict_housing_price/{version}/X_test.csv")

    y_train = pd.read_csv(
        f"outputs/ml_pipeline/predict_housing_price/{version}/y_train.csv")

    y_test = pd.read_csv(
        f"outputs/ml_pipeline/predict_housing_price/{version}/y_test.csv")

    st.write("### ML Pipeline: Predict House Price")
    st.info(
        f"* We tried to have a Classifier model to predict house price"
        f", but the **classifier performance did not meet project requirement**: "
        f"it could not compute the numbers properly and calculations were slow. "
        f"The Regressor model was used for predictions of the house prices "
        f"and we found that GradientBoostingRegressor was best performance model. "
        f"The model gaves us a performance R2 score of 0.8 and above. "
        f"")
    st.write("---")

    st.write("* ML pipeline for house price prediction")
    st.write(clf_pipeline_model)
    st.write("---")

    st.write("The four most important features the model was trained on")
    st.write(X_train.columns.to_list())
    st.image(feature_importance)
    st.write("---")

    st.write("### Pipeline Performance")
    regression_performance(X_train, y_train, X_test, y_test, clf_pipeline_model)

