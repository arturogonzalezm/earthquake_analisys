import folium


def create_map(earthquakes):
    # Create a map centered around the average location of the earthquakes
    avg_lat = sum([eq.latitude for eq in earthquakes]) / len(earthquakes)
    avg_lon = sum([eq.longitude for eq in earthquakes]) / len(earthquakes)
    m = folium.Map(location=[avg_lat, avg_lon], zoom_start=2)

    # Add a marker for each earthquake
    for earthquake in earthquakes:
        folium.Marker(
            location=[earthquake.latitude, earthquake.longitude],
            popup=str(earthquake),
            icon=folium.Icon(color="red", icon="info-sign")
        ).add_to(m)

    # Save the map to an HTML file
    m.save("data/earthquakes_map.html")
