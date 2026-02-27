import os
import pickle
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

# -----------------------
# Paths to model files
# -----------------------
BASE_DIR = os.path.dirname(__file__)  # folder where app.py is
MODEL_PATH = os.path.join(BASE_DIR, "sentiment_model.pkl")
VECT_PATH = os.path.join(BASE_DIR, "vectorizer.pkl")

# -----------------------
# Load model and vectorizer
# -----------------------
with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

with open(VECT_PATH, "rb") as f:
    vectorizer = pickle.load(f)

# -----------------------
# Create FastAPI app
# -----------------------
app = FastAPI()

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],       # allow all origins; replace with your frontend URL for production
    allow_credentials=True,
    allow_methods=["*"],       # allow GET, POST, etc.
    allow_headers=["*"],
)

# -----------------------
# Input schema
# -----------------------
class TextInput(BaseModel):
    text: str

# -----------------------
# Prediction endpoint
# -----------------------
@app.post("/predict")
def predict_sentiment(data: TextInput):
    try:
        # Transform input text
        features = vectorizer.transform([data.text])
        # Predict
        prediction = model.predict(features)[0]
        # Map numeric label to string
        sentiment = "positive" if int(prediction) == 1 else "negative"
        return {"sentiment": sentiment}
    except Exception as e:
        # Catch any error and return
        return {"error": str(e)}
