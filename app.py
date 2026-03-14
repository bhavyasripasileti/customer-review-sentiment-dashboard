import streamlit as st
import pandas as pd
import pickle
import plotly.express as px
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# PAGE CONFIG

st.set_page_config(
    page_title="Customer Review Sentiment Dashboard",
    page_icon="📊",
    layout="wide"
)

# LOAD DATA

@st.cache_data
def load_data():
    df = pd.read_csv("dataset/reviews_sample.csv")

    # Use smaller sample for faster app performance
    df = df[['Text','Score']].sample(50000, random_state=42)

    return df

df = load_data()

# LOAD MODEL

model = pickle.load(open("model/sentiment_model.pkl","rb"))
tfidf = pickle.load(open("model/tfidf_vectorizer.pkl","rb"))

# SENTIMENT FUNCTION

def predict_sentiment(review):

    vector = tfidf.transform([review])
    prediction = model.predict(vector)

    return prediction[0]

# SIDEBAR

menu = st.sidebar.selectbox(
    "Navigation",
    [
        "Home",
        "Sentiment Predictor",
        "Dataset Insights",
        "WordCloud"
    ]
)

# HOME PAGE

if menu == "Home":

    st.title("📊 Customer Review Sentiment Analysis Dashboard")

    st.write("""
    This dashboard analyzes **customer product reviews** and predicts whether the review sentiment is:

    - 😊 Positive
    - 😐 Neutral
    - 😡 Negative
    """)

    st.subheader("Dataset Overview")

    total_reviews = len(df)

    positive = len(df[df['Score'] > 3])
    neutral = len(df[df['Score'] == 3])
    negative = len(df[df['Score'] < 3])

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Reviews", total_reviews)
    col2.metric("Positive Reviews", positive)
    col3.metric("Neutral Reviews", neutral)
    col4.metric("Negative Reviews", negative)

# SENTIMENT PREDICTOR

elif menu == "Sentiment Predictor":

    st.title("🧠 Review Sentiment Predictor")

    st.write("Enter a customer review below to analyze sentiment.")

    review = st.text_area("Enter Customer Review")

    if st.button("Predict Sentiment"):

        prediction = predict_sentiment(review)

        if prediction == "Positive":
            st.success("😊 Positive Review")

        elif prediction == "Negative":
            st.error("😡 Negative Review")

        else:
            st.warning("😐 Neutral Review")

    st.subheader("Example Reviews")

    st.write("""
    Try these examples:

    - This product is amazing and I love it
    - Worst purchase ever, waste of money
    - The product is okay but nothing special
    """)

# DATASET INSIGHTS

elif menu == "Dataset Insights":

    st.title("📈 Dataset Insights")

    df['Sentiment'] = df['Score'].apply(
        lambda x: "Positive" if x > 3 else "Neutral" if x == 3 else "Negative"
    )

    sentiment_counts = df['Sentiment'].value_counts().reset_index()
    sentiment_counts.columns = ['Sentiment','Count']

    fig = px.bar(
        sentiment_counts,
        x='Sentiment',
        y='Count',
        color='Sentiment',
        title="Sentiment Distribution"
    )

    st.plotly_chart(fig, use_container_width=True)

# WORD CLOUD

elif menu == "WordCloud":

    st.title("☁️ Word Cloud")

    df['Sentiment'] = df['Score'].apply(
        lambda x: "Positive" if x > 3 else "Neutral" if x == 3 else "Negative"
    )

    sentiment_option = st.selectbox(
        "Select Sentiment",
        ["Positive","Negative"]
    )

    # Use sample for faster word cloud generation
    sample_reviews = df[df['Sentiment']==sentiment_option]['Text'].sample(3000, random_state=42)

    text = " ".join(sample_reviews)

    wordcloud = WordCloud(
        width=800,
        height=400,
        background_color="white"
    ).generate(text)

    fig, ax = plt.subplots()

    ax.imshow(wordcloud)
    ax.axis("off")

    st.pyplot(fig)

# FOOTER

st.sidebar.write("---")
st.sidebar.write("Built with ❤️ using Streamlit")
