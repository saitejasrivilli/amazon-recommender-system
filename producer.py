from kafka import KafkaProducer
from faker import Faker
import json
import random
import time

# Initialize Kafka producer
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Faker instance to generate fake users/events
fake = Faker()

# Event types to simulate
event_types = ['view', 'click', 'add_to_cart', 'purchase']

# Function to generate a fake event
def generate_event():
    return {
        "user_id": fake.uuid4(),
        "event_type": random.choice(event_types),
        "product_id": fake.uuid4(),
        "timestamp": fake.iso8601()
    }

# Send events in a loop
if __name__ == "__main__":
    topic = 'user_events'
    while True:
        event = generate_event()
        producer.send(topic, value=event)
        print(f"Sent event: {event}")
        time.sleep(1)  # Send one event per second
