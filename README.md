# 📊 Customer Review Sentiment Analysis Dashboard

An **interactive Natural Language Processing (NLP) dashboard** that analyzes customer product reviews and predicts whether the sentiment is **Positive 😊, Neutral 😐, or Negative 😡**.

Built using **Machine Learning and Streamlit**, this project demonstrates how businesses can automatically analyze thousands of customer reviews to understand customer satisfaction and feedback.

---

## 🚀 Streamlit Application

```
https://customer-review-sentiment-dashboard-3nympkkvxgvinsvx2ghisb.streamlit.app
```
---

## 🧠 Project Overview

Customer reviews contain valuable insights about products and services. However, manually reading thousands of reviews is inefficient.

This project solves that problem by building an **AI-powered sentiment analysis system** that automatically classifies reviews into:

• 😊 Positive  
• 😐 Neutral  
• 😡 Negative  

The application provides an **interactive analytics dashboard** where users can:

- Predict sentiment of custom reviews
- Analyze sentiment distribution in the dataset
- Visualize common words using WordCloud
- Explore dataset insights through charts

---

## ✨ Key Features

✅ Real-time **Sentiment Prediction** for custom reviews  
✅ Interactive **Streamlit Dashboard**  
✅ **Sentiment Distribution Visualization** using Plotly  
✅ **Word Cloud Analysis** for review text  
✅ Machine Learning pipeline with **TF-IDF + Logistic Regression**  
✅ Clean and modular project structure  

---

## 🛠 Technologies Used

### Programming Language
- Python

### Data Processing
- Pandas
- NumPy

### Natural Language Processing
- NLTK (stopwords, word_tokenize, punkt)

### Machine Learning
- Scikit-learn
- TF-IDF Vectorization
- Logistic Regression

### Visualization
- Plotly
- Matplotlib
- WordCloud

### Web Application
- Streamlit

---

## 📂 Project Structure

```
Customer-Sentiment-Dashboard
│
├── app.py
├── requirements.txt
├── README.md
│
├── model
│   ├── sentiment_model.pkl
│   └── tfidf_vectorizer.pkl
│
├── notebook
│   └── sentiment_analysis.ipynb
│
├── dataset
|   └── reviews_sample.csv

```

---

## ⚙️ Machine Learning Workflow

1. Dataset Collection  
2. Data Cleaning and Preparation  
3. Text Preprocessing  
4. Feature Extraction using **TF-IDF Vectorization**  
5. Model Training using **Logistic Regression**  
6. Model Evaluation  
7. Streamlit Dashboard Development  
8. Visualization and Insights  

---

## 🧪 Example Predictions

Example Input:

```
This product is amazing and works perfectly
```

Predicted Output:

```
Positive 😊
```
---

Example Input:

```
Worst purchase ever, waste of money
```

Predicted Output:

```
Negative 😡
```
---
Example Input:

```
The product is okay but nothing special
```

Predicted Output:

```
Neutral 😐
```

---

---

## 📦 Installation & Setup

Clone the repository:

```
git clone https://github.com/bhavyasripasileti/customer-review-sentiment-dashboard.git
```

Navigate to the project directory:

```
cd customer-review-sentiment-dashboard
```

Install dependencies:

```
pip install -r requirements.txt
```

Run the Streamlit application:

```
streamlit run app.py
```

---

## 🎯 Future Enhancements

- Deep learning models for improved sentiment detection  
- Real-time review scraping  
- Advanced NLP models (BERT / Transformers)  
- Cloud deployment with CI/CD pipelines  

---

## 👨‍💻 Author

**Bhavya Sri Pasileti**

BTech Student | Data Science & AI Enthusiast  
Passionate about building **AI-powered data products and intelligent systems**.
