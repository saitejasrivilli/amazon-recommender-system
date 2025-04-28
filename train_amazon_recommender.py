import pandas as pd
import pickle
from sklearn.decomposition import TruncatedSVD

# Load the Amazon interaction matrix
interaction_matrix = pd.read_pickle('amazon_interaction_matrix_sample.pkl')

# Fill any missing values
interaction_matrix = interaction_matrix.fillna(0)

# Build SVD model
svd = TruncatedSVD(n_components=50)  # 50 latent features for bigger Amazon data
latent_matrix = svd.fit_transform(interaction_matrix)

print("Latent matrix shape:", latent_matrix.shape)

# Save model and matrix
with open('amazon_svd_model.pkl', 'wb') as f:
    pickle.dump(svd, f)

print("Amazon SVD model trained and saved ✅")
