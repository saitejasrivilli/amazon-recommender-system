import pandas as pd
import psycopg2

# Direct psycopg2 connection
conn = psycopg2.connect(
    host="localhost",
    database="user_events_db",
    user="saitejasrivillibhutturu",  # your Mac username
    password="",                     # leave empty if no password
    port=5432
)

# SQL query
query = """
SELECT user_id, product_id, event_type
FROM user_events
WHERE event_type IN ('view', 'purchase')
"""

# Load data into DataFrame using psycopg2 connection
df = pd.read_sql_query(query, conn)

print("Sample events data:")
print(df.head())

# Create interaction matrix
interaction_matrix = df.groupby(['user_id', 'product_id']).size().unstack(fill_value=0)

print("\nUser-Product Interaction Matrix:")
print(interaction_matrix.head())

# Close connection
conn.close()
interaction_matrix.to_pickle('interaction_matrix.pkl')
