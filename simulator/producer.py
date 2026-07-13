import json

from kafka import KafkaProducer

from config import KAFKA_BROKER


producer = KafkaProducer(
    bootstrap_servers=KAFKA_BROKER,
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)


def publish(topic, event):
    print("Publishing Event:")
    print(json.dumps(event, indent=2))
    future = producer.send(topic, event)

    metadata = future.get(timeout=10)
    producer.flush()
    print(
        f"""
Published Successfully

Topic      : {metadata.topic}
Partition  : {metadata.partition}
Offset     : {metadata.offset}
"""
    )