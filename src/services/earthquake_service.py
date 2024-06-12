import requests
from datetime import datetime


class EarthquakeService:
    @staticmethod
    def get_earthquakes_to_today(start_time, min_magnitude):
        today = datetime.now().strftime("%Y-%m-%d")
        url = f"https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime={start_time}&endtime={today}&minmagnitude={min_magnitude}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            earthquakes = data["features"]
            return earthquakes
        else:
            print(f"Error: {response.status_code}")
            return None
