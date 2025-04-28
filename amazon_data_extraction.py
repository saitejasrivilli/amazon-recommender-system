import pandas as pd
import psycopg2

# Connect to PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    database="user_events_db",
    user="saitejasrivillibhutturu",
    password="",
    port=5432
)

# SQL query to fetch a SAMPLE of records
query = """
SELECT reviewer_id, asin, overall
FROM amazon_ratings
WHERE overall IS NOT NULL
LIMIT 10000;  -- Limit to 10,000 rows for now to prevent memory issues
"""

# Load into DataFrame
df = pd.read_sql_query(query, conn)

print("Sample Amazon Ratings:")
print(df.head())

# Create User-Product Interaction Matrix
# Limit it by filtering out any products with too few reviews
interaction_matrix = df.pivot_table(
    index='reviewer_id',
    columns='asin',
    values='overall',
    fill_value=0
)

# Check the shape of the interaction matrix
print("\nUser-Product Interaction Matrix Shape:", interaction_matrix.shape)

# Save to a pickle file (incrementally save chunks if too large)
interaction_matrix.to_pickle('amazon_interaction_matrix_sample.pkl')

conn.close()

print("Amazon interaction matrix saved successfully!")
