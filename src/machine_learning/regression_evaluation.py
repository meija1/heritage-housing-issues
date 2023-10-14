import streamlit as st
import pandas as pd
import seaborn as sns
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

def regression_performance(X_train, y_train, X_test, y_test, pipeline):
    st.info("Train Set")
    regression_report(X_train, y_train, pipeline)

    st.info("Test Set")
    regression_report(X_test, y_test, pipeline)


def regression_report(X, y, pipeline):

    prediction = pipeline.predict(X)

    st.write('#### Mean Squared Error')
    st.code(mean_squared_error(y, prediction))

    st.write('#### Mean Absolute Error')
    st.code(mean_absolute_error(y, prediction))

    st.write('#### R2 Score')
    st.code(r2_score(y, prediction))
