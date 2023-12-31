import streamlit as st
from app_pages.multipage import MultiPage

from app_pages.page_summary import page_summary
from app_pages.page_hypothesis import page_hypothesis
from app_pages.page_predict_house_price import page_predict_house_price
from app_pages.page_inherited_houses import page_inherited_houses
from app_pages.page_house_price_study import page_house_price_study
from app_pages.page_ml_model import page_ml_model


app = MultiPage(app_name="House Sale Price Predictor")

app.add_page("Project Summary", page_summary)
app.add_page("Project Hypothesis", page_hypothesis)
app.add_page("Predict House Price", page_predict_house_price)
app.add_page("Predict Inherited House Price", page_inherited_houses)
app.add_page("House Price Study", page_house_price_study)
app.add_page("Machine Learning Model", page_ml_model)

app.run()
