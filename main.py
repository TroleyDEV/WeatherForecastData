import streamlit as st
import plotly.express as px
from backend import get_data

# UI
st.title("Weather Forecast for the Next Days")

place = st.text_input("Place:")

days = st.slider(label="Forecast Days", min_value=1, max_value=5, help="Select the number of forecasted days")

option = st.selectbox(label="Select data to view", options=("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} days in {place}")

data, date = get_data(place, days, option)

if option == "Temperature":
    # Create temperature plot
    figure = px.line(x=date, y=data)
    st.plotly_chart(figure)


