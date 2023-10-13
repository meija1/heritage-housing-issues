import streamlit as st
from app_pages.multipage import MultiPage

from app_pages.page_summary import page_summary
from app_pages.page_hypothesis import page_hypothesis
from app_pages.page_predict_house_price import page_predict_house_price
from app_pages.page_inherited_houses import page_inherited_houses


app = MultiPage(app_name="House Sale Price Predictor")

app.add_page("Project Summary", page_summary)
app.add_page("Project Hypothesis", page_hypothesis)
app.add_page("Predict House Price", page_predict_house_price)
app.add_page("Predict Inherited House Price", page_inherited_houses)

app.run()
