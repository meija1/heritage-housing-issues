import streamlit as st


def predict_house_price(X_live, house_features, house_price_pipeline):

    X_live_house_price = X_live.filter(house_features)

    house_price_prediction = house_price_pipeline.predict(X_live_house_price)

    st.write(
        f"The predicted house price is: ")
    st.header(
        f"**{float(house_price_prediction.round(1))}** $"
    )
