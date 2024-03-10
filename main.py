import streamlit as st

# UI
st.title("Weather Forecast for the Next Days")
place = st.text_input("Place:")
st.slider(label="Forecast Days", min_value=1, max_value=5)
st.selectbox(label="Select data to view", options="")
st.title("Temperature for the next day in location TBD")
