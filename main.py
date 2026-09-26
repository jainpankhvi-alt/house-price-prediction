import streamlit as st
import joblib

model = joblib.load("housemodel.pkl")

sqft = st.number_input("Sqft Area", min_value=0)
room = st.number_input("No of Rooms", min_value=1)
floor = st.number_input("Floors", min_value=1)
km = st.number_input("Distance from Railway Station (km)", min_value=0.0)

if st.button("Predict Price"):
    price = model.predict([[sqft, room, floor, km]])
    st.write(f"Predicted House Price: ₹{price[0]:,.0f}")