from datetime import datetime
from src.models.earthquake import Earthquake


class EarthquakeFactory:
    @staticmethod
    def create_earthquake(data):
        properties = data["properties"]
        geometry = data["geometry"]
        coordinates = geometry["coordinates"]
        longitude = float(coordinates[0])
        latitude = float(coordinates[1])
        timestamp_ms = properties["time"]
        timestamp = timestamp_ms / 1000

        date_str = EarthquakeFactory.format_timestamp(timestamp)

        return Earthquake(
            event_id=data.get('id', 'N/A'),
            magnitude=properties.get('mag', 'N/A'),
            location=properties.get('place', 'N/A'),
            date=date_str,
            tsunami_warning=properties.get('tsunami', 'N/A'),
            longitude=longitude,
            latitude=latitude
        )

    @staticmethod
    def format_timestamp(timestamp):
        if EarthquakeFactory.is_valid_timestamp(timestamp):
            timestamp_str = datetime.fromtimestamp(timestamp).isoformat()
            date_str = timestamp_str.split('T')[0]
        else:
            date_str = "1970-01-01"
        return date_str

    @staticmethod
    def is_valid_timestamp(timestamp):
        try:
            datetime.fromtimestamp(timestamp)
            return True
        except (OSError, ValueError):
            return False
