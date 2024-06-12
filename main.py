from src.etl.etl_process import ETLProcess
from src.etl.session import spark


def main():

    start_time = "1900-01-01"
    min_magnitude = 7.0

    # Run ETL process
    earthquakes = ETLProcess.extract(start_time, min_magnitude)
    if earthquakes:
        df = ETLProcess.transform(spark, earthquakes)
        ETLProcess.load(df)
    else:
        print("No earthquakes found.")


if __name__ == "__main__":
    main()
