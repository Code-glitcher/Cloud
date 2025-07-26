# weather_dashboard/app.py
import streamlit as st
from api_client import get_weather
from ui_components import display_weather_metrics, display_city_map, display_footer

# Streamlit App Layout
st.set_page_config(page_title="Interactive Weather Dashboard", layout="centered")

st.title("Interactive Weather Dashboard")

st.markdown(
    """
    Get real-time weather updates for any city around the world!
    """
)

# User input for city
city = st.text_input("Enter city name:", "Enugu") # Default to a common city

# Initialize session state variables if they don't exist
if 'weather_data' not in st.session_state:
    st.session_state.weather_data = None
if 'city_searched' not in st.session_state:
    st.session_state.city_searched = ""

# Logic to fetch weather data based on button click or city change
should_fetch = False
if st.button("Get Weather"):
    should_fetch = True
elif st.session_state.city_searched and st.session_state.city_searched != city:
    # Auto-fetch if city input changes after an initial search
    should_fetch = True
    st.session_state.city_searched = city # Update searched city immediately

if should_fetch:
    if city:
        with st.spinner(f"Fetching weather for {city}..."):
            fetched_weather_data = get_weather(city)
            st.session_state.weather_data = fetched_weather_data
            st.session_state.city_searched = city # Store the city that was searched
    else:
        st.warning("Please enter a city name.")
        st.session_state.weather_data = None # Clear data if city input is empty
        st.session_state.city_searched = ""

# Display results if weather data is available in session state
if st.session_state.weather_data:
    weather_data = st.session_state.weather_data # Get the data from session state
    display_weather_metrics(weather_data)
    display_city_map(weather_data)

else:
    # Display a message if no data is loaded yet
    if not st.session_state.city_searched and not should_fetch:
        st.info("Enter a city and click 'Get Weather' to see current conditions.")

display_footer()