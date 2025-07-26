# weather_dashboard/utils.py

def format_temperature(temp_celsius: float, unit: str = "C") -> str:
    """
    Formats temperature to a string with the specified unit.
    Args:
        temp_celsius (float): Temperature in Celsius.
        unit (str): 'C' for Celsius, 'F' for Fahrenheit.
    Returns:
        str: Formatted temperature string.
    """
    if unit.upper() == "F":
        temp_fahrenheit = (temp_celsius * 9/5) + 32
        return f"{temp_fahrenheit:.1f}°F"
    else:
        return f"{temp_celsius:.1f}°C"