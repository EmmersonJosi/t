import streamlit as st
import joblib

# Load the pre-trained machine learning model
model = joblib.load('sentiment_model.pkl')

# Set a title and description for your app
st.title("Sentiment Analysis App")
st.write("Enter a sentence, and I'll predict its sentiment (positive, negative, or neutral).")

# Create a text input widget
user_input = st.text_input("Enter a sentence:", "I love this product!")

# Define a function to make predictions
def predict_sentiment(text):
    sentiment = model.predict([text])[0]
    return sentiment

# Make predictions and display results
if st.button("Analyze"):
    if user_input:
        result = predict_sentiment(user_input)
        st.write("Predicted Sentiment:", result)
    else:
        st.warning("Please enter a sentence.")

# Add a footer
st.write("By Your Name")