from fastapi import FastAPI
from pydantic import BaseModel
import gzip
import pickle
import numpy as np
import pandas as pd

# ---- load compressed interaction matrix -------------
with gzip.open('amazon_interaction_matrix_sample.pkl.gz', 'rb') as f:
    interaction_matrix = pickle.load(f)

# ---- load compressed SVD model --------------
with gzip.open('amazon_svd_model.pkl.gz', 'rb') as f:
    svd = pickle.load(f)

# ---- precompute latent features -------------
latent_matrix = svd.transform(interaction_matrix)

# ---- create FastAPI app -------------
app = FastAPI()

# ---- request schema -------------
class RecommendRequest(BaseModel):
    user_id: str
    top_n: int = 5

# ---- recommendation function -------------
def recommend_products(user_id: str, top_n: int = 5):
    if user_id not in interaction_matrix.index:
        return {"error": "User not found!"}
    
    user_idx = interaction_matrix.index.get_loc(user_id)
    user_vector = latent_matrix[user_idx]
    
    # compute scores for all products
    scores = np.dot(user_vector, svd.components_)
    product_ids = interaction_matrix.columns
    
    # build a DataFrame of product scores
    scores_df = pd.DataFrame({
        "product_id": product_ids,
        "score": scores
    }).sort_values("score", ascending=False)
    
    # return top N
    top_recs = scores_df.head(top_n).to_dict(orient="records")
    return {"user_id": user_id, "recommendations": top_recs}

# ---- API endpoint -------------
@app.post("/recommend/")
async def get_recommendations(request: RecommendRequest):
    return recommend_products(request.user_id, request.top_n)
