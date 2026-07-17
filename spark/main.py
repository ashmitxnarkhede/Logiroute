from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_json
from schemas.telemetry_schema import telemetry_schema
from pyspark.sql.functions import to_timestamp



spark = (
    SparkSession.builder
    .appName("LogiRoute")
    .master("local[*]")
    .getOrCreate()
)

spark.sparkContext.setLogLevel("ERROR")

print("Connected to Spark!")

from pyspark.sql.functions import col, from_json
from schemas.telemetry_schema import telemetry_schema


raw_df = (
    spark.readStream
    .format("kafka")
    .option("kafka.bootstrap.servers", "kafka:29092")
    .option("subscribe", "vehicle-telemetry")
    .option("startingOffsets", "earliest")
    .load()
)

json_df = raw_df.selectExpr("CAST(value AS STRING) AS json")

telemetry_df = (
    json_df
    .select(
        from_json(
            col("json"),
            telemetry_schema
        ).alias("data")
    )
    .select("data.*")
)

db_df = (
    telemetry_df
    .select(
        col("metadata.event_id").alias("event_id"),
        to_timestamp(
            col("metadata.timestamp")
        ).alias("event_timestamp"),

        col("payload.vehicle_id").alias("vehicle_id"),
        col("payload.driver_id").alias("driver_id"),
        col("payload.delivery_id").alias("delivery_id"),
        col("payload.route_id").alias("route_id"),

        col("payload.latitude").alias("latitude"),
        col("payload.longitude").alias("longitude"),

        col("payload.speed_kmph").alias("speed"),
        col("payload.fuel_level_percent").alias("fuel_level"),
        col("payload.remaining_distance_km").alias("remaining_distance_km"),
        col("payload.eta_minutes").alias("eta_minutes"),
        col("payload.vehicle_status").alias("status")
    )
)

print("Schema loaded successfully")
telemetry_df.printSchema()

def write_to_postgres(batch_df, batch_id):

    print(f"Writing batch {batch_id}")

    (
        batch_df.write
        .format("jdbc")
        .option("url", "jdbc:postgresql://postgres:5432/logiroute")
        .option("dbtable", "vehicle_telemetry")
        .option("user", "postgres")
        .option("password", "postgres")
        .option("driver", "org.postgresql.Driver")
        .mode("append")
        .save()
    )


query = (
    db_df
    .writeStream
    .foreachBatch(write_to_postgres)
    .option(
        "checkpointLocation",
        "/opt/logiroute/checkpoints/postgres"
    )
    .start()
)

print("Streaming to PostgreSQL...")

query.awaitTermination()

