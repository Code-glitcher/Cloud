# weather_dashboard/api_client.py
import requests
import os
from dotenv import load_dotenv
import streamlit as st

# Load environment variables when this module is imported
load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL_WEATHER = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city: str) -> dict | None:
    """
    Fetches current weather data for a given city from OpenWeatherMap API.

    Args:
        city (str): The name of the city.

    Returns:
        dict | None: A dictionary containing weather data if successful, None otherwise.
    """
    if not API_KEY:
        st.error("API key not found. Please set OPENWEATHER_API_KEY in your .env file.")
        return None

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    try:
        response = requests.get(BASE_URL_WEATHER, params=params)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)
        weather_data = response.json()
        return weather_data
    except requests.exceptions.HTTPError as e:
        if response.status_code == 404:
            st.error(f"City '{city}' not found. Please check the spelling.")
        else:
            st.error(f"HTTP error occurred: {e}")
        return None
    except requests.exceptions.ConnectionError:
        st.error("Network error. Please check your internet connection.")
        return None
    except requests.exceptions.Timeout:
        st.error("The request timed out. Please try again.")
        return None
    except requests.exceptions.RequestException as e:
        st.error(f"An error occurred: {e}")
        return None

        