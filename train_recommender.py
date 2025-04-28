import pandas as pd
import pickle
from sklearn.decomposition import TruncatedSVD

# Load your interaction matrix
interaction_matrix = pd.read_pickle('interaction_matrix.pkl')

# Fill missing values
interaction_matrix = interaction_matrix.fillna(0)

# Build the model
svd = TruncatedSVD(n_components=20)  # Compress down to 20 latent features
latent_matrix = svd.fit_transform(interaction_matrix)

print("Latent feature matrix shape:")
print(latent_matrix.shape)

# Save model and matrix
with open('svd_model.pkl', 'wb') as f:
    pickle.dump(svd, f)

interaction_matrix.to_pickle('interaction_matrix.pkl')  # Save matrix separately if needed

print("Model training completed and saved!")
