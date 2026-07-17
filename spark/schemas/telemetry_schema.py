from pyspark.sql.types import *

telemetry_schema = StructType([
    StructField("metadata", StructType([
        StructField("event_id", StringType()),
        StructField("event_type", StringType()),
        StructField("event_version", StringType()),
        StructField("timestamp", StringType())
    ])),
    StructField("payload", StructType([
    StructField("vehicle_id", StringType()),
    StructField("driver_id", StringType()),
    StructField("delivery_id", StringType()),
    StructField("route_id", StringType()),

    StructField("latitude", DoubleType()),
    StructField("longitude", DoubleType()),

    StructField("speed_kmph", DoubleType()),
    StructField("heading", IntegerType()),

    StructField("fuel_level_percent", DoubleType()),
    StructField("odometer_km", DoubleType()),
    StructField("remaining_distance_km", DoubleType(), True),
    StructField("eta_minutes", DoubleType(), True),
    StructField("engine_status", StringType()),
    StructField("vehicle_status", StringType()),

    StructField("traffic_signal", StringType()),
    StructField("traffic_density", StringType()),

    StructField("weather", StringType()),

    StructField("cargo_weight_kg", DoubleType()),

    StructField("battery_voltage", DoubleType()),
    StructField("engine_temperature", DoubleType())
]))
])