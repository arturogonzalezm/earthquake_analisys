class Earthquake:
    def __init__(self, event_id, magnitude, location, date, tsunami_warning, longitude, latitude):
        self.event_id = event_id
        self.magnitude = magnitude
        self.location = location
        self.date = date
        self.tsunami_warning = tsunami_warning
        self.longitude = longitude
        self.latitude = latitude

    def __str__(self):
        return (f"ID: {self.event_id}, Magnitude: {self.magnitude}, Location: {self.location}, "
                f"Date: {self.date}, Tsunami Warning: {self.tsunami_warning}, Longitude: {self.longitude}, "
                f"Latitude: {self.latitude}")
