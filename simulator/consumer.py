import json

from kafka import KafkaConsumer

from config import KAFKA_BROKER, KAFKA_TOPIC


consumer = KafkaConsumer(
    KAFKA_TOPIC,
    bootstrap_servers=KAFKA_BROKER,

    auto_offset_reset="earliest",

    enable_auto_commit=True,

    value_deserializer=lambda x: json.loads(x.decode("utf-8"))
)


print("Listening for telemetry events...\n")

for message in consumer:

    event = message.value

    print("=" * 60)

    print(
        json.dumps(
            event,
            indent=4
        )
    )