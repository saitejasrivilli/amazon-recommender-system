# Amazon Product Recommender System

[![Live Demo](https://img.shields.io/badge/Live-Demo-brightgreen)](https://amazon-recommender-system.onrender.com/docs)  
[![Python](https://img.shields.io/badge/Python-3.11-blue)](https://www.python.org/)  
[![License](https://img.shields.io/badge/License-MIT-red)](LICENSE)

A production-ready **Amazon Electronics Recommender** built with **FastAPI**, **SVD Matrix Factorization**, and **PostgreSQL**, deployed on **Render**.  
Provides personalized product recommendations based on users’ historical ratings.

---

## 📍 Live Demo

▶️ **Swagger UI / API docs**  
https://amazon-recommender-system.onrender.com/docs


---

## 🚀 Tech Stack

- **Language:** Python 3.11  
- **Web API:** FastAPI + Uvicorn  
- **Data Storage:** PostgreSQL  
- **ML:** scikit-learn (Truncated SVD)  
- **Data Processing:** pandas, numpy  
- **Database Driver:** psycopg2-binary  
- **Deployment:** Render.com (Free Tier)  
- **Version Control:** Git & GitHub  

---

## 💾 Installation & Run Locally

1. **Clone** the repo  
   ```bash
   git clone https://github.com/saitejasrivilli/amazon-recommender-system.git
   cd amazon-recommender-system  
POST /recommend/
Content-Type: application/json

{
  "user_id": "A0586418108XHQA8T1IQO",
  "top_n": 5
}
{
  "user_id": "A0586418108XHQA8T1IQO",
  "recommendations": [
    {"product_id": "B00004T8R2", "score": 0.0234},
    {"product_id": "B00004WCIC", "score": 0.0211},
    ...
  ]
}
