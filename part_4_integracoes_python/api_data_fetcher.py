import os
import requests
import pandas as pd
from datetime import datetime

# Constants for Belo Horizonte, Brazil
LAT = -19.9167
LON = -43.9333
API_URL = "https://api.openweathermap.org/data/3.0/onecall"
OUTPUT_CSV = "clima_tempo_data.csv"


def fetch_weather_data(api_key, lat, lon):
    """
    Fetch daily weather forecast data from OpenWeatherMap One Call API.
    Returns the JSON response if successful, else raises an exception.
    """
    params = {
        'lat': lat,
        'lon': lon,
        'exclude': 'current,minutely,hourly,alerts',
        'units': 'metric',
        'appid': api_key
    }
    print("Fetching data from OpenWeatherMap API...")
    try:
        response = requests.get(API_URL, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error: {e} - {response.text}")
        raise
    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")
        raise

def process_weather_data(data):
    """
    Process the API response and extract relevant daily forecast information.
    Returns a pandas DataFrame.
    """
    daily = data.get('daily', [])
    records = []
    from datetime import timezone
    for day in daily:
        date = datetime.fromtimestamp(day['dt'], tz=timezone.utc).strftime('%Y-%m-%d')
        temp_day = day['temp']['day']
        temp_min = day['temp']['min']
        temp_max = day['temp']['max']
        humidity = day['humidity']
        weather_desc = day['weather'][0]['description'] if day.get('weather') else ''
        records.append({
            'date': date,
            'temp.day': temp_day,
            'temp.min': temp_min,
            'temp.max': temp_max,
            'humidity': humidity,
            'weather.description': weather_desc
        })
    return pd.DataFrame(records)

def save_to_csv(df, output_path):
    """Save the DataFrame to a CSV file."""
    try:
        df.to_csv(output_path, index=False)
        print(f"Data saved to {output_path}")
    except Exception as e:
        print(f"Error saving data to CSV: {e}")
        raise

def main():
    print("Starting weather data fetcher for Belo Horizonte, Brazil...")
    # Use the environment variable for the API key
    api_key = os.getenv('OPENWEATHERMAP_API_KEY')
    if not api_key:
        print("Error: OPENWEATHERMAP_API_KEY environment variable not set or missing.")
        print("Please set it and try again.")
        return
    try:
        data = fetch_weather_data(api_key, LAT, LON)
        df = process_weather_data(data)
        output_path = os.path.join(os.path.dirname(__file__), OUTPUT_CSV)
        save_to_csv(df, output_path)
        print(f"Number of records downloaded: {len(df)}")
    except Exception as e:
        print(f"Script failed: {e}")

if __name__ == "__main__":
    main()
