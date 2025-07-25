# weather_dashboard/ui_components.py
import streamlit as st
import folium
from streamlit_folium import st_folium
import pandas as pd
import plotly.express as px

def display_weather_metrics(weather_data: dict):
    """
    Displays core weather metrics using Streamlit's st.metric.
    """
    st.success(f"Weather for {weather_data['name']}, {weather_data['sys']['country']}")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Temperature", f"{weather_data['main']['temp']}°C")
        st.metric("Feels Like", f"{weather_data['main']['feels_like']}°C")
    with col2:
        st.metric("Humidity", f"{weather_data['main']['humidity']}%")
        st.metric("Wind Speed", f"{weather_data['wind']['speed']} m/s")
    with col3:
        st.metric("Condition", weather_data['weather'][0]['description'].capitalize())
        st.metric("Pressure", f"{weather_data['main']['pressure']} hPa")

    # Display weather icon
    icon_code = weather_data['weather'][0]['icon']
    icon_url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"
    st.image(icon_url, width=100)

def display_city_map(weather_data: dict):
    """
    Displays an interactive Folium map showing the city location.
    """
    lat = weather_data['coord']['lat']
    lon = weather_data['coord']['lon']
    city_name_full = f"{weather_data['name']}, {weather_data['sys']['country']}"

    st.markdown("---")
    st.subheader("City Location:")

    m = folium.Map(location=[lat, lon], zoom_start=10)
    folium.Marker(
        [lat, lon],
        popup=f"{city_name_full}<br>Temp: {weather_data['main']['temp']}°C",
        tooltip=city_name_full
    ).add_to(m)

    st_folium(m, width=700, height=500)


def display_footer():
    st.markdown("---")
    st.markdown("Developed by Ebube")
    