import streamlit as st
import plotly.express as px

# UI
st.title("Weather Forecast for the Next Days")

place = st.text_input("Place:")

days = st.slider(label="Forecast Days", min_value=1, max_value=5, help="Select the number of forecasted days")

option = st.selectbox(label="Select data to view", options=("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} days in {place}")

dates = ["2022-25-10", "2022-26-10", "2022-27-10", "2022-27-11", "2022-27-12"]
temperatures = [10, 11, 15, 65, 23]

figure = px.line(x=dates[:days], y=temperatures[:days], labels={"x": "Date", "y": "Temperatures (C)"})
st.plotly_chart(figure)
