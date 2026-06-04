import json
import re
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# ==============================
# PREPROCESS FUNCTION
# ==============================

def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9 ]', '', text)
    return text

# ==============================
# LOAD DATASET
# ==============================

with open("intelligent_dataset.json", "r", encoding="utf-8") as f:
    data = json.load(f)

intent_texts = []
intent_labels = []
retrieval_texts = []

for item in data:

    intent_texts.append(preprocess(item["topic"]))
    intent_labels.append(item["type"])

    combined_text = item["topic"]

    if "content" in item:
        combined_text += " " + item["content"]

    if "aim" in item:
        combined_text += " " + item["aim"]

    if "theory" in item:
        combined_text += " " + item["theory"]

    if "apparatus" in item:
        combined_text += " " + item["apparatus"]

    if "procedure" in item:
        combined_text += " " + " ".join(item["procedure"])

    if "precautions" in item:
        combined_text += " " + " ".join(item["precautions"])

    if "result" in item:
        combined_text += " " + item["result"]

    if "rules" in item:
        combined_text += " " + " ".join(item["rules"])

    retrieval_texts.append(preprocess(combined_text))

# ==============================
# INTENT CLASSIFIER
# ==============================

vectorizer_intent = TfidfVectorizer(
    ngram_range=(1,2),
    stop_words="english"   # 🔥 IMPORTANT FIX
)

X_intent = vectorizer_intent.fit_transform(intent_texts)

model = LogisticRegression(max_iter=1000, class_weight='balanced')
model.fit(X_intent, intent_labels)

# ==============================
# RETRIEVAL VECTORIZER
# ==============================

vectorizer_retrieval = TfidfVectorizer(
    ngram_range=(1,2),
    stop_words="english"   # 🔥 IMPORTANT FIX
)

vectorizer_retrieval.fit(retrieval_texts)

# ==============================
# SAVE FILES
# ==============================

pickle.dump(model, open("intent_model.pkl", "wb"))
pickle.dump(vectorizer_intent, open("vectorizer_intent.pkl", "wb"))
pickle.dump(vectorizer_retrieval, open("vectorizer_retrieval.pkl", "wb"))

print("✅ Model trained and saved successfully.")