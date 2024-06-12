from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, DoubleType, IntegerType, FloatType
import sqlite3

from src.models.earthquake import Earthquake
from src.models.earthquake_factory import EarthquakeFactory
from src.services.earthquake_service import EarthquakeService
from src.utils.map_creator import create_map


class ETLProcess:
    @staticmethod
    def extract(start_time, min_magnitude):
        earthquakes_data = EarthquakeService.get_earthquakes_to_today(start_time, min_magnitude)
        if earthquakes_data:
            print(f"Number of earthquakes: {len(earthquakes_data)}")
            earthquakes = [EarthquakeFactory.create_earthquake(data) for data in earthquakes_data]
            for earthquake in earthquakes:
                print(earthquake)
            return earthquakes
        else:
            print("No earthquakes found.")
            return None

    @staticmethod
    def transform(spark, earthquakes):
        # Convert list of Earthquake objects to list of tuples
        earthquake_tuples = [
            (eq.event_id, eq.magnitude, eq.location, eq.date, eq.tsunami_warning, eq.longitude, eq.latitude) for eq in
            earthquakes]

        # Define the schema explicitly
        schema = StructType([
            StructField("EVENT_ID", StringType(), True),
            StructField("MAGNITUDE", StringType(), True),
            StructField("LOCATION", StringType(), True),
            StructField("DATE", StringType(), True),
            StructField("TSUNAMI_WARNING", IntegerType(), True),
            StructField("LONGITUDE", DoubleType(), True),
            StructField("LATITUDE", DoubleType(), True)
        ])

        # Create Spark DataFrame from the list of tuples using the defined schema
        df = spark.createDataFrame(earthquake_tuples, schema)
        return df

    @staticmethod
    def load(df):
        # Convert Spark DataFrame to Pandas DataFrame
        pandas_df = df.toPandas()

        # Load the data into SQLite
        conn = sqlite3.connect('db/earthquakes.db')
        pandas_df.to_sql('earthquakes', conn, if_exists='replace', index=False)
        conn.close()

        print("Data loaded to SQLite successfully.")

        # Create map with earthquake data
        earthquakes = [
            Earthquake(row.EVENT_ID, row.MAGNITUDE, row.LOCATION, row.DATE, row.TSUNAMI_WARNING, row.LONGITUDE,
                       row.LATITUDE) for index, row in pandas_df.iterrows()]
        create_map(earthquakes)
