import pandas as pd
import numpy as np
import pickle

# Load the interaction matrix
interaction_matrix = pd.read_pickle('interaction_matrix.pkl')

# Load the trained SVD model
with open('svd_model.pkl', 'rb') as f:
    svd = pickle.load(f)

# Transform the interaction matrix into latent space
latent_matrix = svd.transform(interaction_matrix)

# Function to get recommendations
def recommend_products(user_id, top_n=5):
    if user_id not in interaction_matrix.index:
        print(f"User {user_id} not found!")
        return []
    
    user_idx = interaction_matrix.index.get_loc(user_id)
    user_vector = latent_matrix[user_idx]
    
    # Predict scores for all products
    scores = np.dot(user_vector, svd.components_)
    
    # Get product IDs
    product_ids = interaction_matrix.columns
    
    # Create a DataFrame of product scores
    scores_df = pd.DataFrame({
        'product_id': product_ids,
        'score': scores
    }).sort_values(by='score', ascending=False)
    
    # Return top-N recommendations
    return scores_df.head(top_n)

# Example usage:
user = interaction_matrix.index[0]  # Pick a random user
recommendations = recommend_products(user)

print(f"Top recommendations for user {user}:\n")
print(recommendations)
