from src.models.earthquake_factory import EarthquakeFactory
from src.services.earthquake_service import EarthquakeService
from src.utils.map_creator import create_map


def main():
    start_time = "1900-01-01"
    min_magnitude = 7.0

    earthquakes_data = EarthquakeService.get_earthquakes_to_today(start_time, min_magnitude)

    if earthquakes_data:
        print(f"Number of earthquakes: {len(earthquakes_data)}")
        earthquakes = [EarthquakeFactory.create_earthquake(data) for data in earthquakes_data]
        for earthquake in earthquakes:
            print(earthquake)

        # Create map with earthquake data
        create_map(earthquakes)
    else:
        print("No earthquakes found.")


if __name__ == "__main__":
    main()
