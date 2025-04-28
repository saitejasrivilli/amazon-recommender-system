from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import numpy as np
import pickle

# Load Amazon interaction matrix and SVD model
interaction_matrix = pd.read_pickle('amazon_interaction_matrix_sample.pkl')

with open('amazon_svd_model.pkl', 'rb') as f:
    svd = pickle.load(f)

# Precompute the latent features
latent_matrix = svd.transform(interaction_matrix)

# Create FastAPI app
app = FastAPI()

# Request schema
class RecommendRequest(BaseModel):
    user_id: str
    top_n: int = 5

# Recommendation function
def recommend_products(user_id, top_n=5):
    if user_id not in interaction_matrix.index:
        return {"error": "User not found!"}
    
    user_idx = interaction_matrix.index.get_loc(user_id)
    user_vector = latent_matrix[user_idx]
    
    scores = np.dot(user_vector, svd.components_)
    
    product_ids = interaction_matrix.columns
    
    scores_df = pd.DataFrame({
        'product_id': product_ids,
        'score': scores
    }).sort_values(by='score', ascending=False)

    top_recommendations = scores_df.head(top_n).to_dict(orient="records")
    return {"user_id": user_id, "recommendations": top_recommendations}

# API Endpoint
@app.post("/recommend/")
async def get_recommendations(request: RecommendRequest):
    return recommend_products(request.user_id, request.top_n)
