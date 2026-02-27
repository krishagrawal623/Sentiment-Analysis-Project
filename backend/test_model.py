import pickle

with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

with open("sentiment_model.pkl", "rb") as f:
    model = pickle.load(f)

X = vectorizer.transform(["I loved that movie"])
print("Prediction:", model.predict(X))
