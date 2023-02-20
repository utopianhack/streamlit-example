import streamlit as st
import nltk
from nltk.util import ngrams
from collections import Counter

def extract_ngrams(text, n):
    # Tokenize the text
    tokens = nltk.word_tokenize(text.lower())
    # Create the ngrams
    n_grams = ngrams(tokens, n)
    # Count the ngrams
    ngram_freq = Counter(n_grams)
    return ngram_freq
  
# Set the page title
st.title("Most common ngrams")

# Add a text input box for the user to enter the text
text_input = st.text_input("Enter text here:")

# Add a slider to choose the n-gram size
n = st.slider("Choose n-gram size:", 2, 5, 3)

# Call the extract_ngrams function and display the results as a pie chart
if text_input:
    ngram_freq = extract_ngrams(text_input, n)
    labels = [' '.join(ngram) for ngram in ngram_freq.keys()]
    values = list(ngram_freq.values())
    st.pyplot(fig1)
