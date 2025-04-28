from kafka import KafkaConsumer
import psycopg2
import json

# Kafka consumer setup
consumer = KafkaConsumer(
    'user_events',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    value_deserializer=lambda v: json.loads(v.decode('utf-8'))
)

# PostgreSQL connection setup
conn = psycopg2.connect(
    host="localhost",
    database="user_events_db",
    user="saitejasrivillibhutturu",   # <-- your mac username
    password="",                      # leave blank if no password
    port=5432
)
cur = conn.cursor()

# Insert function
def insert_event(event):
    cur.execute(
        """
        INSERT INTO user_events (user_id, event_type, product_id, event_timestamp)
        VALUES (%s, %s, %s, %s)
        """,
        (event['user_id'], event['event_type'], event['product_id'], event['timestamp'])
    )
    conn.commit()

# Main loop
print("Listening for events and saving to database...")

for message in consumer:
    event = message.value
    print(f"Received event: {event}")
    insert_event(event)
