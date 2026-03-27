<div align="center">

# 📊 Customer Review Sentiment Analysis Dashboard

### Understand customer sentiment at scale — instantly.

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org)
[![NLTK](https://img.shields.io/badge/NLTK-NLP-4B8BBE?style=for-the-badge)](https://www.nltk.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)](LICENSE)

<br/>

> An interactive NLP-powered dashboard that automatically classifies customer product reviews as **Positive 😊**, **Neutral 😐**, or **Negative 😡** — built with TF-IDF, Logistic Regression, and Streamlit.

<br/>

**[🚀 Live Demo](#-live-app) · [📖 ML Workflow](#️-machine-learning-workflow) · [🐛 Report Bug](../../issues) · [✨ Request Feature](../../issues)**

</div>

---

## 🌐 Live App

> 🔗 **[Click here to try the dashboard live »](https://customer-review-sentiment-dashboard-3nympkkvxgvinsvx2ghisb.streamlit.app)**

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Key Features](#-key-features)
- [Machine Learning Workflow](#️-machine-learning-workflow)
- [Example Predictions](#-example-predictions)
- [Project Structure](#-project-structure)
- [Tech Stack](#️-tech-stack)
- [Getting Started](#-getting-started)
- [Roadmap](#-roadmap)
- [Author](#-author)

---

## 🔍 Overview

Customer reviews contain invaluable insights about products and services — but manually reading thousands of entries is simply not scalable.

This project solves that problem by building an **AI-powered sentiment analysis system** that automatically classifies any review into one of three categories:

| Label | Sentiment | Example |
|---|---|---|
| 😊 Positive | Satisfied customer | *"This product is amazing and works perfectly"* |
| 😐 Neutral | Mixed or indifferent | *"The product is okay but nothing special"* |
| 😡 Negative | Dissatisfied customer | *"Worst purchase ever, waste of money"* |

The application provides an **interactive analytics dashboard** where users can predict sentiment on custom text, explore dataset distributions, and visualize word patterns through WordClouds.

---

## ✨ Key Features

| Feature | Description |
|---|---|
| 🔮 **Real-Time Prediction** | Predict sentiment on any custom review instantly |
| 📊 **Sentiment Distribution** | Interactive Plotly charts of dataset sentiment breakdown |
| ☁️ **Word Cloud Analysis** | Visual frequency analysis of review vocabulary |
| 📁 **Dataset Explorer** | Browse and filter the underlying review dataset |
| ⚙️ **ML Pipeline** | TF-IDF vectorization + Logistic Regression end-to-end |
| 🧩 **Modular Structure** | Clean, maintainable, and extendable codebase |

---

## ⚙️ Machine Learning Workflow

```
Step 1 — Data Collection
  └─ Customer product reviews dataset (CSV)

Step 2 — Data Cleaning & Preparation
  ├─ Remove nulls, duplicates, and noise
  └─ Normalize text casing and punctuation

Step 3 — Text Preprocessing (NLTK)
  ├─ Tokenization
  ├─ Stopword removal
  └─ Stemming / Lemmatization

Step 4 — Feature Extraction
  └─ TF-IDF Vectorization → sparse numeric feature matrix

Step 5 — Model Training
  └─ Logistic Regression classifier (multi-class)

Step 6 — Model Evaluation
  └─ Accuracy, Precision, Recall, F1-Score

Step 7 — Serialization
  ├─ sentiment_model.pkl      (trained classifier)
  └─ tfidf_vectorizer.pkl     (fitted vectorizer)

Step 8 — Dashboard Deployment
  └─ Streamlit Cloud — live web app
```

---

## 🧪 Example Predictions

```python
Input:   "This product is amazing and works perfectly"
Output:  Positive 😊
```

```python
Input:   "The product is okay but nothing special"
Output:  Neutral 😐
```

```python
Input:   "Worst purchase ever, waste of money"
Output:  Negative 😡
```

---

## 📂 Project Structure

```
customer-review-sentiment-dashboard/
│
├── app.py                          # 🖥  Streamlit dashboard (UI + prediction logic)
├── requirements.txt                # 📦  Project dependencies
├── README.md                       # 📄  Project documentation
│
├── model/
│   ├── sentiment_model.pkl         # 🤖  Serialized Logistic Regression model
│   └── tfidf_vectorizer.pkl        # 🔢  Serialized TF-IDF vectorizer
│
├── notebook/
│   └── sentiment_analysis.ipynb   # 📓  Exploratory analysis & model training
│
└── dataset/
    └── reviews_sample.csv          # 📊  Sample review dataset
```

---

## 🛠️ Tech Stack

| Category | Technology |
|---|---|
| Language | Python 3.9+ |
| Data Processing | Pandas, NumPy |
| NLP | NLTK (tokenization, stopwords, punkt) |
| ML Framework | Scikit-learn |
| Feature Extraction | TF-IDF Vectorization |
| Classifier | Logistic Regression |
| Visualization | Plotly, Matplotlib, WordCloud |
| Dashboard | Streamlit |
| Deployment | Streamlit Cloud |

---

## Getting Started

### Prerequisites

- Python 3.9 or higher
- pip package manager

### Installation

**1. Clone the repository**
```bash
git clone https://github.com/bhavyasripasileti/customer-review-sentiment-dashboard.git
cd customer-review-sentiment-dashboard
```

**2. (Optional) Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate        # macOS / Linux
venv\Scripts\activate           # Windows
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Run the dashboard**
```bash
streamlit run app.py
```

The app will open automatically at `http://localhost:8501`.

---

## 🗺 Roadmap

- [ ] 🤗 Advanced NLP with BERT / Transformers for higher accuracy
- [ ] 🌐 Real-time review scraping from e-commerce platforms
- [ ] 🔁 CI/CD pipeline for automated retraining & deployment
- [ ] 📊 Per-product and per-category sentiment trends
- [ ] 🌍 Multi-language sentiment support

---

## 👤 Author

**Bhavya Sri Pasileti**

> Data Science & AI Enthusiast
> Passionate about building AI-powered data products and intelligent NLP systems.

[LinkedIn](https://linkedin.com/in/your-profile)

---

<div align="center">

**Found this project useful? Give it a ⭐ — it goes a long way!**

*Built with ❤️ by Bhavya Sri Pasileti*

</div>
