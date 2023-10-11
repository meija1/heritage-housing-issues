import streamlit as st
from app_pages.multipage import MultiPage

from app_pages.page_summary import page_summary
from app_pages.page_hypothesis import page_hypothesis


app = MultiPage(app_name="House Sale Price Predictor")

app.add_page("Project Summary", page_summary)
app.add_page("Project Hypothesis", page_hypothesis)

app.run()
