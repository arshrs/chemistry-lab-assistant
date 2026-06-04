import json
import re
import pickle
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

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

texts = []
labels = []

for item in data:
    texts.append(preprocess(item["topic"]))
    labels.append(item["type"])

# ==============================
# LOAD TRAINED MODEL + VECTORIZER
# ==============================

model = pickle.load(open("intent_model.pkl", "rb"))
vectorizer_intent = pickle.load(open("vectorizer_intent.pkl", "rb"))

# ==============================
# SPLIT DATA (SAME RANDOM STATE)
# ==============================

X_train, X_test, y_train, y_test = train_test_split(
    texts, labels, test_size=0.2, random_state=42, stratify=labels
)

# 🔥 IMPORTANT: USE transform ONLY (NO fit)
X_test_vec = vectorizer_intent.transform(X_test)

# ==============================
# PREDICT
# ==============================

predictions = model.predict(X_test_vec)

accuracy = accuracy_score(y_test, predictions)

print("\n==============================")
print("MODEL EVALUATION RESULTS")
print("==============================")
print(f"\nAccuracy: {accuracy:.2f}")
print("\nClassification Report:\n")
print(classification_report(y_test, predictions))

# ==============================
# CONFUSION MATRIX
# ==============================

cm = confusion_matrix(y_test, predictions)

plt.figure()
sns.heatmap(cm, annot=True, fmt='d')
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()