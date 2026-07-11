from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("LogiRoute")
    .master("local[*]")
    .config(
        "spark.jars.packages",
        "org.apache.spark:spark-sql-kafka-0-10_2.13:4.1.2"
    )
    .getOrCreate()
)

spark.sparkContext.setLogLevel("ERROR")

print("Connected to Spark!")

df = (
    spark.readStream
    .format("kafka")
    .option("kafka.bootstrap.servers", "localhost:9092")
    .option("subscribe", "vehicle-telemetry")
    .option("startingOffsets", "latest")
    .load()
)

query = (
    df.writeStream
    .format("console")
    .outputMode("append")
    .start()
)

query.awaitTermination()