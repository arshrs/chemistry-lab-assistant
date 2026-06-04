import sys
import re
import json
import pickle
from sklearn.metrics.pairwise import cosine_similarity

# ==============================
# PREPROCESS
# ==============================

def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9 ]', '', text)
    return text

# ==============================
# LOAD MODEL
# ==============================

model = pickle.load(open("intent_model.pkl", "rb"))
vectorizer_intent = pickle.load(open("vectorizer_intent.pkl", "rb"))
vectorizer_retrieval = pickle.load(open("vectorizer_retrieval.pkl", "rb"))

with open("intelligent_dataset.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# ==============================
# INPUT
# ==============================

if len(sys.argv) < 2:
    print("Please ask a question.")
    sys.exit()

user_input = sys.argv[1]
processed = preprocess(user_input)

# ==============================
# INTENT PREDICTION
# ==============================

intent_vector = vectorizer_intent.transform([processed])
predicted_intent = model.predict(intent_vector)[0]

# ==============================
# FIND BEST MATCH
# ==============================

best_score = 0
best_item = None

for item in data:

    if item["type"] == predicted_intent:

        topic_processed = preprocess(item["topic"])
        topic_vector = vectorizer_retrieval.transform([topic_processed])

        user_vector = vectorizer_retrieval.transform([processed])

        score = cosine_similarity(user_vector, topic_vector)[0][0]

        if score > best_score:
            best_score = score
            best_item = item

# ==============================
# FORMAT OUTPUT BASED ON TYPE
# ==============================

if best_item is None:
    print("Sorry, I couldn't understand your question.")
    sys.exit()

if best_item["type"] in ["definition", "student_question", "formula", "greeting"]:
    print(best_item["content"])

elif best_item["type"] == "safety":
    print("Safety Guidelines:")
    for rule in best_item["rules"]:
        print("- " + rule)

elif best_item["type"] == "experiment":

    print("Experiment:", best_item["topic"].title())
    print("\nAim:", best_item.get("aim", ""))

    if "theory" in best_item:
        print("\nTheory:", best_item["theory"])

    if "apparatus" in best_item:
        print("\nApparatus:", best_item["apparatus"])

    if "procedure" in best_item:
        print("\nProcedure:")
        for step in best_item["procedure"]:
            print("- " + step)

    if "precautions" in best_item:
        print("\nPrecautions:")
        for p in best_item["precautions"]:
            print("- " + p)

    if "result" in best_item:
        print("\nResult:", best_item["result"])

else:
    print("Sorry, I couldn't understand your question.")