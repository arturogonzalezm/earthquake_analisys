from pyspark.sql import SparkSession


class SparkSessionBuilder:
    builder = SparkSession.builder
    log_level = "WARN"  # Default log level

    @staticmethod
    def with_master(master):
        SparkSessionBuilder.builder = SparkSessionBuilder.builder.master(master)
        return SparkSessionBuilder

    @staticmethod
    def with_app_name(app_name):
        SparkSessionBuilder.builder = SparkSessionBuilder.builder.appName(app_name)
        return SparkSessionBuilder

    @staticmethod
    def with_log_level(log_level):
        SparkSessionBuilder.log_level = log_level
        return SparkSessionBuilder

    @staticmethod
    def build():
        spark_session = SparkSessionBuilder.builder.enableHiveSupport().getOrCreate()
        sc = spark_session.sparkContext
        sc.setLogLevel(SparkSessionBuilder.log_level)
        return spark_session


def create_spark_session(master="local[*]", app_name="PySpark App", log_level="WARN"):
    return (
        SparkSessionBuilder
        .with_master(master)
        .with_app_name(app_name)
        .with_log_level(log_level)
        .build()
    )


# spark = create_spark_session(master="spark://localhost:7077", log_level="INFO")
spark = create_spark_session(app_name="PySpark Installation Test")
