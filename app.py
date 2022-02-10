import streamlit as st
from sentiment.model import get_sentiment_analysis


text = st.text_input("Text:")

if text:
    label, score = get_sentiment_analysis(text)
    st.write(f"Inputed text is: {text}")
    st.write(f"Sentiment: {label}")
    st.write("What is the confidence score of this analysis")
    st.progress(score)