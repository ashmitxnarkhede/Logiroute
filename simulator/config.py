import os
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

KAFKA_BROKER = os.getenv("KAFKA_BROKER")
KAFKA_TOPIC = os.getenv("KAFKA_TOPIC")

TOTAL_VEHICLES = int(os.getenv("TOTAL_VEHICLES"))
UPDATE_INTERVAL = float(os.getenv("UPDATE_INTERVAL"))