import plotly.express as px
import streamlit as st

from backend import get_data

# UI
st.title("Weather Forecast for the Next Days")

place = st.text_input("Place:")

days = st.slider(label="Forecast Days", min_value=1, max_value=5, help="Select the number of forecasted days")

option = st.selectbox(label="Select data to view", options=("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} days in {place}")

if place:
    try:
        data, date = get_data(place, days, option)

        if option == "Temperature":
            # Create temperature plot
            figure = px.line(x=date, y=data)
            st.plotly_chart(figure)

        if option == "Sky":
            # Create sky image
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png", "Rain": "images/rain.png",
                      "Snow": "images/snow.png"}
            image_paths = [images[condition] for condition in data]
            st.image(image_paths, width=130, caption=date)

    except KeyError:
        st.error("Wrong name of the City")
