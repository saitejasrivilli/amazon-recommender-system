import pandas as pd

# Load your interaction matrix
interaction_matrix = pd.read_pickle('amazon_interaction_matrix_sample.pkl')

# Print first 5 user IDs
print(interaction_matrix.index.tolist()[:5])
