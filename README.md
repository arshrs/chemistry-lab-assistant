# 🧪 Chemistry Lab Assistant

An AI-powered educational assistant designed to help students understand chemistry concepts, experiments, and laboratory procedures through an interactive chat interface.

The application combines a React frontend, an Express.js backend, and a Machine Learning model built using TF-IDF vectorization and Logistic Regression to provide intelligent responses based on user queries.

---

## 📌 Overview

Chemistry Lab Assistant serves as a virtual chemistry tutor that helps students learn theoretical concepts and laboratory practices through natural language conversations.

The system classifies user intent using Machine Learning and retrieves the most relevant response from a curated chemistry knowledge base using cosine similarity.

---

## ✨ Features

### 🤖 Intelligent Chemistry Chatbot

* Interactive chat-based learning experience.
* Answers chemistry-related questions instantly.
* Provides guidance on laboratory concepts and experiments.

### 🎤 Voice Recognition

* Supports voice input for hands-free interaction.
* Converts speech into text for processing.

### 🧠 Machine Learning-Based Response System

* Intent classification using Logistic Regression.
* TF-IDF vectorization for text processing.
* Cosine similarity matching for response retrieval.

### 📚 Educational Knowledge Base

* Uses a structured chemistry dataset.
* Covers concepts, experiments, and laboratory procedures.
* Provides contextually relevant responses.

### 💡 Suggested Topics

* Displays predefined chemistry topics.
* Helps students explore concepts quickly.

---

## 🛠️ Tech Stack

### Frontend

* React.js
* JavaScript
* HTML5
* CSS3

### Backend

* Node.js
* Express.js

### Machine Learning

* Python
* Scikit-learn
* TF-IDF Vectorizer
* Logistic Regression
* Cosine Similarity

### Data Storage

* JSON Dataset

---

## 📂 Project Structure

```text
Chemistry-Lab-Assistant/
│
├── frontend/
│   ├── App.js
│   ├── App.css
│   └── package.json
│
├── backend/
│   ├── server.js
│   └── package.json
│
└── ml-model/
    ├── train.py
    ├── predict.py
    ├── intelligent_dataset.json
    ├── model.pkl
    └── vectorizer.pkl
```

## ⚙️ How It Works

### User Interaction

1. User enters a chemistry-related question.
2. React frontend sends the query to the Express backend.
3. Backend forwards the request to a Python prediction script.
4. The Machine Learning model classifies the user's intent.
5. Cosine similarity identifies the most relevant response from the chemistry dataset.
6. The response is returned to the user through the chat interface.

---

## 🔄 System Architecture

```text
User
 ↓
React Frontend
 ↓
Express.js Backend
 ↓
Python ML Engine
 ↓
Intent Classification
 ↓
Response Retrieval
 ↓
Chemistry Dataset
 ↓
Response Returned to User
```

---

## 📊 Machine Learning Pipeline

### Training Phase

* Data preprocessing
* Text cleaning
* TF-IDF vectorization
* Logistic Regression training
* Model serialization using Pickle

### Prediction Phase

* Query preprocessing
* Intent classification
* Similarity matching
* Response generation

---

## 🎯 Learning Outcomes

This project helped develop practical skills in:

* Machine Learning
* Natural Language Processing (NLP)
* Information Retrieval
* React Development
* Backend API Development
* Python Programming
* Educational Technology Solutions

---

## 🚀 Future Enhancements

* Integration with Large Language Models (LLMs)
* Experiment simulation support
* Chemical equation balancing
* Interactive laboratory visualizations
* Multi-language support
* Student progress tracking
* Personalized learning recommendations

---

## 👨‍💻 Author

Developed as an AI-powered educational assistant to make chemistry learning more interactive, accessible, and engaging for students.
