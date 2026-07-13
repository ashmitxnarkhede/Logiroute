from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_json

from schemas.telemetry_schema import telemetry_schema


spark = (
    SparkSession.builder
    .appName("LogiRoute Stream Processor")
    .master("local[*]")
    .config(
        "spark.jars.packages",
        "org.apache.spark:spark-sql-kafka-0-10_2.13:4.1.2"
    )
    .getOrCreate()
)

spark.sparkContext.setLogLevel("WARN")


raw_df = (
    spark.readStream
    .format("kafka")
    .option("kafka.bootstrap.servers", "kafka:9092")
    .option("subscribe", "vehicle-telemetry")
    .option("startingOffsets", "latest")
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


query = (
    telemetry_df
    .writeStream
    .format("console")
    .outputMode("append")
    .option("truncate", False)
    .start()
)

query.awaitTermination()